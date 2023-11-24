-- count all row with id greater than 30,000
select count(order_id)
from orders
where row_id > 30000;

select *
from orders
where order_date > '2016-11-04';

select *
from orders
where order_date > '2016-11-04'
    and ship_mode = 'first class';

select *
from orders
where customer_name like '%Smith';