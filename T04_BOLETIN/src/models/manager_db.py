# Archivo: src/models/manager_db.py

import psycopg  # Biblioteca para gestionar la conexión con PostgreSQL
from utils import utils_db, utils_path  # Constantes para la configuración de la base de datos
import os  # Manejo de rutas y validación de existencia de archivos
from utils.utils_popup import _printv2
from typing import Optional


class ManagerDB:
    """
    Clase para gestionar la conexión a la base de datos utilizando psycopg.

    Proporciona métodos para inicializar, recuperar y cerrar conexiones de forma centralizada,
    utilizando parámetros configurados externamente. También incluye la funcionalidad opcional
    de mostrar mensajes emergentes (popups) para notificaciones de estado.
    """

    def __init__(self, show_popup: bool = False, popup_parent: Optional[object] = None):
        """
        Inicializa una instancia de ManagerDB con opciones configurables.

        Parámetros:
        - show_popup (bool): Indica si se utilizarán popups para mostrar mensajes.
        - popup_parent (QWidget | None): Widget padre opcional para asociar los popups con una ventana principal.
        """
        self._connection = None  # Referencia a la conexión de la base de datos
        self._show_popup = show_popup  # Indicador para habilitar mensajes emergentes
        self._popup_parent = popup_parent  # Widget padre opcional para popups

        # Validar las configuraciones de la base de datos al inicializar la clase
        self._validate_db_config()
    # __init__ (fin)

    def _validate_db_config(self):
        """
        Valida que todas las configuraciones de la base de datos en utils_db.py estén completas.

        Lanza una excepción si alguna configuración está incompleta.
        """
        if not utils_db.NAME_DB or not utils_db.USER_DB or not utils_db.PASS_DB \
                        or not utils_db.HOSTNAME_DB or not utils_db.PORT_DB:
            raise ValueError("Las configuraciones de la base de datos en utils_db.py no están completas.")
    # _validate_db_config (fin)

    def open_connection(self) -> bool:
        """
        Abre una conexión a la base de datos utilizando los parámetros configurados.

        Si la conexión falla, se registra el error en la consola y se muestra un popup (si está habilitado).

        Retorno:
        - bool: True si la conexión se estableció exitosamente, False en caso contrario.
        """
        messages = []  # Lista para acumular mensajes de estado
        try:
            self._connection = psycopg.connect(
                dbname=utils_db.NAME_DB,
                user=utils_db.USER_DB,
                password=utils_db.PASS_DB,
                host=utils_db.HOSTNAME_DB,
                port=utils_db.PORT_DB
            )
            messages.append("Conexión a la base de datos establecida exitosamente.")
            return True
        except Exception as e:
            messages.append(f"Error al abrir la conexión a la base de datos:\n{e}")
            self._connection = None  # Reinicia la conexión en caso de error
            return False
        finally:
            # Emite los mensajes acumulados
            self._emit_messages(messages)
    # open_connection (fin)

    def get_connection(self) -> Optional[psycopg.Connection]:
        """
        Retorna la conexión activa a la base de datos.

        Retorno:
        - psycopg.Connection: Instancia activa si la conexión está abierta.
        - None: Si no hay una conexión activa o si la conexión está cerrada.
        """
        if self._connection and not self._connection.closed:
            return self._connection
        messages = ["La conexión a la base de datos no está activa o ha sido cerrada."]
        self._emit_messages(messages)
        return None
    # get_connection (fin)
    
    
    def init_db(self, sql_file_path: str = utils_path.PATH_INICIALIZACION_DB) -> None:
        """
        Inicializa la base de datos ejecutando instrucciones SQL desde un archivo.

        Parámetros:
        - sql_file_path (str): Ruta del archivo SQL que contiene las instrucciones para inicializar la base de datos.

        Si el archivo no existe o ocurre un error durante la ejecución, se captura y notifica.
        """
        messages = []  # Lista para acumular mensajes de estado

        # Verifica si la conexión está activa
        if not self.get_connection():
            print("La conexión no estaba abierta. Intentando abrir conexión...")
            if not self.open_connection():
                return  # Detiene la ejecución si no se pudo abrir la conexión

        # Verifica la existencia del archivo SQL
        if not os.path.exists(sql_file_path):
            messages.append("Error: No se encontró el archivo SQL especificado.")
            self._emit_messages(messages)
            return

        # Intenta leer y ejecutar el archivo SQL
        try:
            with open(sql_file_path, 'r', encoding='utf-8') as file:
                sql_script = file.read()

            connection = self.get_connection()
            if not connection:
                messages.append("No se pudo obtener una conexión activa.")
                self._emit_messages(messages)
                return

            with connection.cursor() as cursor:
                sql_statements = sql_script.split(';')
                for statement in sql_statements:
                    statement = statement.strip()
                    if statement:  # Ejecuta solo si hay una instrucción válida
                        try:
                            cursor.execute(statement)
                        except Exception as e:
                            messages.append(f"Error ejecutando la instrucción:\n{statement}\n{e}")
                connection.commit()
                messages.append("Base de datos inicializada exitosamente.")
        except Exception as e:
            messages.append(f"Error al inicializar la base de datos:\n{e}")
        finally:
            # Emite los mensajes acumulados
            self._emit_messages(messages)
    # init_db (fin)

    def close_connection(self) -> bool:
        """
        Cierra la conexión a la base de datos si está activa.

        Asegura que los recursos se liberen adecuadamente. Si no hay conexión activa,
        se notifica mediante consola y popup (si está habilitado).

        Retorno:
        - bool: True si la conexión se cerró exitosamente, False si no había conexión activa.
        """
        messages = []  # Lista para acumular mensajes de estado
        if self._connection and not self._connection.closed:
            self._connection.close()
            messages.append("Conexión a la base de datos cerrada exitosamente.")
            self._emit_messages(messages)
            return True
        else:
            messages.append("No hay una conexión activa que cerrar.")
            self._emit_messages(messages)
            return False
    # close_connection (fin)

    def _emit_messages(self, messages: list[str]) -> None:
        """
        Emite mensajes acumulados en forma de popup y los registra en la consola.

        Parámetros:
        - messages (list[str]): Lista de mensajes a emitir.
        """
        if messages:
            message_text = "".join(messages)
            _printv2(
                show_popup=self._show_popup,
                parent=self._popup_parent,
                message=message_text,
                duration=5000  # Duración predeterminada del popup
            )
    # _emit_messages (fin)

# ManagerDB (fin)
