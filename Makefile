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