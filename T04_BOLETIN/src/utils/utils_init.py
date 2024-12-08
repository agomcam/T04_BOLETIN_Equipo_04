# Archivo: src/utils/utils_init.py

from typing import Optional
from utils.utils_popup import _printv2  # Importamos la función de impresión y popup centralizada
from models.manager_db import ManagerDB  # Importamos el gestor de base de datos
from utils.utils_path import PATH_INICIALIZACION_DB  # Ruta del archivo SQL de inicialización


def initialize_app(
    show_popup: bool = False,
    popup_parent: Optional[object] = None,
    sql_file_path: str = PATH_INICIALIZACION_DB
) -> ManagerDB:
    """
    Inicializa los componentes principales de la aplicación.

    Configuramos elementos básicos como la conexión a la base de datos y ejecutamos
    scripts SQL para la inicialización.

    Parámetros:
    - show_popup (bool): Si es True, muestra popups para notificaciones (por defecto: False).
    - popup_parent (Optional[object]): Widget padre opcional para asociar los popups (por defecto: None).
    - sql_file_path (str): Ruta al archivo SQL para inicializar la base de datos (por defecto: PATH_INICIALIZACION_DB).

    Retorno:
    - ManagerDB: Instancia del gestor de la base de datos inicializado.

    Excepciones:
    - Lanza una excepción en caso de error crítico durante la inicialización.

    Ejemplo de uso:
        db_manager = initialize_app(show_popup=False, popup_parent=main_window)
    """
    # Inicialización del gestor de base de datos
    manager_db = ManagerDB(show_popup=show_popup, popup_parent=popup_parent)

    try:
        # Intentamos inicializar la base de datos
        manager_db.init_db(sql_file_path)

        # Notificamos si la inicialización fue exitosa
        if show_popup:
            _printv2(
                message="¡Aplicación inicializada correctamente!",
                parent=popup_parent,
                duration=4000  # Duración del popup en milisegundos
            )

    except Exception as e:
        # Informamos sobre errores críticos durante la inicialización
        error_message = f"Error durante la inicialización de la aplicación: {e}"
        _printv2(
            message=error_message,
            parent=popup_parent,
            duration=6000  # Mayor duración para notificaciones de error
        )
        raise RuntimeError(error_message)

    # Retornamos el gestor de la base de datos inicializado
    return manager_db
# initialize_app (fin)
