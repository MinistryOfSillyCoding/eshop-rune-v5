# products_db info:
=============================

## Nav-links:
=============================

- **[Master](/README.md)**
- [frontend](/frontend/README.md)
- [products](/wiki/products_service.md)
- [products_db](/wiki/products_db.md)
- [orders](/wiki/orders_service.md)
- [orders_db](/wiki/orders_db.md)

## General:
=============================

This is the Database to use for the Products service. It stores all the products. Users and the database are initialized by the [create_db.sql](/products_db/scripts/create_db.sql) sql script. Tables and entries are initialized remotely from the Products service. The reason for this separation is that we tried initializing everything here, and it didn't work.

## Files:
=============================

- *SQL*:
    1. [create_db.sql](/products_db/scripts/create_db.sql):
        A custom small initializing script for our db.
- *Misc*:
    1. [Dockerfile](/products_db/Dockerfile):
        Dockerfile for the db. We use a dockerfile (as opposed to running from an image in our [docker-compose](/docker-compose.yaml)), because we want to load a custom initializing script.

## DB:
=============================

- **Type**: Postgresql database
- **Name**: products_db
- **Owner**: products_service
- **Exposed Port**: 5432
- **Users**:
    1. Admin:
        - **Username**: postgres
        - **Password**: postgres
    2. Products service:
        - **Username**: products_service
        - **Password**: welikeproducts
- **Tables**:
    1. Products:
        - **Table name**: products
        - **Columns**:
            1. Id:
                - **Column name**: products_id
                - **Type**: Integer
                - **Properties**: Primary Key (Unique, Not Null, Auto-Increment)
            2. Title:
                - **Column name**: products_name (seeing as we're selling souls, that's a proper title)
                - **Type**: String (Varchar(255))
                - **Properties**: *(TODO)* Not Null
            3. Img:
                - *(TODO)*
            4. Price:
                - **Column name**: products_price
                - **Type**: Float
                - **Properties**: *(TODO)*
            5. Quantity:
                - **Column name**: products_quantity
                - **Type**: Integer
                - **Properties**: *(TODO)*

            