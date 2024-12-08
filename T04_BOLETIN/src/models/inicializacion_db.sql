-- Crear la tabla de Usuarios si no existe
CREATE TABLE IF NOT EXISTS Usuarios (
    email VARCHAR(255) PRIMARY KEY, -- El email será la clave primaria
    nombre_usuario VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Crear la tabla de categoriass
CREATE TABLE IF NOT EXISTS categorias (
    id_categoria SERIAL PRIMARY KEY, -- ID auto incremental
    nombre_categoria VARCHAR(100) NOT NULL
);

-- Insertar categorías predeterminadas
INSERT INTO categorias (nombre_categoria)
VALUES
('Ofimática'),
('Programación'),
('Ocio');

-- Crear la tabla tareas
CREATE TABLE IF NOT EXISTS tareas (
    nombre VARCHAR(255) PRIMARY KEY, -- Nombre de la tareas como clave primaria
    description VARCHAR(255),
    idUsuario VARCHAR(255) NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES Usuarios(email) ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria) ON DELETE CASCADE
);

-- Insertar datos de prueba en la tabla Usuarios
INSERT INTO Usuarios (email, nombre_usuario, password)
VALUES
('antonio@gmail.com', 'antonio', 'usuario0?'),
('david@gmail.com', 'david', 'usuario0?'),
('pedro@gmail.com', 'pedro', 'usuario0?');

-- Insertar tareass para Antonio con la categoría asignada
INSERT INTO tareas (nombre, description, idUsuario, id_categoria) VALUES
('Revisión de documentos', 'Revisar y corregir los documentos enviados por el cliente.', 'antonio@gmail.com', 1), -- Ofimática
('Preparar presentación mensual', 'Crear presentación para la reunión mensual de resultados.', 'antonio@gmail.com', 1), -- Ofimática
('Actualizar base de datos', 'Actualizar la base de datos con los nuevos registros de clientes.', 'antonio@gmail.com', 2), -- Programación
('Reunión con el equipo', 'Coordinar reunión semanal con el equipo de desarrollo.', 'antonio@gmail.com', 1), -- Ofimática
('Enviar reporte de ventas', 'Elaborar y enviar el reporte de ventas mensual al gerente.', 'antonio@gmail.com', 1), -- Ofimática
('Investigación de mercado', 'Analizar las tendencias del mercado para ajustar la estrategia.', 'antonio@gmail.com', 1), -- Ofimática
('Responder correos pendientes', 'Revisar y responder los correos electrónicos recibidos en la semana.', 'antonio@gmail.com', 1); -- Ofimática

-- Insertar tareass para David con la categoría asignada
INSERT INTO tareas (nombre, description, idUsuario, id_categoria) VALUES
('Revisión de inventario', 'Revisar el inventario de productos en el almacén.', 'david@gmail.com', 1), -- Ofimática
('Planificación de producción', 'Planificar las necesidades de producción para el próximo mes.', 'david@gmail.com', 1), -- Ofimática
('Capacitación del personal', 'Organizar una sesión de capacitación para el nuevo equipo.', 'david@gmail.com', 1), -- Ofimática
('Análisis de costos', 'Analizar los costos de producción y buscar áreas de mejora.', 'david@gmail.com', 1), -- Ofimática
('Actualización de precios', 'Actualizar los precios de los productos según los nuevos costos.', 'david@gmail.com', 1), -- Ofimática
('Contacto con proveedores', 'Revisar y confirmar las órdenes de compra con los proveedores.', 'david@gmail.com', 1), -- Ofimática
('Elaboración de informe trimestral', 'Crear un informe con el desempeño del área en el trimestre.', 'david@gmail.com', 1), -- Ofimática
('Supervisión del proceso', 'Supervisar el proceso de ensamblaje en la planta.', 'david@gmail.com', 2); -- Programación

-- Insertar tareass para Pedro con la categoría asignada
INSERT INTO tareas (nombre, description, idUsuario, id_categoria) VALUES
('Diseño de campaña publicitaria', 'Crear el diseño de la nueva campaña de marketing digital.', 'pedro@gmail.com', 3), -- Ocio
('Revisión de redes sociales', 'Analizar el rendimiento de las publicaciones en redes sociales.', 'pedro@gmail.com', 3), -- Ocio
('Creación de contenido', 'Desarrollar contenido para el blog de la empresa.', 'pedro@gmail.com', 3), -- Ocio
('Revisión de SEO', 'Optimizar el SEO del sitio web de la empresa.', 'pedro@gmail.com', 2), -- Programación
('Coordinación con diseñadores', 'Reunirse con el equipo de diseño para revisar avances.', 'pedro@gmail.com', 1), -- Ofimática
('Análisis de métricas', 'Revisar las métricas de tráfico y conversión del sitio web.', 'pedro@gmail.com', 2); -- Programación
