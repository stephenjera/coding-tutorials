CREATE DATABASE testDB;

USE testdb;

CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

-- copy table
CREATE TABLE persons_copy AS
SELECT *
FROM Persons;

-- Alter table, add new column
ALTER TABLE persons_copy
ADD Email varchar(255);

-- Delete a column 
ALTER TABLE persons_copy
DROP COLUMN Email;

-- ADD new columns to Persons
ALTER TABLE Persons
ADD Email varchar(255),
ADD DateOfBirth date;

-- Change data type 
ALTER TABLE Persons
MODIFY COLUMN DateOfBirth year;

SELECT * FROM Persons


