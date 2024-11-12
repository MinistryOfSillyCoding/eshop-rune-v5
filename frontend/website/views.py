from flask import Blueprint, render_template, request
import requests

views = Blueprint('views',__name__)

# ---------------------------

# FRONTEND ROUTES:

# GET methods:

# get homepage
@views.route('/')
def home():
    return render_template('home.html')

# get catalog page
@views.route('/catalog')
def catalog():
    # here we'll need to make a GET request to the backend
    items = requests.get('http://products:5000/products').json()
    # before serving the html
    return render_template('catalog.html', items=items)

# get myproducts page
@views.route('/myproducts', methods=['GET'])
def myproducts():
    return render_template('myproducts.html')

# get cart page
@views.route('/cart')
def cart():
    return render_template('cart.html')

# get orders page
@views.route('/orders')
def orders():
    return render_template('orders.html')

# Other methods:

# create new product in myproducts page
@views.route('/myproducts', methods=['POST'])
def send_new_product_request():
    name = request.form['fname'] + ' ' + request.form['lname']
    product_json = {
        'name' : name
        }
    try:
        post_success = requests.post('http://products:5000/products', json=product_json).json()['success']
    except:
        post_success = False
    return render_template(
        'myproducts.html',
        product_post_sent=True,
        product_post_success=post_success,
        product_name=name
        )