-- Total Sales by Region
select 
	region,
	round(sum(sales)::numeric, 2) as total_sales
from orders
group by region
order by total_sales;

-- Total Sales per Category
select 
	category,
	round(sum(sales)::numeric, 2) as total_sales
from orders
group by category
order by total_sales;

-- Orders by Country and Ship Mode
select
	country,
	ship_mode,
	count(*) as total_orders
from orders
group by country, ship_mode
order by total_orders desc;

-- Discount per Sub-Category
select 
	sub_category,
	round(avg(discount)::numeric * 100, 2) as average_discount_percentage
from orders
group by sub_category
order by average_discount_percentage desc;