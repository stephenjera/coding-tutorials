-- Used to select the database to use when many are present 
USE sql_store;


-- Will casue a syntax error if statements order is changed 
-- Choose the name of the field (column)
SELECT 
	first_name, 
    last_name,
    points,
    points * 10 + 100 AS 'discount factor'  -- AS is the alias statement  
FROM customers  -- Choose table to use 
WHERE customer_id > 3  -- Used to filter records (rows)
ORDER BY last_name DESC;


-- Return all the products 
-- name 
-- unit price
-- new price (unit price * 1.1)
SELECT 
	name,
    unit_price,
    unit_price * 1.1 AS 'new price'
FROM products;


-- Using the where statement 
SELECT * 
FROM customers
-- Interates over all customers and returns those that match condition 
WHERE state != 'VA';


-- Get orders placed in 2019
SELECT * 
FROM orders 
WHERE order_date >= '2019-01-01';


-- Combining multiple search conditions when filtering data
SELECT * 
FROM customers
-- AND operator is always evaluated first 
WHERE birth_date >= '1990-01-01' OR points > 1000 AND state = 'VA';






