from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import json

# initial db configuration
db = SQLAlchemy()
db_uri = {
    'dialect':'postgresql',
    'user':'orders_service',
    'pass':'welikeorders',
    'host':'orders_db',
    'port':'5432',
    'database':'orders_db'
}

# app configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mesecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = f'{db_uri["dialect"]}://{db_uri["user"]}:{db_uri["pass"]}@{db_uri["host"]}:{db_uri["port"]}/{db_uri["database"]}'

# ---------------------------

# further db configuration 
db = SQLAlchemy(app)

# Model - schema
class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    # save json encoded text
    products = db.Column(db.String(1000))
    sumtotal = db.Column(db.Float)
    # 'Pending', 'Reject', or 'Success'
    status = db.Column(db.String(10))

    # property for converting to json format
    @property
    def serialized(self):
        return {
            'id' : self.id,
            'products' : json.loads(self.products),
            'sumtotal' : self.sumtotal,
            'status' : self.status
        }

class DB_Cursor():
    next_id: int

    def __init__(self):
        self.next_id = 1
    
    def increment(self):
        self.next_id += 1
cursor = DB_Cursor()

with app.app_context():
    # Create products table (if it doesn't exist)
    db.create_all()

# ---------------------------

# PRODUCTS BACKEND ROUTES

# GET methods:

# get all orders (full history)
@app.route('/orders', methods = ['GET'])
def send_all_orders():
    return jsonify([p.serialized for p in Orders.query.all()])

# Other methods:

# request to create new order with given fields
@app.route('/products', methods=['POST'])
def create_product():
    ret = {'success' : False}

    p = request.json
    order_new = Orders(
        id = cursor.next_id,
        products = p['products'],
        sumtotal = float(p['sumtotal']),
        status = 'Pending'
    )
    try:
        db.session.add(order_new)
        db.session.commit()
        cursor.increment()
        ret['success'] = True
    except:
        ret['success'] = False

    return jsonify(ret)

# ---------------------------

# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)