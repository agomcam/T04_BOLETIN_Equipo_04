-- #####################################
-- # Archivo: src\models\delete_db.sql #
-- #####################################

-- ########################################################################
-- # NOTA: Las siguientes instrucciones eliminan todas las tablas y datos #
-- # de la base de datos.                                                 #
-- ########################################################################

-- Eliminamos la tabla 'ventas' que contiene los registros de ventas
DROP TABLE IF EXISTS ventas;

-- Eliminamos la tabla 'productos' que contiene todos los productos
DROP TABLE IF EXISTS productos;

-- Eliminamos la tabla 'categorias' que clasifica los productos
DROP TABLE IF EXISTS categorias;

-- Eliminamos la tabla 'usuarios' que almacena los datos de los usuarios de la aplicación
DROP TABLE IF EXISTS usuarios;

-- Eliminamos la tabla 'roles' que define los diferentes roles o permisos
DROP TABLE IF EXISTS roles;

-- Fin del archivo 'delete_db.sql'