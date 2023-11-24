-- Create database
create database testdb;

-- Create schema
create SCHEMA test_schema;

-- Create table
create table test_schema.Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

-- Copy table
create table test_schema.persons_copy as table test_schema.Persons;