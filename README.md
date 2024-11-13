# Master info:

## Nav-links:

- **[Master](/README.md)**
- [frontend](/wiki/frontend.md)
- [products](/wiki/products_service.md)
- [products_db](/wiki/products_db.md)
- [orders](/wiki/orders_service.md)
- [orders_db](/wiki/orders_db.md)

## General:

Welcome to RUNE, the e-shop for the souls of the dead! Unofrtunately there was not enough time to make it all full functional... But

## Directories:

- *Services/Containers*:
    1. [frontend](/frontend/):
        The frontend container.
    2. [orders](/orders/):
        The orders service container.
    3. [orders_db](/orders_db):
        The orders database container.
    4. [products](/products/):
        The products service container.
    5. [products_db](/products_db/):
        The products database container.
- *Misc*:
    1. [wiki](/wiki/):
        Directory with Markdown documentation on each of the 5 services.

## Files:

- *Misc*:
    1. [docker-compose.yaml](docker-compose.yaml):
        Compose file for all our docker containers.
    2. [Makefile](Makefile):
        Makefile for running the app more conveniently. Nothing more than a wrapper for various docker-compose commands.
    3. [README.md](README.md):
        Readme file for the whole app. Start here to RTFM.

