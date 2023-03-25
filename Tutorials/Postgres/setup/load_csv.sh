#!/bin/bash

# Define variables
CONTAINER_NAME=postgres
DB_USER=docker
CSV_FILE=superstore.csv
DATABASE=superstore
TABLE=superstore

# Copy the CSV file to the container
docker cp $CSV_FILE $CONTAINER_NAME:/tmp/$CSV_FILE

# Connect to the PostgreSQL database inside the container
docker exec -it $CONTAINER_NAME psql -U DB_USER -d $DATABASE -c "create table if not exists $TABLE (
    id serial not null,
    ship_model varchar(255) not null,
    segment varchar(255) not null,
    country varchar(255) not null,
    city varchar(255) not null,
    state varchar(255) not null,
    postal_code int not null,
    region varchar(255) not null,
    category varchar(255) not null,
    subcategory varchar(255) not null,
    sales float not null,
    quantity int not null,
    discount float not null,
    profit float not null,
    primary key(id)
) ;"

#"CREATE TABLE $TABLE (id SERIAL PRIMARY KEY, name TEXT, age INTEGER);"

# Load the data from the CSV file into the table
docker exec -it $CONTAINER_NAME psql -U DB_USER -d $DATABASE -c "COPY %TABLE(
    id,
    ship_model,
    segment,
    country,
    city,
    state,
    postal_code,
    region,
    category,
    subcategory,
    sales,
    quantity,
    discount,
    profit)
    FROM '/tmp/$CSV_FILE' DELIMITER ',' CSV HEADER;"

#"COPY $TABLE(name, age) FROM '/tmp/$CSV_FILE' DELIMITER ',' CSV HEADER;"

# Check that the data has been loaded into the table
docker exec -it $CONTAINER_NAME psql -U DB_USER -d $DATABASE -c "SELECT * FROM $TABLE;"

# Remove the CSV file from the container
docker exec -it $CONTAINER_NAME rm /tmp/$CSV_FILE
