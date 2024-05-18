Crear la tabla para ORDENES con Mysql, el servicio de Inventarios genera las tablas de la BD automaticamente

CREATE TABLE ordenes_productos ( orden_id int(11) DEFAULT NULL, producto_id int(11) DEFAULT NULL, precio decimal(10,2) DEFAULT NULL, cantidad int(11) DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE ordenes ( Id int(11) NOT NULL, total decimal(10,2) DEFAULT NULL, date date DEFAULT NULL, status enum('Pagado','Creado','Enviado') DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
