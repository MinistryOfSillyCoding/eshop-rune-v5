CREATE ROLE orders_service WITH LOGIN CREATEDB PASSWORD 'welikeorders';
CREATE DATABASE orders_db OWNER orders_service;