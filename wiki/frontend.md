# frontend info:

## Nav-links:

- **[Master](/README.md)**
- [frontend](/wiki/frontend.md)
- [products](/wiki/products_service.md)
- [products_db](/wiki/products_db.md)
- [orders](/wiki/orders_service.md)
- [orders_db](/wiki/orders_db.md)

## General:



## Files:

- *Python*:
    1. [__init__.py](/frontend/website/__init__.py):
        *(TODO)*
    2. [main.py](/frontend/main.py):
        *(TODO)*
    3. [views.py](/frontend/website/views.py):
        Contains the routes and request handling for the frontend.
- *Html+CSS*:
    1. [base.html](/frontend/website/templates/base.html):
        The base html for our webapp. A base template that is built upon in each page using the Jinja framework. Contains the navbar.
    2. [cart.html](/frontend/website/templates/cart.html):
        The template for the "my cart" page, where the client can see what products are in their pending order before they place it, and place/submit the order.
    3. [catalog.html](/frontend/website/templates/catalog.html):
        The template for the catalog page, where the client can see a list of all available products.
    4. [home.html](/frontend/website/templates/home.html):
        The template for the homepage of our eshop, RUNE. Contains a masterfully crafted description of our service.
    5. [myproducts.html](/frontend/website/templates/myproducts.html):
        The template for the "my products" page, where the client can create new products to go into the catalog.
    5. [orders.html](/frontend/website/templates/orders.html):
        The template for the orders page, where the client can see a history of all placed orders.
    6. [styles.css](/frontend/website/static/styles.css):
        The .css file for styling our webapp.
- *Javascript*:
- *Misc*:
    1. [Dockerfile](/frontend/Dockerfile):
        Dockerfile for the frontend service container.