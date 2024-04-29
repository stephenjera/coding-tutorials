-- Ranked Top Selling Products by Category
select 
	product_name,
	category,
	round(sum(sales::numeric),0) as total_sales,
	dense_rank() over(partition by category order by sum(sales) desc) as sales_rank
from orders
group by product_name, category
order by sales_rank;

-- High-Value Customers
-- method 1
select
    t1.customer_id,
    (
        select o.customer_name
        from orders o
        where o.customer_id = t1.customer_id
        limit 1
    ),
    t1.total_orders,
    t1.sum_sales
from (
    select
        customer_id,
        count(*) as total_orders,
        round(sum(sales)::numeric, 2) as sum_sales
    from
        orders
    group by
        customer_id
) as t1
where
    t1.total_orders > 10
    and t1.sum_sales > 10000;

-- method 2
select
	distinct(t1.customer_id),
    o.customer_name,
    t1.total_orders,
    t1.sum_sales
from (
	select 
		customer_id,
		count(*) as total_orders,
		round(sum(sales)::numeric,2) as sum_sales
	from orders
	group by customer_id
) as t1
join orders o ON t1.customer_id = o.customer_id
where total_orders > 10 and sum_sales > 10000;

-- Running Total of Sales
select
	distinct(order_date),
	sum(sales) over(order by order_date) as running_total
from orders
order by order_date asc;

-- Top Products by Profit
with ranked_profits as(
	select
		product_name,
		category,
		region,
		sum(profit) as total_profit,
		dense_rank() over(partition by region order by sum(profit) desc) as profit_rank
	from orders
	group by product_name, category, region
)
select
	profit_rank,
    product_name,
    category,
    region,
    round(total_profit::numeric, 2)
from ranked_profits
where profit_rank <= 3
order by region, profit_rank;