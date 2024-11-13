FROM postgres:latest

EXPOSE 5432

# we can copy custom scripts and configs like this:
# "/docker-entrypoint-initdb.d" runs all .sh, .sql & .sql.gz scripts in it when the container is started for the 1st time
COPY ./scripts/ /docker-entrypoint-initdb.d/