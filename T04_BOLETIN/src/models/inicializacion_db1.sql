-- #############################################
-- # Archivo: src\models\inicializacion_db.sql #
-- #############################################

-- Crear la tabla 'roles' para definir los permisos de los usuarios
CREATE TABLE IF NOT EXISTS roles (
    id_rol SERIAL PRIMARY KEY,
    nombre_rol VARCHAR(50) UNIQUE NOT NULL
);

-- Insertar datos iniciales en la tabla 'roles'
-- Se utilizan los valores 'admin', 'vendedor' y 'cliente' como roles de ejemplo
INSERT INTO roles (nombre_rol)
VALUES 
    ('admin'),
    ('vendedor'),
    ('cliente')
ON CONFLICT DO NOTHING;

-- Crear la tabla 'usuarios' con referencia a 'roles'
-- Cada usuario está asociado a un rol específico mediante la columna 'id_rol'
CREATE TABLE IF NOT EXISTS usuarios (
    email VARCHAR(255) PRIMARY KEY,
    nombre_usuario VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    id_rol INT REFERENCES roles(id_rol) DEFAULT 3  -- Rol de cliente por defecto
);

-- Insertar datos iniciales en la tabla 'usuarios'
-- Añadimos tres usuarios de ejemplo con diferentes roles
INSERT INTO usuarios (email, nombre_usuario, password, id_rol)
VALUES 
    ('admin@example.com', 'admin', 'adminpass', 1),
    ('vendedor1@example.com', 'vendedor1', 'vendedorpass1', 2),
    ('cliente1@example.com', 'cliente1', 'clientepass1', 3)
ON CONFLICT (email) DO NOTHING;

-- Crear la tabla 'categorias' para clasificar productos, con unicidad en 'nombre_categoria'
-- Se utiliza un índice insensible a mayúsculas para evitar duplicados (ej. 'Periféricos' y 'periféricos' serán tratados como iguales)
CREATE TABLE IF NOT EXISTS categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre_categoria VARCHAR(255) NOT NULL UNIQUE
);

-- Añadir un índice único en 'nombre_categoria' en minúsculas para evitar duplicados insensibles a mayúsculas
CREATE UNIQUE INDEX IF NOT EXISTS idx_nombre_categoria_lower
ON categorias (LOWER(nombre_categoria));

-- Insertar datos de ejemplo en la tabla 'categorias'
-- Se insertan cuatro categorías de productos
INSERT INTO categorias (nombre_categoria)
VALUES 
    ('Periféricos'),
    ('Almacenamiento'),
    ('Computadoras'),
    ('Monitores')
ON CONFLICT (nombre_categoria) DO NOTHING;

-- Crear la tabla 'productos' para almacenar información sobre los productos
-- Cada producto se relaciona con una categoría mediante 'id_categoria'
CREATE TABLE IF NOT EXISTS productos (
    codigo VARCHAR(10) PRIMARY KEY,
    producto VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    ventas INT NOT NULL DEFAULT 0,
    id_categoria INT REFERENCES categorias(id_categoria),
    fecha_agregado DATE DEFAULT CURRENT_DATE
);

-- Insertar datos de ejemplo en la tabla 'productos'
-- Añadimos productos de ejemplo para las categorías de 'Periféricos', 'Almacenamiento', 'Computadoras' y 'Monitores'
INSERT INTO productos (codigo, producto, descripcion, precio, stock, ventas, id_categoria)
VALUES 
    -- Periféricos
    ('001', 'Teclado Mecánico', 'Teclado RGB con switches rojos', 75, 20, 150, 1),
    ('002', 'Ratón Inalámbrico', 'Ratón óptico inalámbrico', 30, 50, 300, 1),
    ('003', 'Auriculares Bluetooth', 'Auriculares inalámbricos con micrófono', 50, 30, 120, 1),
    ('004', 'Altavoces USB', 'Altavoces estéreo para ordenador', 25, 40, 80, 1),
    ('005', 'Cámara Web HD', 'Cámara web de alta definición', 60, 25, 75, 1),
    ('006', 'Teclado Inalámbrico', 'Teclado Bluetooth ultrafino', 40, 15, 50, 1),
    ('007', 'Ratón Gaming', 'Ratón con sensor óptico de alta precisión', 45, 35, 180, 1),
    ('008', 'Micrófono USB', 'Micrófono para streaming y grabación', 90, 20, 60, 1),
    ('009', 'Pad Mouse XL', 'Alfombrilla de ratón extra grande', 15, 60, 200, 1),
    ('010', 'Controlador USB', 'Mando para juegos compatible con PC', 35, 25, 110, 1),
    
    -- Almacenamiento
    ('011', 'Disco Duro Externo', 'HDD 2TB USB 3.0', 60, 40, 100, 2),
    ('012', 'SSD Interno', 'SSD 512GB NVMe', 85, 30, 90, 2),
    ('013', 'Pendrive 64GB', 'Pendrive USB 3.1', 20, 100, 300, 2),
    ('014', 'SSD Externo', 'SSD 1TB portátil', 150, 15, 45, 2),
    ('015', 'Tarjeta MicroSD 128GB', 'Memoria expandible para dispositivos móviles', 25, 80, 140, 2),
    ('016', 'NAS de 4 bahías', 'Sistema de almacenamiento en red', 350, 10, 20, 2),
    ('017', 'Pendrive 128GB', 'Pendrive de alta capacidad', 30, 50, 85, 2),
    ('018', 'HDD Interno', 'Disco duro interno 1TB', 50, 25, 60, 2),
    ('019', 'Carcasa Externa', 'Carcasa para discos duros 2.5"', 20, 40, 70, 2),
    ('020', 'HDD Externo 4TB', 'Disco duro externo de gran capacidad', 110, 20, 45, 2),

    -- Computadoras
    ('021', 'Portátil Gaming', 'Portátil con GPU RTX 3060', 1200, 5, 20, 3),
    ('022', 'Ordenador Sobremesa', 'PC de sobremesa Intel i5', 700, 8, 18, 3),
    ('023', 'MacBook Air', 'Portátil ultraligero de Apple', 1000, 10, 30, 3),
    ('024', 'Chromebook', 'Portátil compacto con Chrome OS', 250, 15, 25, 3),
    ('025', 'Mini PC', 'PC compacto para uso básico', 200, 12, 35, 3),
    ('026', 'All-in-One PC', 'Ordenador todo en uno con pantalla táctil', 850, 7, 12, 3),
    ('027', 'Laptop Convertible', 'Portátil 2 en 1 con pantalla táctil', 600, 10, 22, 3),
    ('028', 'Workstation', 'Estación de trabajo para diseño gráfico', 1500, 3, 10, 3),
    ('029', 'Raspberry Pi', 'Microordenador de bajo consumo', 40, 50, 150, 3),
    ('030', 'Portátil Ultrabook', 'Portátil ultrafino con SSD', 900, 6, 16, 3),
    
    -- Monitores
    ('031', 'Monitor 27"', 'Monitor LED 27 pulgadas 4K', 350, 10, 50, 4),
    ('032', 'Monitor 24"', 'Monitor Full HD 24 pulgadas', 150, 15, 60, 4),
    ('033', 'Monitor Gaming 144Hz', 'Monitor para juegos con alta tasa de refresco', 250, 12, 40, 4),
    ('034', 'Monitor Curvo', 'Monitor curvo de 32 pulgadas', 300, 8, 25, 4),
    ('035', 'Monitor UltraWide', 'Monitor ultra ancho para multitarea', 400, 5, 18, 4)
ON CONFLICT (codigo) DO NOTHING;

-- Crear la tabla 'ventas' para registrar ventas individuales, con relación a 'usuarios' y 'productos'
-- Cada venta registra el producto vendido, el usuario que realiza la compra, y la cantidad
CREATE TABLE IF NOT EXISTS ventas (
    id_venta SERIAL PRIMARY KEY,
    codigo_producto VARCHAR(10) REFERENCES productos(codigo),
    email_usuario VARCHAR(255) REFERENCES usuarios(email),
    cantidad_vendida INT NOT NULL,
    fecha_venta DATE DEFAULT CURRENT_DATE
);

-- Insertar datos de ejemplo en la tabla 'ventas'
-- Añadimos ventas de ejemplo para relacionar productos y usuarios
INSERT INTO ventas (codigo_producto, email_usuario, cantidad_vendida, fecha_venta)
VALUES 
    ('001', 'cliente1@example.com', 2, '2024-11-13'),
    ('003', 'cliente1@example.com', 1, '2024-11-14'),
    ('004', 'vendedor1@example.com', 1, '2024-11-15'),
    ('007', 'cliente1@example.com', 3, '2024-11-15'),
    ('013', 'cliente1@example.com', 4, '2024-11-16'),
    ('027', 'cliente1@example.com', 1, '2024-11-17'),
    ('035', 'cliente1@example.com', 2, '2024-11-18')
ON CONFLICT DO NOTHING;

-- ########################################################################
-- # Consultas de verificación de datos en las tablas                     #
-- ########################################################################

-- Consultar todos los datos de la tabla 'roles'
SELECT * FROM roles;

-- Consultar todos los datos de la tabla 'usuarios'
SELECT * FROM usuarios;

-- Consultar todos los datos de la tabla 'categorias'
SELECT * FROM categorias;

-- Consultar todos los datos de la tabla 'productos'
SELECT * FROM productos;

-- Consultar todos los datos de la tabla 'ventas'
SELECT * FROM ventas;

-- Consultar todos los usuarios y sus roles
-- Esta consulta une las tablas 'usuarios' y 'roles' para mostrar el rol de cada usuario
SELECT u.email, u.nombre_usuario, r.nombre_rol
FROM usuarios u
JOIN roles r ON u.id_rol = r.id_rol;

-- Consultar todas las categorías de productos
SELECT * FROM categorias;

-- Consultar todos los productos con su categoría
-- Esta consulta une las tablas 'productos' y 'categorias' para mostrar la categoría de cada producto
SELECT p.codigo, p.producto, p.descripcion, p.precio, p.stock, p.ventas, c.nombre_categoria
FROM productos p
JOIN categorias c ON p.id_categoria = c.id_categoria;

-- Consultar todas las ventas con detalles de usuario y producto
-- Esta consulta une las tablas 'ventas', 'usuarios', y 'productos' para mostrar quién compró qué producto
SELECT v.id_venta, u.email AS usuario, p.producto, v.cantidad_vendida, v.fecha_venta
FROM ventas v
JOIN usuarios u ON v.email_usuario = u.email
JOIN productos p ON v.codigo_producto = p.codigo;

-- Consultar el stock total de productos
-- Esta consulta muestra el nombre del producto, el stock disponible y el total vendido.
SELECT producto, stock, ventas FROM productos;

-- Fin del archivo 'inicializacion_db.sql'