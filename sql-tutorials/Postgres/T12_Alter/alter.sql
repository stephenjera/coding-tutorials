-- Alter table, add new column
alter table test_schema.persons_copy
add column Email varchar(255);

-- Delete a column 
alter table test_schema.persons_copy drop column Email;

-- Add new columns to Persons
alter table test_schema.Persons
add column Email varchar(255),
    add column DateOfBirth date;

-- Change data type 
alter table test_schema.Persons
alter column DateOfBirth type varchar(4);