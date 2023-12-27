#!/bin/bash

# Define variables
CONTAINER_NAME=postgres
DB_USER=docker
CSV_FILE=global_superstore_orders_2018.csv
CSV_FOLDER=global_superstore
DATABASE=global_superstore
TABLE=orders


# Create superstore global database
docker exec -it $CONTAINER_NAME createdb -U $DB_USER $DATABASE

# Copy csv to container 
docker cp ../datasets/$CSV_FOLDER/$CSV_FILE postgres:/var/lib/postgresql/data

# Connect to the "superstore" database
docker exec -it $CONTAINER_NAME psql -U $DB_USER -d $DATABASE -c "create table if not exists $TABLE (
    Row_ID int not null,
    Order_ID varchar(255) not null,
    Order_Date date,
    Ship_Date date,
    Ship_Mode varchar(255) not null,
    Customer_ID varchar(255) not null,
    Customer_Name varchar(255) not null,
    Segment varchar(255) not null,
    Postal_Code varchar(255),
    City varchar(255) not null,
    State varchar(255) not null,
    Country varchar(255) not null,
    Region varchar(255) not null,
    Market varchar(255) not null,
    Product_ID varchar(255) not null,
    Product_Name varchar(255) not null,
    Sub_Category varchar(255) not null,
    Category varchar(255) not null,
    Sales float not null,
    Quantity int not null,
    Discount float not null,
    Profit float not null,
    Shipping_Cost float not null,
    Order_Priority varchar(255) not null,
    primary key(row_ID)
) ;"


# Load the data from the CSV file into the table
docker exec -it $CONTAINER_NAME psql -U $DB_USER -d $DATABASE -c "SET datestyle = 'ISO, DMY'; TRUNCATE TABLE $TABLE; COPY $TABLE(
    Row_ID,
    Order_ID,
    Order_Date,
    Ship_Date,
    Ship_Mode,
    Customer_ID,
    Customer_Name,
    Segment,
    Postal_Code,
    City,
    State,
    Country,
    Region,
    Market,
    Product_ID,
    Product_Name,
    Sub_Category,
    Category,
    Sales,
    Quantity,
    Discount,
    Profit,
    Shipping_Cost,
    Order_Priority)
    FROM '/var/lib/postgresql/data/$CSV_FILE' DELIMITER ',' CSV HEADER;"


# Check that the data has been loaded into the table
# docker exec -it $CONTAINER_NAME psql -U $DB_USER -d $DATABASE -c "SELECT * FROM $TABLE;"

#Remove CSV from container
docker exec -it postgres rm /var/lib/postgresql/data/$CSV_FILE