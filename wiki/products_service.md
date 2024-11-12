# products info:

## Nav-links:

- **[Master](/README.md)**
- [frontend](/wiki/frontend.md)
- [products](/wiki/products_service.md)
- [products_db](/wiki/products_db.md)
- [orders](/wiki/orders_service.md)
- [orders_db](/wiki/orders_db.md)

## General:

This is the products service. We use a Python-Flask-SQLAlchemy framework, to handle http requests from the frontend service, and make queries to the products database. We chose this particular framework because it is easy to learn, lightweight, based on Python (which we know better than JS); and because complexity and concurrency in "production" are expected to be low (thus, moderately slow Python code is not something to worry about).

## Files:

- *Python*:
    1. [main.py](/products/main.py):
        The main code for our app.
- *Misc*:
    1. [Dockerfile](/products/Dockerfile):
        Dockerfile for the products backend container.