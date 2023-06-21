-- count all row with id greater than 30,000
select count(order_id)
from orders
where row_id > 30000;