-- Group all orders by product category and count the number of orders in each group
select category,
    count(*) as num_orders
from orders
group by category;

-- Group all orders by ship mode and calculate the average shipping cost for each ship mode
select ship_mode,
    avg(shipping_cost) as average_shipping_cost
from orders
group by ship_mode;