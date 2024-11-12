from flask import Blueprint, render_template, request
import requests

class ProductsAPIConfig():
    protocol: str
    address: str
    port: int
    
    def __init__(self):
        self.protocol = 'http'
        self.address = 'products'
        self.port = 5000
    
    def getURL(self, route: str):
        return self.protocol+'://'+self.address+':'+str(self.port)+route
products_conf = ProductsAPIConfig()

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
    # GET catalog from products service
    items = requests.get(products_conf.getURL('/products')).json()
    
    return render_template('catalog.html', items=items)

# get myproducts page
@views.route('/myproducts', methods=['GET'])
def myproducts():
    return render_template(
        'myproducts.html',
        request_type='none'
    )

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
@views.route('/myproducts/create', methods=['POST'])
def send_new_product_request():
    name = request.form['fname'] + ' ' + request.form['lname']
    product_json = {
        'name' : name,
        'price' : request.form['price'],
        'quantity' : request.form['quantity']
        }
    try:
        success = requests.post(products_conf.getURL('/products'), json=product_json).json()['success']
    except:
        success = False
    return render_template(
        'myproducts.html',
        request_type='new',
        request_success=success,
        product_name=name
        )

# update a product price/quantity by id
@views.route('/myproducts/update', methods=['POST'])
def update_product_by_id():
    update_id = request.form['updateid']
    product_json = {
        'id' : update_id,
        'new_price' : request.form['newprice'],
        'new_quantity' : request.form['newquantity']
    }
    try:
        success = requests.put(products_conf.getURL('/products'), json=product_json).json()['success']
    except:
        success = False
    return render_template(
        'myproducts.html',
        request_type='update',
        request_success=success,
        update_id=update_id
    )


# delete a product in myproducts page
@views.route('/myproducts/delete', methods=['POST'])
def delete_product_by_id():
    deletion_id = request.form['deletionid']
    try:
        success = requests.delete(products_conf.getURL('/products/'+deletion_id)).json()['success']
    except:
        success = False
    return render_template(
        'myproducts.html',
        request_type='delete',
        request_success=success,
        deletion_id=deletion_id
    )
    