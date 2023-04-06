-- get every column
select *
from orders;

-- get unique categories 
select distinct category
from orders;

-- concatenation
select customer_name || ' ' || ship_date as combined
from orders;

-- aliasing 
select 5 * 3 as multiplication;