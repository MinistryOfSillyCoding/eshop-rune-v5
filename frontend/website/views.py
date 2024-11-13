from flask import Blueprint, render_template, request, make_response
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
@views.route('/products')
def catalog():
    # GET catalog from products service
    products = requests.get(products_conf.getURL('/products/all')).json()
    
    return render_template('catalog.html', products=products)


# search by product id and name in catalog page
@views.route('/products/search')
def search_catalog():
    id = request.args['id']
    name = request.args['name']

    id = '0' if id == '' else id
    name = '0' if name == '' else name
    
    products = requests.get(products_conf.getURL('/products/__'+id+'__'+name)).json()

    return render_template('catalog.html', products=products)

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
    text = request.cookies.get('in_cart')
    cart_list = text.split('_') if text else []
    cart_products = {}
    cart_ids = []
    for q in cart_list:
        info = q.split(':')
        cart_products[info[0]] = info[1]
        cart_ids.append(info[0])
    try:
        products = requests.get(products_conf.getURL('/products/list'), json=cart_ids).json()
    except:
        products = []
        print('oh noes')
    return render_template('cart.html', products=products, cart_products=cart_products)

# get orders page
@views.route('/orders')
def orders():
    return render_template('orders.html')

# Other methods:

# add product to cart
@views.route('/updatecart/<id>', methods=['POST'])
def add_to_cart(id):
    amount_to_add = request.form['amount']
    products_in_cart = request.cookies.get('in_cart')
    
    if products_in_cart:
        # products_in_cart += '_'+id+':'+name+':'+price
        products_in_cart += '_'+id+':'+amount_to_add
    else:
        # products_in_cart = id+':'+name+':'+price
        products_in_cart = id+':'+amount_to_add
    
    resp = make_response(render_template('addedtocart.html', id=id))
    resp.set_cookie('in_cart', products_in_cart)
    return resp

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

# place an order in cart page
@views.route('/placeorder', methods=['POST'])
def place_order():
    text = request.cookies.get('in_cart')
    cart_list = text.split('_') if text else []
    cart_products = []
    for q in cart_list:
        info = q.split(':')
        cart_products.append(
            {'id' : info[0],
             'amount' : info[1]}
        )
    pass

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
    