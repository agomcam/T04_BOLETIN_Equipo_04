# Archivo: src\views\report_view.py

from PySide6.QtWidgets import (
    QGridLayout, QWidget, QTableView, QLineEdit, QComboBox,
    QLabel, QSizePolicy, QPushButton
)
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QIcon
from widgets.custom_chart_widget import CustomChartWidget
from utils import utils_sizes, utils_path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from typing import List,Dict,Any
from utils.utils_popup import _printv2

class ReportView(QWidget):
    """
    Clase encargada de gestionar la interfaz de usuario para la visualización de informes.
    """
    # Definición de señales
    apply_filters_signal = Signal(str, str)  # Señal para aplicar filtros: texto de búsqueda y categoría
    generate_pdf_signal = Signal(list)  # Señal para generar el PDF con los datos filtrados

    def __init__(self):
        """
        Inicializa la vista de informes, configurando filtros, tabla de datos y gráficos.
        """
        super().__init__()
        self.filtered_data = []  # Almacena los datos filtrados
        # Configuración de la ventana
        self.setMinimumSize(
            utils_sizes.SIZE_MINIMUM_WIDTH_WIDGET,
            utils_sizes.SIZE_MINIMUM_HEIGHT_WIDGET
        )

        # Inicialización de componentes principales
        self._init_filters()
        self._init_table()
        self._init_summary()
        self._init_chart()
        self._init_pdf_button()  # Nuevo: Inicializa el botón de generar PDF

        # Configuración del diseño principal
        main_layout = QGridLayout()
        main_layout.addLayout(self.filters_layout, 0, 0, 1, 2)
        main_layout.addWidget(self.table_view, 1, 0, 1, 2)
        main_layout.addWidget(self.summary_label, 2, 0, 1, 1)
        main_layout.addWidget(self.chart_widget, 3, 0, 1, 2)
        main_layout.addWidget(self.generate_pdf_button, 4, 1, 1, 1)  # Nuevo: Añade el botón al diseño


        # Ajustes de márgenes y espaciado
        main_layout.setContentsMargins(
            utils_sizes.MARGIN_10, utils_sizes.MARGIN_10,
            utils_sizes.MARGIN_10, utils_sizes.MARGIN_10
        )
        main_layout.setHorizontalSpacing(utils_sizes.MARGIN_10)
        main_layout.setVerticalSpacing(utils_sizes.MARGIN_10)

        # Establecemos el diseño en la ventana
        self.setLayout(main_layout)
    # __init__ (fin)
    
    @Slot()
    def _emit_apply_filters_signal(self):
        search_text = self.search_input.text()
        category = self.category_select.currentText()
        self.apply_filters_signal.emit(search_text, category)

    def _init_pdf_button(self):
        self.generate_pdf_button = QPushButton("Generar PDF")
        self.generate_pdf_button.setIcon(QIcon(utils_path.PDF_ICON_PATH))  # Opcional
        self.generate_pdf_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.generate_pdf_button.clicked.connect(self._emit_generate_pdf_signal)

    @Slot()
    def _emit_generate_pdf_signal(self):
        if not self.filtered_data:
            _printv2(show_popup=True, parent=self, message="No hay datos para generar el PDF.")
            return
        self.generate_pdf_signal.emit(self.filtered_data)
    

    

    def _init_filters(self):
        """
        Inicializa los filtros de búsqueda y selección de categorías.
        """
        self.filters_layout = QGridLayout()

        # Barra de búsqueda
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar productos...")
        self.search_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.filters_layout.addWidget(QLabel("Buscar:"), 0, 0)
        self.filters_layout.addWidget(self.search_input, 0, 1)

        # Selector de categoría
        self.category_select = QComboBox()
        self.category_select.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.filters_layout.addWidget(QLabel("Categoría:"), 1, 0)
        self.filters_layout.addWidget(self.category_select, 1, 1)

        # Botón para aplicar filtros con icono
        self.apply_filter_button = QPushButton("Aplicar Filtros")
        self.apply_filter_button.setIcon(QIcon(utils_path.SEARCH_ICON_PATH))  # Añadimos el icono
        self.apply_filter_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.filters_layout.addWidget(self.apply_filter_button, 2, 1)

        # Conectar botón a la señal de filtros
        self.apply_filter_button.clicked.connect(self._emit_apply_filters_signal)
    # _init_filters (fin)

    def _init_table(self):
        """
        Configura la tabla de datos para mostrar los resultados.
        """
        self.table_view = QTableView()
        self.table_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    # _init_table (fin)

    def _init_summary(self):
        """
        Configura el resumen de datos, incluyendo el total de elementos y la suma total.
        """
        self.summary_label = QLabel(f"Total de elementos:0, Suma total: 0")
        self.summary_label.setAlignment(Qt.AlignLeft)
    # _init_summary (fin)
    def _set_number(self,total,suma_total):
        """
        Configura el resumen de datos, incluyendo el total de elementos y la suma total.
        """

        self.summary_label.setText(f"Total de elementos: {total}, Suma total: {suma_total}")


    def _init_chart(self):
        """
        Inicializa el espacio para gráficos utilizando el widget CustomChartWidget.
        """
        self.chart_widget = CustomChartWidget()
        self.chart_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    # _init_chart (fin)

    @Slot()
    def _emit_apply_filters_signal(self):
        """
        Emite la señal de aplicar filtros con los valores actuales de búsqueda y categoría.
        """
        search_text = self.search_input.text()
        category = self.category_select.currentText()
        self.apply_filters_signal.emit(search_text, category)
    # _emit_apply_filters_signal (fin)

    def _set_model(self, model):
        """
        Establece el modelo de datos en el QTableView y ajusta las columnas.

        Parámetros:
        - model (QStandardItemModel): Modelo de datos compatible con QTableView.
        """
        self.table_view.setModel(model)
        self.table_view.resizeColumnsToContents()
    # _set_model (fin)

    def _set_categories(self, categories):
        """
        Llena el combo box de categorías con los valores recibidos.

        Parámetros:
        - categories (list[str]): Lista de categorías obtenidas desde el controlador.
        """
        self.category_select.clear()
        self.category_select.addItem("Todas")  # Añadir opción predeterminada
        self.category_select.addItems(categories)
    # _set_categories (fin)

    def _set_chart(self, data):
        """
        Configura el gráfico utilizando el widget CustomChartWidget.

        Parámetros:
        - data (dict): Datos para el gráfico en el formato esperado por CustomChartWidget.
        """
        self.chart_widget._set_data(data)
    # _set_chart (fin)
# ReportView (fin)
