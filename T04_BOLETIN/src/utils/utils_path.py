# Archivo: src\utils\utils_path.py

import os  # Importamos os para gestionar las rutas de archivos y directorios

# Definimos la ruta base del proyecto, dos niveles por encima del directorio actual.
# Esto nos permitirá acceder a rutas relativas desde la raíz del proyecto.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

VIEWS_DIR = os.path.join(BASE_DIR, "views")
CONTROLLERS_DIR = os.path.join(BASE_DIR, "controllers")
MODELS_DIR = os.path.join(BASE_DIR, "models")
UTILS_DIR = os.path.join(BASE_DIR, "utils")
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
ICON_DIR = os.path.join(RESOURCES_DIR, "icon")
IMG_DIR = os.path.join(RESOURCES_DIR, "img")


SEARCH_ICON_PATH = os.path.join(ICON_DIR, "search_icon.png") 
TRASH_ICON_PATH = os.path.join(ICON_DIR, "trash_icon.png")
PDF_ICON_PATH = os.path.join(ICON_DIR, "pdf.png")

# Ruta absoluta del archivo SQL para inicializar la base de datos.
# Usamos BASE_DIR como punto de partida para facilitar la gestión de rutas si es necesario hacer cambios.
PATH_INICIALIZACION_DB = os.path.join(MODELS_DIR, "inicializacion_db.sql")

# Ruta absoluta del archivo SQL para eliminar o limpiar la base de datos.
# Esta ruta nos permitirá acceder fácilmente al archivo desde cualquier parte del proyecto.
PATH_DELETE_DB = os.path.join(MODELS_DIR, "delete_db.sql")

# Bloque principal de prueba: solo se ejecuta cuando el archivo se ejecuta directamente.
# Este bloque imprimirá las rutas generadas, lo cual es útil para verificar que los paths son correctos.
if __name__ == '__main__':
    print(f"\nBASE_DIR: {BASE_DIR}\n")
    print(f"\nPATH_INICIALIZACION_DB: {PATH_INICIALIZACION_DB}\n")
    print(f"\nPATH_DELETE_DB: {PATH_DELETE_DB}\n")
    print(f"\SEARCH_ICON_PATH: {SEARCH_ICON_PATH}\n")
