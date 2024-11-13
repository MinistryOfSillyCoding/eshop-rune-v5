from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# initial db configuration
db = SQLAlchemy()
db_uri = {
    'dialect':'postgresql',
    'user':'products_service',
    'pass':'welikeproducts',
    'host':'products_db',
    'port':'5432',
    'database':'products_db'
}

# app configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mesecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = f'{db_uri["dialect"]}://{db_uri["user"]}:{db_uri["pass"]}@{db_uri["host"]}:{db_uri["port"]}/{db_uri["database"]}'

# ---------------------------

# further db configuration 
db = SQLAlchemy(app)

# Model - schema
class Products(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    # TODO: img
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    # property for converting to json format
    @property
    def serialized(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'price' : self.price,
            'quantity' : self.quantity
        }

class DB_Cursor():
    next_id: int

    def __init__(self):
        next_id = 1
    
    def increment(self):
        self.next_id += 1
cursor = DB_Cursor()

with app.app_context():
    # Create products table (if it doesn't exist)
    db.create_all()
    # get first available id, to enter manually
    cursor.next_id = Products.query.count() + 1
    # Create initial catalog (if no items exist)
    # We input id numbers to the products even though it's not necessary
    # This is so that it causes an error if the db already has products in it
    if cursor.next_id == 1:
        products = [
            Products(
                id=1,
                name='Colleslawe Andromedas',
                price=34.99,
                quantity=5),
            Products(
                id=2,
                name='Barnacklus Riffraff',
                price=37.99,
                quantity=3),
            Products(
                id=3,
                name='Margot Robbie',
                price=74.99,
                quantity=72),
            Products(
                id=4,
                name='Achilles of the Myrmidons',
                price=39.99,
                quantity=3),
            Products(
                id=5,
                name='John Gin',
                price=999.99,
                quantity=1)
        ]
        try:
            for p in products:
                db.session.add(p)
            db.session.commit()
            cursor.next_id += len(products)
        except:
            print('oh no!')

# ---------------------------

# Cache configuration

# temporary item list before making request to database
'''
items = []
items.append({'name' : 'Achies', 'price' : '$39.99'})
items.append({'name' : 'Margie', 'price' : '$19.99'})
items.append({'name' : 'Johnny-o', 'price' : '$99999.99'})
'''
# TODO: cache items here, for reduced traffic (say, requests with less than x secs in-between)

# ---------------------------

# PRODUCTS BACKEND ROUTES

# GET methods:

# request all products
@app.route('/products/all', methods = ['GET'])
def send_all_products():
    return jsonify([p.serialized for p in Products.query.all()])

# request of a specific product by id and name
@app.route('/products/__<id>__<name>', methods=['GET'])
def send_product_by_id_name(id, name):
    if id == '0':
        q = Products.query.filter(Products.name == name).all()
    elif name == '0':
        q = Products.query.filter(Products.id == int(id)).all()
    else:
        q = Products.query.filter(Products.id == int(id), Products.id == int(id)).all()
    return jsonify([p.serialized for p in q])

# request products from a list of ids
@app.route('/products/list', methods = ['GET'])
def send_products_by_id_list():

    ids = [int(id) for id in request.json]
    products = Products.query.filter(Products.id.in_(ids)).all()
    return jsonify([p.serialized for p in products]) if products else jsonify({})
    

    


# Other methods:

# request to create new product with given fields
@app.route('/products', methods=['POST'])
def create_product():
    ret = {'success' : False}

    p = request.json
    product_new = Products(
        id = cursor.next_id,
        name = p['name'],
        price = float(p['price']),
        quantity = int(p['quantity'])
    )
    try:
        db.session.add(product_new)
        db.session.commit()
        cursor.increment()
        ret['success'] = True
    except:
        ret['success'] = False

    return jsonify(ret)

# request to update a product by id
@app.route('/products', methods=['PUT'])
def update_product():
    ret = {'success' : False}
    p = request.json
    try:
        Products.query.filter(Products.id == p['id']).update({Products.price: p['new_price'], Products.quantity: p['new_quantity']})
        db.session.commit()
        ret['success'] = True
    except:
        ret['success'] = False

    return jsonify(ret)

# request to delete a product by id
@app.route('/products/<deletion_id>', methods=['DELETE'])
def delete_product(deletion_id):
    ret = {'success' : False}

    try:
        Products.query.filter(Products.id == int(deletion_id)).delete()
        db.session.commit()
        ret['success'] = True
    except:
        ret['success'] = False

    return jsonify(ret)


# ---------------------------

# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)