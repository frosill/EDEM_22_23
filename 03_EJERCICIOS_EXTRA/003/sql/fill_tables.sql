
-- Inserting data into product table
INSERT INTO product (product_id, name) VALUES (1, champu);
INSERT INTO product (product_id, name) VALUES (2, gel);
INSERT INTO product (product_id, name) VALUES (3, jabon);
INSERT INTO product (product_id, name) VALUES (4, esponja);

-- Inserting data into country table
INSERT INTO country (country_id, country_name) VALUES (234, Spain);
INSERT INTO country (country_id, country_name) VALUES (321, China);
INSERT INTO country (country_id, country_name) VALUES (289, India);
INSERT INTO country (country_id, country_name) VALUES (124, Finland);
INSERT INTO country (country_id, country_name) VALUES (783, EEUU);

-- Inserting data into city table
INSERT INTO city (city_id, city_name, country_id) VALUES (2341, Albacete, 234);
INSERT INTO city (city_id, city_name, country_id) VALUES (2348, Madrid, 234);
INSERT INTO city (city_id, city_name, country_id) VALUES (3216, Hong Kong, 321);
INSERT INTO city (city_id, city_name, country_id) VALUES (7833, Chicago, 783);
INSERT INTO city (city_id, city_name, country_id) VALUES (2897, Nueva Delhi, 289);
INSERT INTO city (city_id, city_name, country_id) VALUES (1247, Helsinki, 124);

