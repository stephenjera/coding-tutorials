USE sql_store;

SELECT 
	first_name, 
    last_name,
    points,
    points * 10 + 100 as increase
FROM customers
WHERE customer_id > 3
ORDER BY last_name DESC