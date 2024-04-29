-- Order Processing Time
with shipping as (
	select
		order_id,
		order_date,
		ship_date,
		ship_date - order_date as date_diff,
		region,
		order_priority,
		ship_mode
	from orders
)
select 
	region,
	order_priority,
	ship_mode,
	round(avg(date_diff)::numeric, 2) as avg_days,
	max(date_diff) as max_days
from shipping
where date_diff > 5
group by region, order_priority, ship_mode
order by avg_days desc;

-- multi-region customers
with multi_region_customers as (
	select
		customer_name, 
		count(distinct region) as num_regions
	from orders
	group by customer_name
	having count(distinct region) > 1
),
num_regions_table as (
	select 
		o.customer_name,
		o.order_id,
		o.sales,
		o.region,
		mrc.num_regions
	from orders o
		join multi_region_customers as mrc on mrc.customer_name = o.customer_name
)

select
	customer_name,
	region,
	count(*) as num_orders,
	dense_rank() over(partition by customer_name order by count(*) desc) as most_orders_region_rank,
	dense_rank() over(partition by customer_name order by sum(sales) desc) as most_sales_region_rank,
	round(sum(sales)::numeric,2) as total_sales
from num_regions_table
group by customer_name, region;

-- Year-over-Year Growth Rate
select 
	year_of_order,
	category,
	round((((total_sales/last_year_sales)-1)*100)::numeric, 2) as yoy_growth_percentage
from (
	select
		date_part('year', order_date) as year_of_order,
		category,
		sum(sales) as total_sales,
		lag(sum(sales)) over(partition by category order by date_part('year', order_date)) as last_year_sales
	from orders
	group by 1, category
) as t1
