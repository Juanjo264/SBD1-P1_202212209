

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import oracledb
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
# Inicializar Flask source .venv/bin/activate

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos Oracle XE en Docker
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+oracledb://SYSTEM:99437@localhost:1521/?service_name=XE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Envios(db.Model):
    __tablename__ = 'envios'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    numero_orden = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.Integer, nullable=False)
    transporte = db.Column(db.String(20), nullable=False)
    creado = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    actualizado = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

class OrdenCompra(db.Model):
    __tablename__ = 'ordenes_de_compra'
    __table_args__ = {'extend_existing': True}  

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=True)
    envios_id = db.Column(db.Integer, db.ForeignKey('envios.id'), nullable=False)
    creado = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    actualizado = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

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

class InformacionCliente(db.Model):
    __tablename__ = 'informacion_clientes'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True)
    email_confirmado = db.Column(db.Boolean, default=False)

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
    
class Imagen(db.Model):
    __tablename__ = 'imagenes'

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    imagen = db.Column(db.String(150), nullable=False)
    creado = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    actualizado = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

class Inventario(db.Model):
    __tablename__ = 'inventario'

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    localizacion_id = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    creado = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    actualizado = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

class NombreProducto(db.Model):
    __tablename__ = 'nombre_productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    productos_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)

class Pago(db.Model):
    __tablename__ = 'pagos'
    
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    metodo_pago_id = db.Column(db.Integer, db.ForeignKey('tipos_pago.id'), nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    actualizado_en = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    cliente = db.relationship('Cliente', backref=db.backref('pagos', lazy=True))
    metodo_pago = db.relationship('TipoPago', backref=db.backref('pagos', lazy=True))


 
with app.app_context():
    db.create_all()

# *****************Endpoints de Clientes************
@app.route('/api/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()

    required_fields = ['id', 'id_nacional', 'nombre', 'apellido', 'telefono', 'email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Datos incompletos'}), 400

    # Verificar si el ID Nacional o el Email ya existen
    if Cliente.query.filter_by(id_nacional=data['id_nacional']).first():
        return jsonify({'message': 'El ID Nacional ya está registrado'}), 409
    if InformacionCliente.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'El Email ya está registrado'}), 409
    
    hashed_password = generate_password_hash(data['password'])

    # Crear Cliente
    new_cliente = Cliente(
        id=data['id'],  
        id_nacional=data['id_nacional'],
        nombre=data['nombre'],
        apellido=data['apellido'],
        password=hashed_password
    )

    db.session.add(new_cliente)
    db.session.commit()

    new_info = InformacionCliente(
        id=data['id'],
        cliente_id=new_cliente.id,
        telefono=data['telefono'],
        email=data['email']
    )

    db.session.add(new_info)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Cliente creado correctamente'}), 201


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

    if not data.get("id") or not data.get("envios_id"):
        return jsonify({'message': 'Datos incompletos'}), 400

    nueva_orden = OrdenCompra(
        id=data['id'],
        cliente_id=data.get('cliente_id'),  
        envios_id=data['envios_id']
    )

    db.session.add(nueva_orden)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Orden de compra creada correctamente'}), 201

@app.route('/api/ordenes/<int:id>', methods=['GET'])
def get_orden(id):
    orden = OrdenCompra.query.get(id)

    if not orden:
        return jsonify({'status': 'error', 'message': 'Orden no encontrada'}), 404

    return jsonify({
        'id': orden.id,
        'cliente_id': orden.cliente_id,
        'envios_id': orden.envios_id,
        'creado': orden.creado,
        'actualizado': orden.actualizado
    }), 200

@app.route('/api/ordenes', methods=['GET'])
def get_ordenes():
    ordenes = OrdenCompra.query.all()
    
    return jsonify({
        'ordenes': [
            {
                'id': orden.id,
                'cliente_id': orden.cliente_id,
                'envios_id': orden.envios_id,
                'creado': orden.creado,
                'actualizado': orden.actualizado
            } for orden in ordenes
        ]
    }), 200

@app.route('/api/ordenes/<int:id>', methods=['PUT'])
def update_orden(id):
    orden = OrdenCompra.query.get(id)

    if not orden:
        return jsonify({'status': 'error', 'message': 'Orden no encontrada'}), 404

    data = request.get_json()

    if 'cliente_id' in data:
        orden.cliente_id = data['cliente_id']
    if 'envios_id' in data:
        orden.envios_id = data['envios_id']

    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Orden de compra actualizada correctamente'}), 200

# *****************Endpoints de pago************
@app.route('/api/pagos', methods=['POST'])
def create_pago():
    data = request.get_json()

    required_fields = ['id', 'cliente_id', 'metodo_pago_id']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Datos incompletos'}), 400

    # Verificar  cliente existe
    cliente = Cliente.query.get(data['cliente_id'])
    if not cliente:
        return jsonify({'message': 'Cliente no encontrado'}), 404

    metodo_pago = TipoPago.query.get(data['metodo_pago_id'])
    if not metodo_pago:
        return jsonify({'message': 'Método de pago no válido'}), 404

    new_pago = Pago(
        id=data['id'],
        cliente_id=data['cliente_id'],
        metodo_pago_id=data['metodo_pago_id']
    )

    db.session.add(new_pago)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Pago registrado correctamente'}), 201

@app.route('/api/pagos', methods=['GET'])
def get_pagos():
    pagos = Pago.query.all()
    result = [
        {
            'id': pago.id,
            'cliente_id': pago.cliente_id,
            'metodo_pago_id': pago.metodo_pago_id,
            'creado_en': pago.creado_en.strftime('%Y-%m-%d %H:%M:%S'),
            'actualizado_en': pago.actualizado_en.strftime('%Y-%m-%d %H:%M:%S') if pago.actualizado_en else None
        }
        for pago in pagos
    ]
    return jsonify(result)


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=5000)
