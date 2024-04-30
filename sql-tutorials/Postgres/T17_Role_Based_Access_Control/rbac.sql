-- create roles
create role test_role; 

-- create users 
create user test_user with password 'test';

-- grant roles
grant test_role to test_user;

-- database permissions
grant select on all tables in schema public to test_role; 

-- revoke permissions
revoke select on all tables in schema public from test_role; 