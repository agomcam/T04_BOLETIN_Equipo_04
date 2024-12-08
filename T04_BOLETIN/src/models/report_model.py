"""
WEBGRAFIA:
- psycopg.rows.dict_row. (s. f.). Psycopg.org. de https://www.psycopg.org/psycopg3/docs/api/rows.html#psycopg.rows.dict_row
- information_schema.columns. (s. f.). Postgresql.org. de https://www.postgresql.org/docs/current/infoschema-columns.html
- Python fetchall() Method. (s. f.). W3Schools.com. de https://www.w3schools.com/python/ref_cursor_fetchall.asp
"""
# Archivo: src/models/report_model.py

from typing import List, Dict, Optional, Union
import psycopg  # Biblioteca para consultas SQL
from utils.utils_popup import _printv2  # Utilidad para mostrar popups
from utils import utils_db


class ReportModel:
    """
    Clase para gestionar operaciones de datos utilizando psycopg.

    Facilita la ejecución de consultas SQL y la obtención de datos
    desde PostgreSQL, utilizando la conexión administrada por ManagerDB.
    """

    def __init__(self, db_manager, popup_parent: Optional[object] = None) -> None:
        """
        Inicializa el ReportModel utilizando una instancia de ManagerDB.

        Parámetros:
        - db_manager: Instancia de ManagerDB para gestionar la conexión a la base de datos.
        - popup_parent: Widget padre opcional para mostrar popups.
        """
        self._db_manager = db_manager
        self._popup_parent = popup_parent
    # __init__ (fin)

    def _fetch_data(self, table_name: str) -> Optional[List[Dict[str, Union[str, int, float]]]]:
        """
        Obtiene todos los datos de una tabla específica desde PostgreSQL.

        Parámetros:
        - table_name: Nombre de la tabla en PostgreSQL.

        Retorno:
        - Lista de registros obtenidos como diccionarios clave-valor.
        - None si ocurre un error.
        """
        if not self._validate_table_name(table_name):
            _printv2(show_popup=False, parent=self._popup_parent, message=f"Tabla '{table_name}' no es válida.")
            return None

        try:
            connection = self._db_manager.get_connection()
            if connection is None:
                raise ValueError("No hay una conexión activa a la base de datos.")

            query = f"SELECT * FROM {table_name};"
            with connection.cursor(row_factory=psycopg.rows.dict_row) as cursor:
                cursor.execute(query)
                data = []
                for row in cursor.fetchall():
                    data.append(row)  # Construimos la lista de registros explícitamente
                return data
        except Exception as e:
            _printv2(show_popup=False, parent=self._popup_parent, message=f"Error al obtener datos de '{table_name}': {e}")
            return None
    # _fetch_data (fin)

    def _fetch_columns(self, table_name: str) -> Optional[List[str]]:
        """
        Obtiene los nombres de las columnas de una tabla específica desde PostgreSQL.

        Parámetros:
        - table_name: Nombre de la tabla en PostgreSQL.

        Retorno:
        - Lista de nombres de las columnas.
        - None si ocurre un error.
        """
        if not self._validate_table_name(table_name):
            _printv2(show_popup=False, parent=self._popup_parent, message=f"Tabla '{table_name}' no es válida.")
            return None

        try:
            connection = self._db_manager.get_connection()
            if connection is None:
                raise ValueError("No hay una conexión activa a la base de datos.")

            query = f"""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = '{table_name}';
            """
            with connection.cursor() as cursor:
                cursor.execute(query)
                columns = []
                for row in cursor.fetchall():
                    columns.append(row[0])  # Construimos la lista de columnas explícitamente
                return columns
        except Exception as e:
            _printv2(show_popup=False, parent=self._popup_parent, message=f"Error al obtener columnas de '{table_name}': {e}")
            return None
    # _fetch_columns (fin)

    def _get_model(self, table_name: str) -> Optional[Dict[str, Union[List[str], List[Dict[str, Union[str, int, float]]]]]]:
        """
        Obtiene los datos y columnas de una tabla específica desde PostgreSQL.

        Parámetros:
        - table_name: Nombre de la tabla en PostgreSQL.

        Retorno:
        - Diccionario con "columns" y "data".
        - None si ocurre un error.
        """
        if not self._validate_table_name(table_name):
            _printv2(show_popup=False, parent=self._popup_parent, message=f"Tabla '{table_name}' no es válida.")
            return None

        try:
            columns = self._fetch_columns(table_name)
            if columns is None:
                raise ValueError(f"No se pudieron obtener columnas de '{table_name}'.")

            data = self._fetch_data(table_name)
            if data is None:
                raise ValueError(f"No se pudieron obtener datos de '{table_name}'.")

            return {"columns": columns, "data": data}
        except Exception as e:
            _printv2(show_popup=False, parent=self._popup_parent, message=f"Error al obtener modelo de '{table_name}': {e}")
            return None
    # _get_model (fin)

    def _validate_table_name(self, table_name: str) -> bool:
        """
        Valida si el nombre de la tabla está permitido según la configuración.

        Parámetros:
        - table_name: Nombre de la tabla a validar.

        Retorno:
        - True si es válido, False en caso contrario.
        """
        for enum_table in utils_db.EnumTablasDB:
            if table_name == enum_table.value:
                return True
        return False
    # _validate_table_name (fin)

    def _close_connection(self) -> None:
        """
        Cierra la conexión a la base de datos delegando la lógica a ManagerDB.

        Esto asegura que la conexión se cierre correctamente cuando ya no sea necesaria.
        """
        try:
            self._db_manager.close_connection()
        except Exception as e:
            _printv2(show_popup=False, parent=self._popup_parent, message=f"Error al cerrar la conexión: {e}")
    # _close_connection (fin)
# ReportModel (fin)
