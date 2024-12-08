from typing import List, Dict, Any, Optional
from PySide6.QtCore import Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget
from utils import utils_db
from utils.utils_popup import _printv2
from models.report_model import ReportModel
from views.report_view import ReportView
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


class ReportController:
    """
    Controlador que actúa como intermediario entre el modelo y la vista,
    gestionando la lógica de la aplicación y la interacción entre la base de datos y la interfaz de usuario.
    """

    def __init__(self, report_view: ReportView, report_model: ReportModel, popup_parent: Optional[QWidget] = None):
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

    def _initialize_view(self) -> None:
        """
        Inicializa la vista cargando los datos iniciales y las categorías.
        """
        try:
            # Cargar datos iniciales de la tabla "tareas"
            model_data = self._model._get_model(utils_db.EnumTablasDB.TAREAS.value)
            if model_data:
                prepared_data = self._prepare_table_data(model_data)
                self._view._set_model(prepared_data)

                # Configurar el gráfico inicial
                chart_data = self._prepare_chart_data(model_data)
                self._view._set_chart(chart_data)

                # Calcular totales iniciales y actualizar el resumen
                totals = self._calculate_totals(model_data.get("data", []))
                self._view._set_number(totals["total"], totals["categories"])
            else:
                _printv2(parent=self._popup_parent, message="No se encontraron datos en la tabla 'tareas'.")
                self._view._clear_chart()

            # Cargar categorías y establecerlas en la vista
            categories_data = self._model._fetch_data(utils_db.EnumTablasDB.CATEGORIAS.value)
            if categories_data:
                allowed_categories = ["Ofimática", "Programación", "Ocio"]
                categories = [row["nombre_categoria"] for row in categories_data if row["nombre_categoria"] in allowed_categories]
                self._view._set_categories(categories)
        except Exception as e:
            _printv2(parent=self._popup_parent, message=f"Error al inicializar la vista: {e}")

    @Slot(str, str)
    def _apply_filters(self, search_text: str, category: str) -> None:
        """
        Aplica los filtros recibidos desde la vista y actualiza los datos mostrados.
        """
        CATEGORY_MAP = {
            1: "Ofimática",
            2: "Programación",
            3: "Ocio"
        }

        try:
            # Obtener los datos completos desde el modelo
            model_data = self._model._fetch_data(utils_db.EnumTablasDB.TAREAS.value)

            if not model_data:
                _printv2(parent=self._popup_parent, message="No se encontraron datos para aplicar filtros.")
                self._view._clear_chart()
                self._view._set_model(QStandardItemModel())
                self._view.filtered_data = []
                self._view._set_number(0, {"Ofimática": 0, "Programación": 0, "Ocio": 0})
                return

            # Filtrar datos según el texto de búsqueda y la categoría
            filtered_data = [
                row for row in model_data
                if (
                    not search_text.strip() or
                    search_text.lower() in str(row["id_categoria"]).lower() or
                    search_text.lower() in row["nombre"].lower() or
                    search_text.lower() in row["description"].lower() or
                    search_text.lower() in row["idusuario"].lower()
                ) and
                (category == "Todas" or CATEGORY_MAP.get(row["id_categoria"], "").lower() == category.lower())
            ]

            self._view.filtered_data = filtered_data
            if not filtered_data:
                _printv2(parent=self._popup_parent, message="No se encontraron datos con los filtros aplicados.")
                self._view._clear_chart()
                self._view._set_model(QStandardItemModel())
                self._view._set_number(0, {"Ofimática": 0, "Programación": 0, "Ocio": 0})
                return

            # Actualizar la tabla con los datos filtrados
            prepared_data = self._prepare_table_data({
                "columns": ["id_categoria", "nombre", "description", "idusuario"],
                "data": filtered_data,
            })
            self._view._set_model(prepared_data)

            # Calcular totales por categoría y actualizar resumen
            totals = self._calculate_totals(filtered_data)
            self._view._set_number(totals["total"], totals["categories"])

            # Filtrar y agrupar los datos para la gráfica
            chart_totals = totals["categories"]
            chart_data = {
                utils_db.EnumEjes.EJE_X.value: list(chart_totals.keys()),  # Categorías
                utils_db.EnumEjes.EJE_Y.value: {"Totales": list(chart_totals.values())}  # Totales
            }
            self._view._set_chart(chart_data)

        except Exception as e:
            _printv2(parent=self._popup_parent, message=f"Error al aplicar filtros: {e}")

    @Slot(list)
    def generate_pdf(self, data: List[Dict[str, Any]]) -> None:
        output_path = os.path.join(os.getcwd(), "reporte_tareas.pdf")
        chart_image_path = "temp_chart.png"  # Ruta temporal para guardar el gráfico

        try:
            # Guardar el gráfico como una imagen (asumiendo que `chart_widget` tiene este método)
            self._view.chart_widget.save_chart_as_image(chart_image_path)

            # Crear el PDF
            pdf = canvas.Canvas(output_path, pagesize=letter)
            pdf.setTitle("Reporte de Tareas Filtradas")
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, 750, "Reporte de Tareas Filtradas")
            pdf.setFont("Helvetica", 10)

            # Filtros aplicados
            y_position = 700

            # Datos filtrados
            if not data:
                pdf.drawString(50, y_position, "No se encontraron datos con los filtros aplicados.")
            else:
                for row in data:
                    if y_position < 50:  # Nueva página si queda poco espacio
                        pdf.showPage()
                        y_position = 750

                    pdf.setFont("Helvetica-Bold", 10)
                    pdf.drawString(50, y_position, "Nombre tarea: ")
                    pdf.setFont("Helvetica", 10)
                    pdf.drawString(150, y_position, row["nombre"])
                    y_position -= 20

                    pdf.setFont("Helvetica-Bold", 10)
                    pdf.drawString(50, y_position, "Descripción: ")
                    pdf.setFont("Helvetica", 10)
                    pdf.drawString(150, y_position, row["description"])
                    y_position -= 20

                    pdf.setFont("Helvetica-Bold", 10)
                    pdf.drawString(50, y_position, "Autor: ")
                    pdf.setFont("Helvetica", 10)
                    pdf.drawString(150, y_position, row["idusuario"])
                    y_position -= 40

            # Agregar el gráfico al PDF
            pdf.showPage()  # Crear una nueva página para el gráfico
            pdf.drawString(50, 750, "Gráfico de Datos")
            pdf.drawImage(chart_image_path, 50, 400, width=500, height=300)  # Ajustar dimensiones del gráfico

            # Guardar el PDF
            pdf.save()
            _printv2(show_popup=True, parent=self._popup_parent, message=f"PDF generado con éxito en: {output_path}")

        except Exception as e:
            error_msg = f"Error al generar el PDF: {e}"
            _printv2(show_popup=True, parent=self._popup_parent, message=error_msg)

        finally:
            # Eliminar el archivo temporal del gráfico
            if os.path.exists(chart_image_path):
                os.remove(chart_image_path)


    def _prepare_table_data(self, model_data: Dict[str, Any]) -> QStandardItemModel:
        qt_model = QStandardItemModel()
        columns = model_data.get("columns", [])
        qt_model.setHorizontalHeaderLabels(columns)

        for row in model_data.get("data", []):
            items = [QStandardItem(str(row.get(col, ""))) for col in columns]
            qt_model.appendRow(items)

        return qt_model

    def _prepare_chart_data(self, model_data: Dict[str, Any]) -> Dict[str, Any]:
        eje_x = model_data.get(utils_db.EnumEjes.EJE_X.value, [])
        barritas_datos = model_data.get(utils_db.EnumEjes.EJE_Y.value, {})

        return {
            utils_db.EnumEjes.EJE_X.value: eje_x,
            utils_db.EnumEjes.EJE_Y.value: barritas_datos
        }

    def _calculate_totals(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calcula los totales generales y por categoría.
        """
        CATEGORY_MAP = {
            1: "Ofimática",
            2: "Programación",
            3: "Ocio"
        }
        totals = {"Ofimática": 0, "Programación": 0, "Ocio": 0}
        for row in data:
            category_name = CATEGORY_MAP.get(row["id_categoria"], "")
            if category_name in totals:
                totals[category_name] += 1

        return {
            "total": sum(totals.values()),
            "categories": totals
        }
