CREATE ROLE products_service WITH LOGIN CREATEDB PASSWORD 'welikeproducts';
CREATE DATABASE products_db OWNER products_service;