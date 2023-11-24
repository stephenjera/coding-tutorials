-- Count the number of orders in each region
select region,
    count(*) as num_orders
from orders
group by region;

-- Count the number of returns in each region
select region,
    count(*) as num_returns
from returns
group by region;

-- Select the top 5 products by sales, ordered by sales in descending order
select product_name,
    sum(sales) as total_sales
from orders
group by product_name
order by total_sales desc
limit 5;

-- Group all orders by order date and calculate the total sales for each day
select order_date,
    sum(sales) as total_sales
from orders
group by order_date;

-- Calculate the average shipping cost per order in each region
select region,
    avg(shipping_cost) as avg_shipping_cost_per_order
from orders
group by region;

-- Find the highest shipping cost for an order in each region
select region,
    max(shipping_cost) as highest_shipping_cost
from orders
group by region;

-- Find the lowest order amount in each region
select region,
    min(sales) as lowest_order_amount
from orders
group by region;