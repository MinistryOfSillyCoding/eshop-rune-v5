# Master info:

## Nav-links:

- **[Master](/README.md)**
- [frontend](/wiki/frontend.md)
- [products](/wiki/products_service.md)
- [products_db](/wiki/products_db.md)
- [orders](/wiki/orders_service.md)
- [orders_db](/wiki/orders_db.md)

## General:

### Introduction:

Welcome to RUNE, the e-shop for the souls of the dead! Unofrtunately there was not enough time to make it all full functional...
But, I have made a [public repo on github](https://github.com/MinistryOfSillyCoding/eshop-rune-v5), and would love to continue work on it until at least
all the core functionality is finished. Please, inform me if that's possible.

Here is a list of the most important missing features:
    - Placing an order. There just barely was not enough time. The infrastructure is almost finished too, but what can you do?
    - Having an image for each product. As it stands now, all images are mere placeholders.
    - Removing things from cart once they're there. Would be handy.
    - Making things pretty and/or readable with css
    - Finishing the documentation. And I wanted it to be so fancy too. Ah well.

Here is a list of features that *DO* exist though:
    - The entire file/container structure and databases
    - The entire products service and database functionality (aside from the images thing).

> And should I fail, I should at least feel honoured to have come this far


### Installation/Running/How to Use:

First, you must have Docker on your machine. I use Docker Desktop. Once the Docker Engine is running, simply cd into the [main work directory](/), 
and enter the command "make" in terminal. It's that simple. (I've got a Makefile as a wrapper fpr docker-compose, cause why not?).
Once the containers are all running (please do check that all 5 containers are running, sometimes when I start with no volumes the backend services can't access their respective db's, I don't know why. If that happens, simple  enter the command "make re" to stop and then rerun everything),
you can access the webapp on [localhost](http://localhost:8081/), port 8081. And that's all folks.

_my apologies for the unfinished work, but please have fun to make up for it_

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

