"""
* WEBGRAFÍA *

- QTableView Class. (s. f.). Doc.qt.io. de https://doc.qt.io/qtforpython-6.7/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView

- QStandardItemModel Class. (s. f.). Doc.qt.io. de https://doc.qt.io/qtforpython-6.7/PySide6/QtGui/QStandardItemModel.html#PySide6.QtGui.QStandardItemModel

- QStandardItem Class. (s. f.). Doc.qt.io. de https://doc.qt.io/qtforpython-6.7/PySide6/QtGui/QStandardItem.html#PySide6.QtGui.QStandardItem

"""

# Archivo: src\widgets\custom_table_widget.py

from PySide6.QtWidgets import QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem


class CustomTableWidget(QTableView):
    """
    Widget personalizado para mostrar tablas utilizando QTableView.
    Recibe datos en forma de diccionario y los renderiza automáticamente.
    """

    def __init__(self, data=None, parent=None):
        """
        Inicializa el widget de tabla y, opcionalmente, configura los datos iniciales.

        Parámetros:
        - data (dict | None): Diccionario que contiene los datos iniciales para la tabla.
          - "columns" (list[str]): Lista de nombres de las columnas.
          - "data" (list[dict]): Lista de filas, donde cada fila es un diccionario con clave/valor.
        - parent (QWidget | None): Widget padre opcional.
        """
        super().__init__(parent)

        # Inicializamos el modelo interno
        self._model = QStandardItemModel()
        self.setModel(self._model)

        # Si se proporcionan datos, configuramos la tabla
        if data:
            self._set_data(data)
    # __init__ (fin)

    def _set_data(self, data):
        """
        Configura los datos en la tabla.

        Parámetros:
        - data (dict): Diccionario que contiene:
          - "columns" (list[str]): Lista de nombres de las columnas.
          - "data" (list[dict]): Lista de filas, donde cada fila es un diccionario con clave/valor.

        Si los datos no son válidos o no contienen las claves requeridas, el método no realiza cambios.
        """
        if not data or not isinstance(data, dict):
            print("[ERROR] Los datos proporcionados no son válidos. Se esperaba un diccionario con 'columns' y 'data'.")
            return

        # Configurar columnas
        columns = data.get("columns", [])
        if not columns:
            print("[ERROR] No se encontraron columnas en los datos proporcionados.")
            return
        self._model.setHorizontalHeaderLabels(columns)

        # Limpiar filas actuales y agregar nuevas
        self._model.clear()
        for row in data.get("data", []):
            items = [QStandardItem(str(row.get(col, ""))) for col in columns]
            self._model.appendRow(items)

        # Ajustar el tamaño de las columnas automáticamente
        self.resizeColumnsToContents()
    # _set_data (fin)
# CustomTableWidget (fin)

