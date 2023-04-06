-- order by date
select order_id,
    order_date
from orders
order by order_date asc;

-- order b customer name length
select customer_name,
    length(customer_name) as len
from orders
order by len;