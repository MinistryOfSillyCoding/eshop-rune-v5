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
    # name = db.Column(db.String(255))
    # price = db.Column(db.Float)
    # quantity = db.Column(db.Integer)

    # property for converting to json format
    @property
    def serialized(self):
        return {
            # 'id' : self.id,
            # 'name' : self.name,
            # 'price' : self.price,
            # 'quantity' : self.quantity
            'id' : self.id
        }

with app.app_context():
    # Create products table (if it doesn't exist)
    db.create_all()

# ---------------------------

# PRODUCTS BACKEND ROUTES

# GET methods:

# Other methods:

# ---------------------------

# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)