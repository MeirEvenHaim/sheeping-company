from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mainDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define models for the database
class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f"<Register(id={self.id}, email='{self.email}')>"

    def __str__(self):
        return f"Register: {self.email}"

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200), unique=False, nullable=False)
    ccn = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

    def __str__(self):
        return f"User: {self.username}"

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'address': self.address,
            'ccn': self.ccn
        }

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return f"<Supplier(id={self.id}, name='{self.name}', email='{self.email}')>"

    def __str__(self):
        return f"Supplier: {self.name}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    expire = db.Column(db.String(120), unique=False, nullable=False)
    price = db.Column(db.String(200), unique=False, nullable=False)
    origin = db.Column(db.String(10), unique=False, nullable=False)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price='{self.price}')>"

    def __str__(self):
        return f"Product: {self.name}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'expire': self.expire,
            'price': self.price,
            'origin': self.origin
        }

class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(80), unique=True, nullable=False)
    num_of_employees = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"<Branch(id={self.id}, region='{self.region}')>"

    def __str__(self):
        return f"Branch: {self.region}"

    def to_dict(self):
        return {
            'id': self.id,
            'region': self.region,
            'num_of_employees': self.num_of_employees
        }
        
        
# Create the database and the tables
# NOT GOOD
@app.before_request
def create_tables():
    db.create_all()

# Where you create new something with same ids twice - you have 500 
@app.route('/registers', methods=['POST'])
def create_register():
    data = request.get_json()
    new_register = Register(email=data['email'], password=data['password'])
    db.session.add(new_register)
    db.session.commit()
    return jsonify(new_register.to_dict()), 201

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], address=data['address'], ccn=data['ccn'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/suppliers', methods=['POST'])
def create_supplier():
    data = request.get_json()
    new_supplier = Supplier(name=data['name'], email=data['email'], address=data['address'])
    db.session.add(new_supplier)
    db.session.commit()
    return jsonify(new_supplier.to_dict()), 201

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], expire=data['expire'], price=data['price'], origin=data['origin'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@app.route('/branches', methods=['POST'])
def create_branch():
    data = request.get_json()
    new_branch = Branch(region=data['region'], num_of_employees=data['num_of_employees'])
    db.session.add(new_branch)
    db.session.commit()
    return jsonify(new_branch.to_dict()), 201

@app.route('/registers/<int:id>', methods=['PUT'])
def update_register(id):
    register = Register.query.get_or_404(id)
    data = request.get_json()

    if 'email' in data:
        register.email = data['email']
    if 'password' in data:
        register.password = data['password']

    db.session.commit()
    return jsonify({'message': 'Register updated successfully', 'data': register.to_dict()})

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()

    if 'email' in data:
        user.email = data['email']
        
    if 'ccn' in data:
        user.ccn = data['ccn']
        
    if 'username' in data:
        user.username = data['username']
        
    if 'address' in data:
        user.address = data['address']
        
    db.session.commit()
    return jsonify({'message': 'User updated successfully', 'data': user.to_dict()})

@app.route('/suppliers/<int:id>', methods=['PUT'])
def update_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    data = request.get_json()

    if 'email' in data:
        supplier.email = data['email']
                
    if 'name' in data:
        supplier.name = data['name']
        
    if 'address' in data:
        supplier.address = data['address']
        
    db.session.commit()
    return jsonify({'message': 'Supplier updated successfully', 'data': supplier.to_dict()})

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()

    if 'name' in data:
        product.name = data['name']
        
    if 'expire' in data:
        product.expire = data['expire']
        
    if 'price' in data:
        product.price = data['price']
        
    if 'origin' in data:
        product.origin = data['origin']
        
    db.session.commit()
    return jsonify({'message': 'Product updated successfully', 'data': product.to_dict()})

@app.route('/branches/<int:id>', methods=['PUT'])
def update_branch(id):
    branch = Branch.query.get_or_404(id)
    data = request.get_json()

    if 'num_of_employees' in data:
        branch.num_of_employees = data['num_of_employees']
        
    if 'region' in data:
        branch.region = data['region']
        
    db.session.commit()
    return jsonify({'message': 'Branch updated successfully', 'data': branch.to_dict()})

@app.route('/registers/<int:id>', methods=['DELETE'])
def delete_register(id):
    register = Register.query.get_or_404(id)
    db.session.delete(register)
    db.session.commit()
    return jsonify({'message': 'Register deleted successfully'})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

@app.route('/suppliers/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    db.session.delete(supplier)
    db.session.commit()
    return jsonify({'message': 'Supplier deleted successfully'})

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

@app.route('/branches/<int:id>', methods=['DELETE'])
def delete_branch(id):
    branch = Branch.query.get_or_404(id)
    db.session.delete(branch)
    db.session.commit()
    return jsonify({'message': 'Branch deleted successfully'})

@app.route('/registers', methods=['GET'])
def get_registers():
    registers = Register.query.all()
    return jsonify([register.to_dict() for register in registers])

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([supplier.to_dict() for supplier in suppliers])

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@app.route('/branches', methods=['GET'])
def get_branches():
    branches = Branch.query.all()
    return jsonify([branch.to_dict() for branch in branches])

if __name__ == '__main__':
    app.run(debug=True)
