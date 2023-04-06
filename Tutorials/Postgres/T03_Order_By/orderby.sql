-- order by date
select order_id,
    order_date
from orders
order by order_date asc;

-- order by customer name length
select customer_name,
    length(customer_name) as len
from orders
order by len;

-- order by post code, nulls first 
select customer_name,
    postal_code
from orders
order by postal_code nulls first;