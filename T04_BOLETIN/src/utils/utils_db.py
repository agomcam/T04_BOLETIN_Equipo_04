# Archivo: src\utils\utils_db.py

from enum import Enum

# Definimos constantes de configuración de la base de datos.
# Estas constantes nos permiten centralizar y facilitar la gestión de la configuración,
# asegurando que cualquier cambio en los valores de conexión solo requiera modificación en este archivo,
# mejorando así la organización del proyecto.

# DRIVER_DB nos permite especificar el controlador de base de datos que utilizaremos con QSqlDatabase.
# En este caso, "QPSQL" indica el controlador para PostgreSQL.
# Otros valores posibles pueden incluir:
# - "QPSQL": para PostgreSQL.
# - "QMYSQL": para bases de datos MySQL o MariaDB.
# - "QSQLITE": para bases de datos SQLite, que son bases de datos ligeras y embebidas.
# - "QOCI": para bases de datos Oracle.
# - "QODBC": para bases de datos que usan ODBC (Open Database Connectivity).
DRIVER_DB = "QPSQL"

# HOSTNAME_DB define el nombre del host o servidor donde reside la base de datos.
# Si la base de datos se encuentra en otro servidor, podemos usar una dirección IP o un dominio.
HOSTNAME_DB = "localhost"

# NAME_DB establece el nombre de la base de datos a la que queremos conectarnos.
# En este proyecto, hemos elegido "t04_db" para almacenar nuestros datos.
# Si necesitamos conectarnos a otra base de datos, solo es necesario cambiar este valor.
NAME_DB = "t04_db"

# USER_DB define el nombre del usuario que tiene permisos para acceder a la base de datos.
# En este caso, hemos configurado el usuario "admin" con los permisos necesarios.
# Cambiar de usuario es tan sencillo como modificar esta constante.
USER_DB = "admin"

# PASS_DB define la contraseña asociada al usuario de la base de datos.
# Aquí, hemos usado "0000" como la contraseña para el usuario.
# Nota: En entornos de producción, es recomendable almacenar contraseñas en un sistema seguro 
# y no directamente en el código, para mejorar la seguridad de nuestra aplicación.
PASS_DB = "0000"

# PORT_DB define el puerto en el que la base de datos escucha conexiones.
# Podemos ajustar este valor si PostgreSQL está configurado para escuchar en un puerto diferente.
PORT_DB = 60000

# Nombre de la conexión para QSqlDatabase, basado en el nombre de la base de datos.
# Esto ayuda a identificar claramente la conexión en aplicaciones más complejas.
CONNECTION_NAME = NAME_DB

# Definimos un enumerado para los nombres de las tablas de la base de datos.
# Esto centraliza y organiza los nombres de las tablas, reduciendo la posibilidad de errores tipográficos.
class EnumTablasDB(Enum):
    #ROLES = "roles"
    USUARIOS = "usuarios"
    CATEGORIAS = "categorias"
    TAREAS = "tareas"
    #VENTAS = "ventas"

class EnumDataMode(Enum):
    TABLA = "table"
    GRAFICA = "chart"
    
class EnumEjes(Enum):
    EJE_X = "eje_x"
    EJE_Y = "barritas_datos"
