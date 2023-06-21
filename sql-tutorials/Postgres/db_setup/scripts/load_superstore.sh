#!/bin/bash

# Define variables
CONTAINER_NAME=postgres
DB_USER=docker
CSV_FILE=superstore.csv
DATABASE=superstore
TABLE=superstore


# Create superstore database
docker exec -it $CONTAINER_NAME createdb -U $DB_USER $DATABASE

# Copy csv to container 
docker cp ../datasets/$CSV_FILE postgres:/var/lib/postgresql/data

# Connect to the "superstore" database
docker exec -it $CONTAINER_NAME psql -U $DB_USER -d $DATABASE -c "create table if not exists $TABLE (
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

# Load the data from the CSV file into the table
docker exec -it $CONTAINER_NAME psql -U $DB_USER -d $DATABASE -c "TRUNCATE TABLE $TABLE; COPY $TABLE(
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
    FROM '/var/lib/postgresql/data/$CSV_FILE' DELIMITER ',' CSV HEADER;"


# Check that the data has been loaded into the table
# docker exec -it $CONTAINER_NAME psql -U $DB_USER -d $DATABASE -c "SELECT * FROM $TABLE;"

#Remove CSV from container
docker exec -it postgres rm /var/lib/postgresql/data/superstore.csv