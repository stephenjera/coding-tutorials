-- order by date
select order_id,
    order_date
from orders
order by order_date asc;

-- order by customer name length
select customer_name,
    length (customer_name) as len
from orders
order by len;

-- Order all orders by customer segment, then by customer ID, both in descending order
select *
from orders
order by segment desc,
    customer_id desc;