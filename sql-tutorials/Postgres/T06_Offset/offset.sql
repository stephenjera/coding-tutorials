-- Select the first 10 rows from the orders table
select *
from orders
order by order_date offset 0
limit 10;

-- Select the next 10 rows from the orders table, starting after the first 10 rows
select *
from orders
order by order_date offset 10
limit 10;