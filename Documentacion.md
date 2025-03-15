# Proyecto #1 Sistemas de Bases de Datos 1 - Juan José Almengor Tizol

# **Herramientas**

- [Draw.io](http://Draw.io) para el modelo conceptual, data modeler para el modelo logico y fisico
- Usando Datagrip para la base de datos con oracle
- API realizada con flask y python

# **Modelo Conceptual**

![modelo conceptual.png](Imgdocumentacion/modelo_conceptual.png)

# **Modelo Lógico**

![Modelo logico.png](Imgdocumentacion/Modelo_logico.png)

## Detalles del modelo

### Productos

Los productos contienen nombre productos, y solug producto, tambien un producto puede tener varias imagenes.

### Ordenes de compra

Las ordenes de compra contienen Clientes que son los que hacen las compras, y los clientes tienen varias formas de pago, y las formas de pago contienen varios metodos de pago.

### Envios

Los envios contienen varias ordenes entregadas y pueden venir de diferentes compañías, asi mismo los envios tienen varias direcciones para ir.

### Inventario

El inventario puede tener categorias para almacenar productos, y los productos tienen movimientos, y el inventario esta almacenado en diferentes sedes, que las sedes pueden tener varios trabajadores, y que pueden estar en varios departamentos.

# **Modelo Físico**

![modelo fisico.png](Imgdocumentacion/modelo_fisico.png)

# **Normalización tablas**

# ⦿Categorías

| id | name | created_at | updated_at |
| --- | --- | --- | --- |
| 1 | Classic Groceries | 2021-06-15 23:57:05 | 2025-01-24 10:57:39 |
| 2 | Luxury Electronics | 2020-04-21 7:30:50 | 2025-01-10 4:00:21 |
| 3 | Classic Groceries | 2022-07-24 22:55:19 | 2025-01-29 20:55:08 |
| 4 | Fresh Furniture | 2024-07-04 14:51:18 | 2025-01-27 17:02:41 |
| 5 | Organic Electronics | 2022-06-10 20:15:37 | 2025-02-02 0:06:08 |

# **⦿Clientes**

| id | national_document | name | lastname | confirmed_email | created_at | updated_at |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 678733372 | Nicole Wilkins | Brown | True | 53:23.3 | 25:39.1 |
| 2 | 567666164 | Charles Fowler | Ruiz | False | 30:35.4 | 19:28.9 |
| 3 | 257822152 | Bonnie Hopkins | Green | False | 35:14.1 | 37:14.6 |
| 4 | 642608427 | Courtney Salinas DDS | Anderson | True | 43:39.7 | 23:04.2 |

### Informacion de contacto clientes

| location_id | phone | email | active |
| --- | --- | --- | --- |
| 1 | 001-508-529-9226x35951 | davidhurst@example.net | True |
| 2 | (970)667-9652x439 | susancole@example.org | True |
| 3 | (879)819-1291x7812 | dcarter@example.org | True |
| 4 | (630)460-0755x091 | lwhite@example.org | True |

# **⦿Departamentos**

| id | name | created_at | updated_at |
| --- | --- | --- | --- |
| 1 | Harness Ubiquitous Partnerships - Taylor-Bennett | 2022-04-17 12:18:08 | 2025-01-13 18:09:30 |
| 2 | Mesh Extensible Solutions - Wise LLC | 2022-09-13 1:36:04 | 2025-01-21 21:13:40 |
| 3 | Incubate Dynamic Models - Peterson PLC | 2023-06-08 13:54:29 | 2025-01-21 17:10:14 |
| 4 | Harness Collaborative Applications - Schroeder, Lucas and Ware | 2023-07-18 23:45:44 | 2025-01-18 14:09:33 |
| 5 | Seize Enterprise Applications - Reynolds, Reed and Lowery | 2025-01-15 4:00:23 | 2025-01-01 23:12:25 |

# **⦿Direcciones**

| id | client_id | address | created_at | updated_at |
| --- | --- | --- | --- | --- |
| 1 | 467 | USCGC Davis
FPO AA 85087 | 2020-07-14 3:01:47 | 2025-01-06 6:33:55 |
| 2 | 904 | Unit 1018 Box 7098
DPO AP 82292 | 2024-03-15 5:15:10 | 2025-01-27 23:03:58 |
| 3 | 465 | 34375 Stacy Bridge
Port Michele, DC 89640 | 2022-01-23 1:26:54 | 2025-01-22 21:45:04 |
| 4 | 877 | 99506 Irwin Forest Apt. 034
Coleview, NH 31027 | 2021-12-23 11:16:11 | 2025-01-22 9:56:13 |
| 5 | 169 | 18476 Vanessa Underpass
East Sarahton, NM 84927 | 2023-07-27 23:18:49 | 2025-01-18 11:03:05 |

# **⦿Imagenes**

| id | product_id | image | created_at | updated_at |
| --- | --- | --- | --- | --- |
| 1 | 1997 | [https://dummyimage.com/728x232](https://dummyimage.com/728x232) | 2024-12-27 19:03:22 | 2025-01-05 10:36:57 |
| 2 | 4213 | [https://dummyimage.com/572x423](https://dummyimage.com/572x423) | 2022-08-16 15:38:55 | 2025-01-10 14:30:42 |
| 3 | 9482 | [https://dummyimage.com/963x133](https://dummyimage.com/963x133) | 2020-11-27 18:40:49 | 2025-01-05 0:31:52 |
| 4 | 9932 | [https://placekitten.com/629/738](https://placekitten.com/629/738) | 2020-06-13 18:05:26 | 2025-02-01 17:57:50 |
| 5 | 1562 | [https://dummyimage.com/566x820](https://dummyimage.com/566x820) | 2020-02-11 10:34:22 | 2025-01-07 1:37:57 |

# **⦿Inventario**

| id | product_id | location_id | quantity | created_at | updated_at |
| --- | --- | --- | --- | --- | --- |
| 1 | 10322 | 33 | 78152 | 2024-12-27 19:03:22 | 2025-01-05 10:36:57 |
| 2 | 9097 | 29 | 91542 | 2022-08-16 15:38:55 | 2025-01-10 14:30:42 |
| 3 | 2148 | 12 | 3936 | 2020-11-27 18:40:49 | 2025-01-05 0:31:52 |
| 4 | 2965 | 38 | 50672 | 2020-06-13 18:05:26 | 2025-02-01 17:57:50 |
| 5 | 4685 | 7 | 33841 | 2020-02-11 10:34:22 | 2025-01-07 1:37:57 |

# **⦿movimientos_productos**

| id | movement_id | product_id | quantity | created_at | updated_at |
| --- | --- | --- | --- | --- | --- |
| 1 | 10915 | 3401 | 55214 | 2024-05-14 8:28:07 | 2025-01-09 15:36:35 |
| 2 | 5657 | 6935 | 94341 | 2021-03-08 23:47:04 | 2025-01-30 1:25:39 |
| 3 | 22083 | 9432 | 45321 | 2020-11-27 18:40:49 | 2025-01-05 0:31:52 |
| 4 | 35014 | 9711 | 38946 | 2020-06-13 18:05:26 | 2025-02-01 17:57:50 |
| 5 | 52343 | 1295 | 50909 | 2020-02-11 10:34:22 | 2025-01-07 1:37:57 |

# **⦿Movimientos_tabla**

| id | location_origin_id | location_dest_id | status_id | estimate_arrive_date | requested_at | created_at | updated_at |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 33 | 26 | 1 | 2023-10-22 12:20:01.673757 | 2023-03-09 12:04:00.992985 | 2023-05-02 15:38:21.875842 | 2025-01-03 15:16:40.527548 |
| 2 | 34 | 6 | 2 | 2020-01-08 12:40:58.755482 | 2022-03-04 23:55:42.353327 | 2021-10-31 20:42:04.659949 | 2025-01-01 10:06:18.593387 |
| 3 | 37 | 47 | 3 | 2023-03-28 05:32:20.029937 | 2022-08-22 06:12:36.794679 | 2022-08-07 09:44:07.861158 | 2025-01-29 15:18:23.297310 |
| 4 | 12 | 26 | 3 | 2024-07-23 13:28:26.687573 | 2020-05-02 14:02:23.421001 | 2024-12-03 07:33:33.720933 | 2025-01-13 03:29:19.997770 |
| 5 | 22 | 10 | 4 | 2022-10-24 16:29:56.165937 | 2020-08-25 03:04:45.646505 | 2023-06-09 07:46:57.550983 | 2025-02-01 17:38:12.453793 |

**status_name tabla**

| status_id | status_name |
| --- | --- |
| 1 | APPROVED |
| 2 | PENDING |
| 3 | REQUESTED |
| 4 | REJECTED |

# **⦿Ordenes_entregadas**

| id | order_id | status | delivered_at | created_at | updated_at |
| --- | --- | --- | --- | --- | --- |
| 1 | 339512 | DELIVERED | 2023-07-22 8:41:55 | 2020-11-29 21:41:43 | 2025-01-10 23:41:36 |
| 2 | 9691 | DELIVERED | 2024-12-24 22:47:46 | 2025-01-15 19:03:55 | 2025-01-09 16:23:52 |
| 3 | 5093 | FAILED | 2022-02-27 5:17:02 | 2023-11-16 16:34:14 | 2025-02-03 17:49:29 |
| 4 | 5348 | DELIVERED | 2020-11-08 3:43:19 | 2024-03-11 3:36:24 | 2025-01-28 10:16:56 |
| 5 | 1585 | COMMING | 2022-08-22 6:30:34 | 2021-12-28 22:20:40 | 2025-01-26 15:23:01 |

### compañías_ordenes_entregadas

| company | address | number_company_guide |
| --- | --- | --- |
| Griffin, Nelson and Russo | 352 Christine PathKimberlyberg, ME 56294 | 4315 |
| Allison-Davis | 8962 Erica Throughway Suite 741Malloryfort, NH 67976 | 1044 |
| Hicks-Cooper | 9136 Natasha RoadRichardsonfurt, PR 86145 | 3022 |
| Foster and Sons | 40020 Autumn Square Suite 500East Stephenborough, CO 24266 | 3361 |
| Foster and Sons | 709 Maria Alley Apt. 460Aliciaburgh, MP 83487 | 2607 |

# **⦿Ordenes_productos**

| id | order_id | product_id | quantity | price | created_at | updated_at |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 418 | 5572 | 59666 | 778921724 | 2023-06-25 9:24:24 | 2025-01-27 7:22:56 |
| 2 | 8626 | 1066 | 97465 | 155033500 | 2025-02-03 8:27:58 | 2025-01-10 17:03:17 |
| 3 | 9494 | 5397 | 87283 | 630440996 | 2024-10-15 6:52:48 | 2025-01-17 13:10:46 |
| 4 | 2670 | 7337 | 38089 | 13220361 | 2021-09-20 16:50:09 | 2025-01-20 10:10:32 |
| 5 | 5450 | 1604 | 13311 | 267115418 | 2024-07-13 12:03:47 | 2025-01-03 5:08:54 |

# **⦿Ordenes**

| id | client_id | location_id | created_at | updated_at |
| --- | --- | --- | --- | --- |
| 1 | 387 | 23 | 2024-01-31 0:13:11 | 2025-01-19 15:30:53 |
| 2 | 533 | 8 | 2021-11-16 10:21:11 | 2025-02-20 18:12:39 |
| 3 | 832 | 35 | 2020-09-26 12:56:29 | 2025-01-26 19:10:48 |
| 4 | 206 | 5 | 2021-12-19 19:51:11 | 2025-02-14 22:01:09 |
| 5 | 80 | 27 | 2024-07-13 12:03:47 | 2025-01-03 5:08:54 |

# **⦿Pago_ordenes**

| id | order_id | payment_method_id | status_id | created_at | updated_at |
| --- | --- | --- | --- | --- | --- |
| 1 | 2000 | 1 | 1 | 2021-09-11 3:06:42 | 2025-01-09 13:03:33 |
| 2 | 9796 | 1 | 1 | 2020-01-31 12:56:48 | 2025-01-04 16:04:21 |
| 3 | 3746 | 2 | 2 | 2020-10-16 21:23:37 | 2025-01-06 13:47:12 |
| 4 | 5091 | 3 | 2 | 2024-07-30 21:25:42 | 2025-01-15 4:22:03 |
| 5 | 4195 | 2 | 1 | 2021-03-07 4:31:53 | 2025-01-26 4:39:52 |

**Tabla de metodos de pago ordenes**

| payment_method_id | payment_method |
| --- | --- |
| 1 | BANK |
| 2 | CREDIT AMEX |
| 3 | CREDIT VISA |
| 4 | CREDIT MASTERCARD |
| 5 | BITCOIN |

**Tabla de status de pago ordenes**

| status_id | status |
| --- | --- |
| 1 | PAID |
| 2 | PENDING |
| 3 | FAILED |

# **⦿**Datos de pagos

### Tabla de métodos de pago

| id_type_payment | payment metod |
| --- | --- |
| 1 | tarjeta de credito |
| 2 | transferencia bancaria |
| 3 | billetera electrónica |
| 4 | cripto |

### Formas de pago del cliente

| id_cliente | Tipo método de pago |
| --- | --- |
| 1 | 1 |
| 2 | 1 |
| 1 | 2 |
| 1 | 3 |

### Bitácora de pagos

| id | client_id | payment_method | created_at | updated_at |
| --- | --- | --- | --- | --- |
| 1 | 242 | CREDIT VISA | 34:45.5 | 27:16.7 |
| 2 | 209 | CREDIT VISA | 05:11.6 | 02:32.1 |
| 3 | 222 | CREDIT VISA | 10:18.6 | 02:04.4 |
| 4 | 333 | BANK | 38:03.6 | 19:16.5 |
| 5 | 462 | CREDIT VISA | 01:19.5 | 19:03.8 |

# **⦿Producto_devolucion**

| id | product_id | description | status_id | requested_at | created_at | updated_at |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2666 | Fire agree direction like stay until along. Interview value among attack.
Require million because reality minute those method. Staff share bill thousand new and. | 1 | 2022-10-02 4:39:02 | 2020-03-04 20:50:51 | 2025-01-28 10:04:40 |
| 2 | 1491 | After theory Mr strategy ready condition. Federal growth both democratic seek. Interest picture worker wish. | 1 | 2023-01-19 23:19:23 | 2020-06-02 3:56:30 | 2025-02-01 0:17:42 |
| 3 | 4566 | Test money inside up staff. Structure describe raise easy phone stay however.
Assume sense support size general time eight low. Population wear discussion feeling. | 2 | 2024-03-17 16:46:49 | 2020-01-27 6:17:11 | 2025-01-30 4:32:40 |
| 4 | 9268 | East unit general old. Some various happy best ten five. Section state base under single always.
Carry strategy certainly turn purpose. Join summer contain situation safe. | 3 | 2020-01-16 18:01:54 | 2022-01-12 21:57:54 | 2025-01-26 5:14:42 |
| 13 | 6359 | Small impact health most water. Medical true drug blue activity end material. Apply later improve weight piece. | 4 | 2024-03-23 12:44:47 | 2025-01-27 14:08:46 | 2025-01-15 8:18:01 |

**tabla_status_devolucion**

| status_id | status |
| --- | --- |
| 1 | PENDING |
| 2 | REQUESTED |
| 3 | APPROVED |
| 4 | REJECTED |

# **⦿Produtos tabla**

| id | sku | name | description | price | slug | category_id | active | created_at | updated_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SZR-7250 | 234 | Arrive stuff policy close fund write.
Daughter protect thousand.
Arm start time road word any scientist if. But herself capital shoulder beyond. | 837200743 | 23 | 6 | True | 2024-04-05 13:12:04.347584 | 2025-01-05 15:56:08.976367 |
| 2 | WMH-1032 | 33 | Hospital pressure government agreement without. Bill attention should thus recognize away. Real whatever deal pull house race case. | 649398428 | 212 | 23 | False | 2020-02-03 18:11:46.815218 | 2025-01-05 01:37:55.184392 |
| 3 | NEG-1609 | 21 | Current range raise together program send soldier. Resource word four million.
Best moment building hotel quickly task nothing. Major article dream work daughter consider. | 372025130 | 221 | 25 | True | 2024-02-24 21:21:38.710640 | 2025-01-12 16:25:37.130002 |
| 4 | JEF-4952 | 35 | Explain professor amount position anything. Floor do site arrive tax.
Today event week president job build deep.
Trade raise a. Court argue join fall pick start. | 142259806 | 16 | 21 | True | 2024-07-13 12:51:16.419115 | 2025-02-01 17:35:50.148571 |
| 5 | INQ-5517 | 66 | Bag price computer from team local work. Could government realize low because its.
War dream by well. Simple see artist yes recognize edge. See what old fact down learn research career. | 773330935 | 145 | 40 | True | 2020-04-14 05:56:03.310666 | 2025-01-14 13:18:23.719609 |

**Product_name tabla**

| id | product_name |
| --- | --- |
| 1 | Innovative Aluminum Bottle |
| 2 | Premium Wooden Headphones |
| 3 | Durable Aluminum Chair |
| 4 | Durable Glass Backpack |
| 5 | Durable Glass Backpack |

**Slug table**

| id | slug |
| --- | --- |
| 1 | innovative-aluminum-bottle |
| 2 | premium-wooden-headphones |
| 3 | stylish-plastic-phone |
| 4 | durable-glass-backpack |
| 5 | durable-aluminum-chair |

# **⦿sedes**

| id | name | created_at | updated_at |
| --- | --- | --- | --- |
| 1 | West Michaelburgh | 2021-07-20 4:49:49 | 2025-01-05 17:26:13 |
| 2 | Gregoryfort | 2020-01-22 9:55:57 | 2025-01-17 17:59:45 |
| 3 | New Amber | 2021-04-19 20:59:33 | 2025-01-30 10:21:30 |
| 4 | Hugheshaven | 2023-03-06 14:00:12 | 2025-01-09 1:42:40 |
| 5 | East Georgeland | 2022-06-25 13:48:55 | 2025-01-18 22:37:49 |

# **⦿trabajadores**

| id | national_document | name | lastname | job | department_id | active | created_at | updated_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 723369915 | Jessica Lee | Murray | Press photographer | 4 | False | 35:38.3 | 10:14.7 |
| 2 | 240751754 | Peter Owens | Horton | Commercial art gallery manager | 1 | True | 11:19.6 | 27:26.7 |
| 3 | 260048599 | Joseph Evans | Moore | Pharmacist, community | 7 | False | 25:48.3 | 05:46.4 |
| 4 | 173165019 | Carly Williams | Anderson | Horticulturist, commercial | 7 | False | 20:15.7 | 17:37.7 |
| 5 | 843709370 | James Peters | Snyder | Chief Marketing Officer | 9 | False | 37:12.9 | 25:10.6 |

### Información de contacto de los trabajadores

| phone | email | location_id |
| --- | --- | --- |
| 714.503.1184 | guerrakayla@example.net | 48 |
| +1-401-455-5313x16740 | williamsshannon@example.com | 9 |
| +1-685-399-5828x85940 | robertwolfe@example.org | 45 |
| (963)387-1292 | bhernandez@example.net | 32 |
| 001-702-336-6497x000 | zjenkins@example.net | 14 |

## Departamentos

| id | name | created_at | updated_at |
| --- | --- | --- | --- |
| 1 | Ventas | 18:08.5 | 09:30.2 |
| 2 | Auditoria y Contabilidad | 36:04.1 | 13:40.4 |
| 3 | Gerecia de compras | 54:29.0 | 10:14.1 |
| 4 | Gerencia financiera | 45:43.7 | 09:32.8 |
| 5 | Gerencia de logistica | 00:22.7 | 12:24.9 |

| id | name | created_at | updated_at |
| --- | --- | --- | --- |
| 1 | Ventas | 18:08.5 | 09:30.2 |
| 2 | Auditoria y Contabilidad | 36:04.1 | 13:40.4 |
| 3 | Gerecia de compras | 54:29.0 | 10:14.1 |
| 4 | Gerencia financiera | 45:43.7 | 09:32.8 |
| 5 | Gerencia de logistica | 00:22.7 | 12:24.9 |
|  |  |  |  |

# **Implementación**

Para el desarrollo de este proyecto, nos guiaremos por las convenciones de sintaxis SQL definidas por Oracle, asegurando coherencia y alineación con las mejores prácticas establecidas por esta tecnología.

### Tabla categorias

Categorias tienen un id como llave primaria, nombre tipo VARCHAR2, tambien creado y actualizado que ambos son de tipo DATE

```sql
CREATE TABLE categorias (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR2(60) NOT NULL,
    creado DATE NOT NULL,
    actualizado DATE
);

```

### Tabla clientes

clientes tienen un id como llave primaria, id nacional como VARCHAR2, cada cliente tiene nombre y apellido, y la contraseña, creado y actualizado que ambos son de tipo DATE

```sql
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    id_nacional VARCHAR2(10) NOT NULL,
    nombre VARCHAR2(30) NOT NULL,
    apellido VARCHAR2(50) NOT NULL,
    contraseña VARCHAR2(50) NOT NULL,
    creado DATE DEFAULT SYSDATE,
    actualizado DATE
);

```

### Tabla ordenes_de_compra

Las ordenes de compra contienen un id, un cliente id, que va relacionado a cliuentes,  y tambien un Envios_id que va relacionado a los envios, cuando se haga una compra se ve que cliente fue y los datos del envio.

```sql
CREATE TABLE Ordenes_de_compra (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER NULL,
    creado DATE NOT NULL,
    actualizado DATE,
    Envios_id INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (Envios_id) REFERENCES envios(id)
);

```

### Tabla direcciones

las direcciones, tienen un id, un cliente_id, direccion que es cada direccion, creado y actualizado, por ultimo un Envios id que va relacionado a la tabla envios con su id, para cuando se haga un envio, se sepa a que direccion va.

```sql
CREATE TABLE direcciones (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    direccion VARCHAR2(80) NOT NULL,
    creado DATE NOT NULL,
    actualizado DATE,
    Envios_id INTEGER NULL,
    FOREIGN KEY (Envios_id) REFERENCES envios(id)
);

```

### Tabla imagenes

Las imagenes guardan el id, producto_id relacionado a un id de la tabla Producto, ya que es sobre ese producto la imagen.

```sql
CREATE TABLE imagenes (
    id INTEGER PRIMARY KEY,
    producto_id INTEGER NOT NULL,
    imagen VARCHAR2(150) NOT NULL,
    creado DATE NOT NULL,
    actualizado DATE,
    FOREIGN KEY (producto_id) REFERENCES Productos(id)
);

```

### Tabla Envios

los envios tienen un id, fehca del envio, numero de orden, la direccion, el trasporte, y cuando fue creado o actualizado.

```sql
CREATE TABLE envios (
    id INTEGER PRIMARY KEY,
    fecha DATE NOT NULL,
    numero_orden INTEGER NOT NULL,
    direccion INTEGER NOT NULL,
    transporte VARCHAR2(20) NOT NULL,
    creado DATE NOT NULL,
    actualizado DATE
);

```

### Tabla ordenes_producto

las ordenes producto tienen un id, un numero de irden_id, el producto_id que contiene el producto, la cantidad, el precio, creado y acutualizado.

```sql
CREATE TABLE ordenes_producto (
    id INTEGER PRIMARY KEY,
    orden_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio INTEGER NOT NULL,
    creado DATE DEFAULT SYSDATE,
    actualizado DATE
);

```

### Tabla ordenes_entregadas

las ordenes_entregadas tienen un id, un orden_id, que va relacionado a ordenes_de_compra, y tiene Envios_id que va relacionado a la tabla envios con el atributo id.

```sql
CREATE TABLE ordenes_entregadas (
    id INTEGER PRIMARY KEY,
    orden_id INTEGER NOT NULL,
    status VARCHAR2(15) NOT NULL,
    creado DATE NOT NULL,
    actualizado DATE,
    Envios_id INTEGER NOT NULL,
    FOREIGN KEY (orden_id) REFERENCES ordenes_de_compra(id),
    FOREIGN KEY (Envios_id) REFERENCES envios(id)
);

```

```sql
CREATE TABLE compañias_ordenes_entregadas (
    compañia VARCHAR2(80) NOT NULL,
    direccion VARCHAR2(80) NOT NULL,
    numero_guia INTEGER NOT NULL,
    Ordenes_entregadas_id INTEGER NOT NULL,
    PRIMARY KEY (compañia, numero_guia),
    FOREIGN KEY (Ordenes_entregadas_id) REFERENCES ordenes_entregadas(id)
);

```

### Tabla inventario

los inventario tienen un id, un producto_id que esta relacionado a la tabla productos donde se guardan los productos.

```sql
CREATE TABLE inventario (
    id INTEGER PRIMARY KEY,
    producto_id INTEGER NOT NULL,
    localizacion_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    creado DATE NOT NULL,
    actualizado DATE,
    productos_id INTEGER NULL,
    FOREIGN KEY (productos_id) REFERENCES productos(id)
);

```

```sql
CREATE TABLE sedes (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR2(80) NOT NULL,
    creado DATE NOT NULL,
    actualizado DATE,
    inventario_id INTEGER NOT NULL,
    FOREIGN KEY (inventario_id) REFERENCES inventario(id)
);

```

### Tabla productos

los productos estan relacionados con el inventario, cuando con sku_producto, nombre, descripcion, sslug, precio, sinesta activo o no.

```sql
CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    sku_producto VARCHAR2(50) NOT NULL,
    nombre VARCHAR2(50) NOT NULL,
    descripcion VARCHAR2(80),
    precio INTEGER NOT NULL,
    slug INTEGER NOT NULL,
    activo VARCHAR2(20) NOT NULL,
    creado DATE NOT NULL,
    actualizado DATE
);

```

```sql
CREATE TABLE movimiento_productos (
    id INTEGER PRIMARY KEY,
    movimiento_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    creado DATE NOT NULL,
    actualizado DATE,
    inventario_id INTEGER NULL,
    FOREIGN KEY (inventario_id) REFERENCES inventario(id)
);

```

```sql
CREATE TABLE nombre_productos (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR2(50) NOT NULL,
    Productos_id INTEGER NOT NULL,
    FOREIGN KEY (Productos_id) REFERENCES productos(id)
);

```

### Tabla estado_movimientos

estado_movimientos gaurdamos cuando un movimiento fue exitoso o esta pendiente o paso algo, etnonces la relacionamos con los movimientos.

```sql
CREATE TABLE estado_movimientos (
    id INTEGER PRIMARY KEY,
    nombre_estado VARCHAR2(50) NOT NULL
);

```

```sql
CREATE TABLE movimientos (
    id INTEGER PRIMARY KEY,
    id_origen INTEGER NOT NULL,
    id_destino INTEGER NOT NULL,
    id_estado INTEGER NOT NULL,
    fecha_estimada_llegada DATE,
    fecha_solicitud DATE NOT NULL,
    creado DATE DEFAULT SYSDATE,
    actualizado DATE,
    FOREIGN KEY (id_estado) REFERENCES estado_movimientos(id)
);

```

### Tabla pagos_ordenes

pagos_ordenes esta relacionado a ordenes_de_compra, porque se genera una orden cuando se va a pagar, tambien esta relacionado a pagos, para ver el tipo de pago y la informacion, y a estados_pago, para saber si se logro completar o no.

```sql
CREATE TABLE pagos_ordenes (
    id INTEGER PRIMARY KEY,
    orden_id INTEGER NOT NULL,
    pago_id INTEGER NOT NULL,
    estado_pago_id INTEGER NOT NULL,
    creado_en DATE DEFAULT SYSDATE,
    actualizado_en DATE,
    FOREIGN KEY (orden_id) REFERENCES pagos_ordenes (id),
    FOREIGN KEY (pago_id) REFERENCES pagos(id),
    FOREIGN KEY (estado_pago_id) REFERENCES estados_pagos(id)
);

```

```sql
CREATE TABLE pagos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    metodo_pago_id INTEGER NOT NULL,
    creado_en DATE DEFAULT SYSDATE,
    actualizado_en DATE,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (metodo_pago_id) REFERENCES tipos_pago(id)
);

```

### Tabla tipos_pago

tipos_pago almacena los diferentes pagos como tarjeta, efectivo, bitcoin, etc.

```sql
CREATE TABLE tipos_pago (
    id INTEGER PRIMARY KEY,
    metodo_pago VARCHAR2(80) NOT NULL
);

```

```sql
CREATE TABLE estados_pagos (
    id INTEGER PRIMARY KEY,
    estado VARCHAR2(50) NOT NULL
);

```

### Tabla formas_pago

formas_pago pueden ser varias, por eso se relacionan con un cliente, y con tipos_pago, ya que cada cliente puede tener el propio.

```sql
CREATE TABLE formas_pago (
    clientes_id INTEGER,
    tipo_metodo_pago INTEGER,
    PRIMARY KEY (clientes_id, tipo_metodo_pago),
    FOREIGN KEY (clientes_id) REFERENCES clientes(id),
    FOREIGN KEY (tipo_metodo_pago) REFERENCES tipos_pago(id)
);

```

```sql
CREATE TABLE departamentos (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR2(50) NOT NULL,
    creado DATE NOT NULL,
    actualizado DATE
);

```

```sql
CREATE TABLE departamentos_empresa (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR2(100) NOT NULL
);

```

```sql
CREATE TABLE cargos (
    id INTEGER PRIMARY KEY,
    nombre_cargo VARCHAR2(100) NOT NULL
);

```

### Tabla trabajadores

los trabajadores tienen un id, id_departamento que identifica en que departamento esta trabajando, su nombre y apellido.

```sql
CREATE TABLE trabajadores (
    id INTEGER PRIMARY KEY,
    id_departamento INTEGER,
    id_nacional VARCHAR2(10) NOT NULL,
    nombre VARCHAR2(50) NOT NULL,
    apellido VARCHAR2(50) NOT NULL,
    trabajo VARCHAR2(50)
);

```

```sql
CREATE TABLE estados_devoluciones (
    id INTEGER PRIMARY KEY,
    estado VARCHAR2(50) NOT NULL
);

```

### Tabla producto_devoluciones

los producto_devoluciones es cuando un producto se va a devolver, entonces esta relacionado con los producto con su producto_id, y relacionado al estados_devoluciones para saber si fue exitoso o que paso.

```sql
CREATE TABLE producto_devoluciones (
    id INTEGER PRIMARY KEY,
    producto_id INTEGER NOT NULL,
    descripcion VARCHAR2(255) NOT NULL,
    estado_id INTEGER NOT NULL,
    fecha_solicitud DATE NOT NULL,
    creado_en DATE DEFAULT SYSDATE,
    actualizado_en DATE,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (estado_id) REFERENCES estados_devoluciones(id)
);
```

# API

Utilizamos un entorno virtual y tenemos que exportar todas las librerias

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import oracledb
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
# Inicializar Flask source .venv/bin/activate

app = Flask(__name__)
CORS(app)

```

tenemos que tener python en el entorno virtual

```python
python3 --version
pip install flask

```

Es importante saber que tenemos que tener en docker la base de datos, en este caso utilizamos la de oracle

Buscar la imagen oficial de Oracle en Docker Hub

```bash
docker search oracle/database
```

Descargar la imagen de Oracle

```bash
docker pull gvenzl/oracle-xe
```

Crear y ejecutar un contenedor de Oracle

```bash
docker run -d --name oracle-xe -p 1521:1521 -p 5500:5500 -e ORACLE_PASSWORD=your_password gvenzl/oracle-xe
```

En la API colocamos la configuración

```python
# Configuración de la base de datos Oracle XE en Docker
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+oracledb://SYSTEM:99437@localhost:1521/?service_name=XE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

```

Declaramos los diferentes tipos de clases igual que en nuestra base de datos

```python
class TipoPago(db.Model):
    __tablename__ = 'tipos_pago'
    id = db.Column(db.Integer, primary_key=True)
    metodo_pago = db.Column(db.String(80), nullable=False)

class FormaPago(db.Model):
    __tablename__ = 'formas_pago'
    clientes_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), primary_key=True)
    tipo_metodo_pago = db.Column(db.Integer, db.ForeignKey('tipos_pago.id'), primary_key=True)

class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    id_nacional = db.Column(db.String(10), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)  
    creado = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    actualizado = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    
class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    sku_producto = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(100), nullable=False)
    id_categoria = db.Column(db.Integer, nullable=False)
    activo = db.Column(db.Integer, nullable=False)  
    creado = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    actualizado = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "sku_producto": self.sku_producto,
            "nombre": self.nombre,
            "slug": self.slug,
            "activo": "TRUE" if self.activo == 1 else "FALSE"
        }
    
```

# Script de las consultas

```python
@app.route('/api/clientes/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    info_cliente = InformacionCliente.query.filter_by(cliente_id=cliente_id).first()

    if not cliente:
        return jsonify({'message': 'Cliente no encontrado'}), 404

    cliente_data = {
        'id': cliente.id,
        'id_nacional': cliente.id_nacional,
        'nombre': cliente.nombre,
        'apellido': cliente.apellido,
        'telefono': info_cliente.telefono if info_cliente else None,
        'email': info_cliente.email if info_cliente else None,
        'activo': info_cliente.activo if info_cliente else None,
        'email_confirmado': info_cliente.email_confirmado if info_cliente else None,
        'creado': cliente.creado.strftime('%Y-%m-%d %H:%M:%S'),
        'actualizado': cliente.actualizado.strftime('%Y-%m-%d %H:%M:%S') if cliente.actualizado else None
    }

    return jsonify(cliente_data), 200

@app.route('/api/clientes/<int:cliente_id>', methods=['PUT'])
def update_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    info_cliente = InformacionCliente.query.filter_by(cliente_id=cliente_id).first()
    
    if not cliente:
        return jsonify({'message': 'Cliente no encontrado'}), 404

    data = request.get_json()

    cliente.nombre = data.get('nombre', cliente.nombre)
    cliente.apellido = data.get('apellido', cliente.apellido)
    
    if 'password' in data:
        cliente.password = generate_password_hash(data['password'])
    
    if info_cliente:
        info_cliente.telefono = data.get('telefono', info_cliente.telefono)
        info_cliente.email = data.get('email', info_cliente.email)
        info_cliente.activo = data.get('activo', info_cliente.activo)
        info_cliente.email_confirmado = data.get('email_confirmado', info_cliente.email_confirmado)

    db.session.commit()
    
    return jsonify({'status': 'success', 'message': 'Cliente actualizado correctamente'}), 200

@app.route('/api/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    # Buscar al cliente
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({'status': 'error', 'message': 'Cliente no encontrado'}), 404

    # Eliminar primero los datos en informacion_clientes
    InformacionCliente.query.filter_by(cliente_id=id).delete()

    db.session.delete(cliente)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Cliente eliminado correctamente'}), 200

# *****************Endpoints de Productos************
@app.route('/api/productos', methods=['POST'])
def create_producto():
    data = request.get_json()

    # Verificar los datos obligatorios 
    required_fields = ["id", "sku_producto", "nombre", "descripcion", "precio", "slug", "id_categoria", "activo"]
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Datos incompletos'}), 400

    # Crear producto
    new_producto = Producto(
        id=data["id"],
        sku_producto=data["sku_producto"],
        nombre=data["nombre"],
        descripcion=data["descripcion"],
        precio=data["precio"],
        slug=data["slug"],
        id_categoria=data["id_categoria"],
        activo=int(data["activo"]),
        creado=datetime.datetime.utcnow(),
        actualizado=datetime.datetime.utcnow()
    )

    db.session.add(new_producto)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Producto creado correctamente'}), 201

@app.route('/api/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    productos_data = [producto.to_dict() for producto in productos]
    return jsonify({"productos": productos_data}), 200

#unico producto
@app.route('/api/productos/<int:id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({'status': 'error', 'message': 'Producto no encontrado'}), 404

    return jsonify(producto.to_dict()), 200

@app.route('/api/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({'status': 'error', 'message': 'Producto no encontrado'}), 404

    data = request.get_json()

    if "sku_producto" in data:
        producto.sku_producto = data["sku_producto"]
    if "nombre" in data:
        producto.nombre = data["nombre"]
    if "descripcion" in data:
        producto.descripcion = data["descripcion"]
    if "precio" in data:
        producto.precio = data["precio"]
    if "slug" in data:
        producto.slug = data["slug"]
    if "id_categoria" in data:
        producto.id_categoria = data["id_categoria"]
    if "activo" in data:
        producto.activo = int(data["activo"])
    
    producto.actualizado = datetime.datetime.utcnow()

    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Producto actualizado correctamente'}), 200

@app.route('/api/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({'status': 'error', 'message': 'Producto no encontrado'}), 404

    # Eliminar registros relacionados 
    Imagen.query.filter_by(producto_id=id).delete()
    Inventario.query.filter_by(producto_id=id).delete()
    NombreProducto.query.filter_by(productos_id=id).delete()

    db.session.delete(producto)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Producto eliminado correctamente'}), 200

# *****************Endpoints de ordenes************
@app.route('/api/ordenes', methods=['POST'])
def create_orden():
    data = request.get_json()
    if not data or 'cliente_id' not in data:
        return jsonify({'message': 'Datos incompletos'}), 400
    
    new_orden = OrdenCompra(cliente_id=data['cliente_id'])
    db.session.add(new_orden)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Orden de compra creada correctamente'}), 201

@app.route('/api/ordenes/<int:id>', methods=['GET'])
def get_orden(id):
    orden = OrdenCompra.query.get(id)
    if not orden:
        return jsonify({'message': 'Orden no encontrada'}), 404
    
    return jsonify({'id': orden.id, 'cliente_id': orden.cliente_id, 'creado': orden.creado})

# *****************Endpoints de pago************
@app.route('/api/formas_pago', methods=['POST'])
def create_forma_pago():
    data = request.get_json()
    if not data or 'clientes_id' not in data or 'tipo_metodo_pago' not in data:
        return jsonify({'message': 'Datos incompletos'}), 400
    
    new_forma_pago = FormaPago(clientes_id=data['clientes_id'], tipo_metodo_pago=data['tipo_metodo_pago'])
    db.session.add(new_forma_pago)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Forma de pago registrada correctamente'}), 201

```

# Endpoints

Estos fueron probados con thunderbolt.

### Clientes

“POST”

{
"id": 150,
"id_nacional": "62050516",
"nombre": "Juan",
"apellido": "Almengor",
"telefono": "555-9321",
"email": "[juanjo@example.com](mailto:juanjo@example.com)",
"password": "passwordxd"
}

De esta manera podemos crear un cliente en nuestra base de datos.

URL: [http://127.0.0.1:5000/api/cliente](http://127.0.0.1:5000/api/clientes/150)

“GET” 

URL: [http://127.0.0.1:5000/api/clientes/150](http://127.0.0.1:5000/api/clientes/150)

De esta manera podemos obtener la informacion de algun cliente que necesitemos, solo colocamos el id en la url, no es necesario mandar nada

“PUT”

Para actualizar la informacion de un cliente, usamos este metodo y la misma URL, solo mandamos el ID

“DELETE” 

Para delete no mandamos nada, solo con el ID en la URL ya eliminamos a un cliente.

### Productos

“POST

{
"id": 152,
"sku_producto": "ABC123",
"nombre": "Producto de prueba",
"descripcion": "Este es un producto de prueba",
"precio": 100,
"slug": "producto-de-prueba",
"id_categoria": 5,
"activo": 1,
"creado": "2025-03-15 02:40:21",
"actualizado": "2025-03-15 02:40:21"
}

De esta manera mandamos un producto a nuestra base de datos

“GET”

[http://127.0.0.1:5000/api/productos/152](http://127.0.0.1:5000/api/productos/152)

SI queremos obtener un producto, solo colocamos la url y el id del producto que queramos. 

Si solo colocamos esta url nos mandara la lista de todos los productos

[http://127.0.0.1:5000/api/productos](http://127.0.0.1:5000/api/productos)

“PUT”

[http://127.0.0.1:5000/api/productos/101](http://127.0.0.1:5000/api/productos/101)

“DELETE”

Con la URL mandamos el id y lo eliminamos

[http://127.0.0.1:5000/api/productos/101](http://127.0.0.1:5000/api/productos/101)

### Gestion de Ordenes

“POST”

{
"id": 10,
"cliente_id": 150,
"envios_id": 5,
"creado": "2025-03-15 03:50:00",
"actualizado": "2025-03-15 03:50:00"
}

 [http://127.0.0.1:5000/api/ordenes_compra](http://127.0.0.1:5000/api/ordenes_compra)

De esta manera mandamos una gestion a nuestra base de datos

“GET”

[http://127.0.0.1:5000/api/productos/152](http://127.0.0.1:5000/api/productos/152)

SI queremos obtener un producto, solo colocamos la url y el id del gestion que queramos. 

Si solo colocamos esta url nos mandara la lista de todas las gestiones

 [http://127.0.0.1:5000/api/ordenes_compra](http://127.0.0.1:5000/api/ordenes_compra)

“PUT”

 [http://127.0.0.1:5000/api/ordenes_compra/10](http://127.0.0.1:5000/api/ordenes_compra/10)

{
"cliente_id": 155,
"envios_id": 7,
"actualizado": "2025-03-16 10:00:00"
}

“DELETE”

Con la URL mandamos el id y lo eliminamos

 [http://127.0.0.1:5000/api/ordenes_compra/10](http://127.0.0.1:5000/api/ordenes_compra/10)

### Pagos

“POST”

{
"id": 101,
"cliente_id": 4,
"metodo_pago_id": 3
}

URL: [http://127.0.0.1:5000/api/pagos](http://127.0.0.1:5000/api/pagos)

Agregamos un pago con un id

“GET”

URL: [http://127.0.0.1:5000/api/pagos](http://127.0.0.1:5000/api/pagos)

Obtenemos todos los Pagos