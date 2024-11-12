# Makefile for convenience commands

# Run this to spin up the containers
# after updating their images
default:
	docker-compose up --build -d

# Run this to spin down the containers
down:
	docker-compose down

# Run this to update running containers
# spinning them down, updating, and then
# spinning them up again
re:
	docker-compose down
	docker-compose up --build -d

# to load the initial products into the db
# it is necessary to spin the containers up,
# down, and then up again. We've no idea why.
# Run this only if there is not already a created volume
full:
	docker-compose up --build -d
	docker-compose down
	docker-compose up --build -d