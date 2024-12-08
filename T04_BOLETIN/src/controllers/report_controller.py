from typing import List, Dict, Any, Optional
from PySide6.QtCore import Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget
from utils import utils_db
from utils.utils_popup import _printv2
from models.report_model import ReportModel
from views.report_view import ReportView
from widgets.custom_chart_widget import CustomChartWidget
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

class ReportController:
    """
    Controlador que actúa como intermediario entre el modelo y la vista,
    gestionando la lógica de la aplicación y la interacción entre la base de datos y la interfaz de usuario.
    """

    def __init__(self, report_view: ReportView, report_model: ReportModel, popup_parent: Optional[QWidget] = None):
        """
        Inicializa el controlador, configurando la vista, el modelo y el gestor de popups.

        Parámetros:
        - report_view (ReportView): Vista para mostrar la interfaz de usuario.
        - report_model (ReportModel): Modelo de datos para interactuar con la base de datos.
        - popup_parent (QWidget | None): Widget padre opcional para asociar los popups a la ventana principal.
        """
        if not report_view or not report_model:
            raise ValueError("Se requieren tanto la vista como el modelo para inicializar el controlador.")

        self._view: ReportView = report_view
        self._model: ReportModel = report_model
        self._popup_parent: Optional[QWidget] = popup_parent


        # Conectar señales
        self._view.apply_filters_signal.connect(self._apply_filters)
        self._view.generate_pdf_signal.connect(self.generate_pdf)


        # Inicializar vista
        self._initialize_view()
    # __init__ (fin)

    def _initialize_view(self) -> None:
        """
        Inicializa la vista cargando los datos iniciales y las categorías.
        """
        try:
            # Cargar datos iniciales de la tabla "tareas"
            model_data: Optional[Dict[str, Any]] = self._model._get_model(utils_db.EnumTablasDB.TAREAS.value)
            if model_data:
                prepared_data: QStandardItemModel = self._prepare_table_data(model_data)
                self._view._set_model(prepared_data)

                # Configurar el gráfico inicial
                chart_data = self._prepare_chart_data(model_data)
                self._view._set_chart(chart_data)
            else:
                _printv2(show_popup=False, parent=self._popup_parent, message="No se encontraron datos en la tabla 'tareas'.")
                self._view._clear_chart()

            # Cargar categorías
            categories_data: Optional[List[Dict[str, Any]]] = self._model._fetch_data(utils_db.EnumTablasDB.CATEGORIAS.value)
            if categories_data:
                categories: List[str] = [row["nombre_categoria"] for row in categories_data]
                self._view._set_categories(categories)
            else:
                _printv2(show_popup=False, parent=self._popup_parent, message="No se encontraron categorías.")
        except Exception as e:
            error_msg: str = f"Error al inicializar la vista: {e}"
            _printv2(show_popup=False, parent=self._popup_parent, message=error_msg)
    # _initialize_view (fin)

    @Slot(str, str)
    def _apply_filters(self, search_text: str, category: str) -> None:
        """
        Aplica los filtros recibidos desde la vista y actualiza los datos mostrados.

        Parámetros:
        - search_text (str): Texto ingresado en la barra de búsqueda.
        - category (str): Categoría seleccionada para filtrar.
        """
        CATEGORY_MAP = {
            1: "Ofimática",
            2: "Programación",
            3: "Ocio"
        }

        try:
            # Obtener los datos completos desde el modelo
            model_data: Optional[List[Dict[str, Any]]] = self._model._fetch_data(utils_db.EnumTablasDB.TAREAS.value)

            if not model_data:
                _printv2(show_popup=False, parent=self._popup_parent, message="No se encontraron datos para aplicar filtros.")
                self._view._clear_chart()
                self._view._set_model(QStandardItemModel())
                self._view.filtered_data = []
                return

            # Filtrar datos según el texto de búsqueda y la categoría
            filtered_data: List[Dict[str, Any]] = [
                row for row in model_data
                if (not search_text.strip() or search_text.lower() in row["nombre"].lower()) and
                (category == "Todas" or CATEGORY_MAP.get(row["id_categoria"], "").lower() == category.lower())
            ]
            
            self._view.filtered_data = filtered_data
            if not filtered_data:
                _printv2(show_popup=False, parent=self._popup_parent, message="No se encontraron datos con los filtros aplicados.")
                self._view._clear_chart()
                self._view._set_model(QStandardItemModel())
                return

            # Actualizar la tabla con los datos filtrados
            prepared_data: QStandardItemModel = self._prepare_table_data({
                "columns": ["id_categoria","nombre", "description", "idusuario"],
                "data": filtered_data,
            })
            self._view._set_model(prepared_data)
            # Actualizar el QLabel con el resumen
            total_elementos = len(filtered_data)
            suma_categorias = sum(row["id_categoria"] for row in filtered_data)
            self._view._set_number(total_elementos,suma_categorias)
            # Actualizar el gráfico con los datos filtrados
            chart_data = self._prepare_chart_data({
                utils_db.EnumEjes.EJE_X.value: [row["nombre"] for row in filtered_data],
                utils_db.EnumEjes.EJE_Y.value: {"Categoría": [int(row["id_categoria"]) for row in filtered_data] if filtered_data else []},
            })
            self._view._set_chart(chart_data)
            # Generar PDF con los datos filtrados
            #self.generate_pdf(filtered_data)
            

        except Exception as e:
            error_msg: str = f"Error al aplicar filtros: {e}"
            _printv2(show_popup=False, parent=self._popup_parent, message=error_msg)

    @Slot(list)
    def generate_pdf(self, data: List[Dict[str, Any]]) -> None:
        output_path = os.path.join(os.getcwd(), "reporte_tareas.pdf")
        try:
            pdf = canvas.Canvas(output_path, pagesize=letter)
            pdf.setTitle("Reporte de Tareas Filtradas")
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, 750, "Reporte de Tareas Filtradas")
            pdf.setFont("Helvetica", 10)

            y_position = 700
            for row in data:
                #pdf.drawString(50, y_position, f"Tarea: {row['nombre']}")
                pdf.drawString(50, y_position, f"Descripción: {row['description']}")
                #pdf.drawString(350, y_position, f"Categoría: {row['id_categoria']}")
                y_position -= 20
                if y_position < 50:
                    pdf.showPage()
                    y_position = 750

            pdf.save()
            _printv2(show_popup=True, parent=self._popup_parent, message=f"PDF generado con éxito en: {output_path}")
        except Exception as e:
            error_msg = f"Error al generar el PDF: {e}"
            _printv2(show_popup=True, parent=self._popup_parent, message=error_msg)

    def _prepare_table_data(self, model_data: Dict[str, Any]) -> QStandardItemModel:
        """
        Prepara los datos para ser usados en un QStandardItemModel, compatible con QTableView.

        Parámetros:
        - model_data (dict): Diccionario que contiene las columnas y los datos de la tabla.

        Retorno:
        - QStandardItemModel: Modelo de datos compatible con QTableView.
        """
        qt_model: QStandardItemModel = QStandardItemModel()

        # Configurar columnas
        columns: List[str] = model_data.get("columns", [])
        qt_model.setHorizontalHeaderLabels(columns)

        # Agregar filas
        for row in model_data.get("data", []):
            items: List[QStandardItem] = [QStandardItem(str(row.get(col, ""))) for col in columns]
            qt_model.appendRow(items)

        return qt_model
    # _prepare_table_data (fin)

    def _prepare_chart_data(self, model_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepara los datos estructurados para graficar en el CustomChartWidget.

        Parámetros:
        - model_data (dict): Diccionario que contiene los datos estructurados.

        Retorno:
        - dict: Datos en el formato esperado por CustomChartWidget.
        """
        eje_x: List[str] = model_data.get(utils_db.EnumEjes.EJE_X.value, [])
        barritas_datos: Dict[str, List[int]] = model_data.get(utils_db.EnumEjes.EJE_Y.value, {})

        return {
            utils_db.EnumEjes.EJE_X.value: eje_x,
            utils_db.EnumEjes.EJE_Y.value: barritas_datos
        }
    # _prepare_chart_data (fin)
# ReportController (fin)
