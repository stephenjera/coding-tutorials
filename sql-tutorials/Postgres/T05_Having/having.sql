-- Select all product categories with total sales over \$100,000
select sub_category
from orders
group by sub_category
having sum(sales) > 100000;