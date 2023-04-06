#!/bin/bash

# Define variables
CONTAINER_NAME=postgres
DB_USER=docker
CSV_FILE=global_superstore_returns_2018.csv
CSV_FOLDER=global_superstore
DATABASE=global_superstore
TABLE=returns


# Create superstore global database
docker exec -it $CONTAINER_NAME createdb -U $DB_USER $DATABASE

# Copy csv to container 
docker cp ../datasets/$CSV_FOLDER/$CSV_FILE postgres:/var/lib/postgresql/data

# Connect to the "superstore" database
docker exec -it $CONTAINER_NAME psql -U $DB_USER -d $DATABASE -c "create table if not exists $TABLE (
    Returned varchar(255) not null,
    Order_ID varchar(255) not null,
    Region varchar(255) not null
) ;"


# Load the data from the CSV file into the table
docker exec -it $CONTAINER_NAME psql -U $DB_USER -d $DATABASE -c "TRUNCATE TABLE $TABLE; COPY $TABLE(
    Returned,
    Order_ID,
    Region)
    FROM '/var/lib/postgresql/data/$CSV_FILE' DELIMITER ',' CSV HEADER;"


# Check that the data has been loaded into the table
# docker exec -it $CONTAINER_NAME psql -U $DB_USER -d $DATABASE -c "SELECT * FROM $TABLE;"

#Remove CSV from container
docker exec -it postgres rm /var/lib/postgresql/data/$CSV_FILE