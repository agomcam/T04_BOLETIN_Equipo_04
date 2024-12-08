from typing import Optional, Dict, List, Any
from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries
from PySide6.QtCharts import QBarCategoryAxis, QValueAxis
from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QToolTip
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter
from utils.utils_db import EnumEjes


class CustomChartWidget(QScrollArea):
    """
    Widget personalizado para mostrar gráficos de barras utilizando PySide6.
    Incluye soporte para scroll horizontal si el gráfico excede el tamaño visible.
    """

    def __init__(self, parent: Optional[QWidget] = None):
        """
        Inicializa el widget de gráfico de barras.

        Parámetros:
        - parent (Optional[QWidget]): Widget padre opcional.
        """
        super().__init__(parent)

        # Configurar el scroll
        self.setWidgetResizable(True)
        self._chart_container = QWidget()
        self._layout = QVBoxLayout(self._chart_container)
        self.setWidget(self._chart_container)

        # Crear el gráfico y añadirlo al contenedor
        self._chart = QChart()
        self._chart_view = QChartView(self._chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)
        self._layout.addWidget(self._chart_view)

        # Configuración inicial
        self._set_empty_chart()
    # __init__ (fin)

    def _set_data(self, data: Dict[str, Any]) -> None:
        """
        Configura los datos del gráfico de barras.

        Parámetros:
        - data (Dict[str, Any]): Diccionario con los datos para el gráfico.
        """
        eje_x: List[str] = data.get(EnumEjes.EJE_X.value, [])
        barritas_datos: Dict[str, List[int]] = data.get(EnumEjes.EJE_Y.value, {})

        if not eje_x or not barritas_datos:
            self._set_empty_chart()
            return

        # Limpiar el gráfico existente
        self._chart.removeAllSeries()
        self._chart.setTitle("Gráfico de ventas por producto")

        # Crear las series de barras
        bar_series = QBarSeries()

        # Agregar conjuntos de barras a la serie
        for name, values in barritas_datos.items():
            bar_set = QBarSet(name)

            for value in values:
                bar_set.append(value)

            # Conectar el evento hovered para mostrar un tooltip dinámico
            bar_set.hovered.connect(lambda status, index, bar_set=bar_set: self._show_tooltip(status, index, bar_set))
            bar_series.append(bar_set)

        # Añadir las series al gráfico
        self._chart.addSeries(bar_series)

        # Configurar los ejes
        self._configure_axes(eje_x, bar_series)
    # _set_data (fin)

    def _configure_axes(self, eje_x: List[str], bar_series: QBarSeries) -> None:
        """
        Configura los ejes del gráfico.

        Parámetros:
        - eje_x (List[str]): Categorías para el eje X.
        - bar_series (QBarSeries): Series de barras del gráfico.
        """
        # Elimina los ejes existentes
        for axis in self._chart.axes():
            self._chart.removeAxis(axis)

        # Crear y configurar el eje X
        axis_x = QBarCategoryAxis()
        axis_x.append(eje_x)
        axis_x.setLabelsAngle(-90)  # Rotar etiquetas para mejor visualización
        self._chart.setAxisX(axis_x, bar_series)

        # Crear y configurar el eje Y
        axis_y = QValueAxis()
        axis_y.setTitleText("Valores")
        axis_y.applyNiceNumbers()
        self._chart.setAxisY(axis_y, bar_series)

        # Ajustar el tamaño del gráfico para permitir scroll si es necesario
        self._chart_view.setMinimumWidth(len(eje_x) * 100)
    # _configure_axes (fin)

    def _set_empty_chart(self) -> None:
        """
        Configura un gráfico vacío con ejes visibles.
        """
        self._chart.removeAllSeries()
        self._chart.setTitle("Sin datos disponibles")

        axis_x = QBarCategoryAxis()
        axis_y = QValueAxis()
        axis_y.setRange(0, 10)
        axis_y.setTitleText("Valores")

        self._chart.setAxisX(axis_x)
        self._chart.setAxisY(axis_y)
    # _set_empty_chart (fin)

    def clear_chart(self) -> None:
        """
        Limpia el gráfico por completo.
        """
        self._set_empty_chart()
    # clear_chart (fin)

    def _show_tooltip(self, status: bool, index: int, bar_set: QBarSet) -> None:
        """
        Muestra un tooltip con información sobre la barra cuando el usuario pasa el ratón por encima.

        Parámetros:
        - status (bool): Indica si el ratón está sobre la barra.
        - index (int): Índice de la barra dentro del conjunto.
        - bar_set (QBarSet): Conjunto de barras al que pertenece la barra.
        """
        if status:
            value = bar_set.at(index)
            category = self._chart.axisX().categories()[index]
            QToolTip.showText(
                self.mapToGlobal(self._chart_view.pos() + QPoint(10, 10)),
                f"{category}: {value}"
            )
    # _show_tooltip (fin)
# CustomChartWidget (fin)
