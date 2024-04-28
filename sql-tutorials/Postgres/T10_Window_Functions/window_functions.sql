-- RANK() assigns a rank to each row within a partition, allowing gaps between ranks.
select 
	extract(year from order_date) as order_year,
	order_id,
	sales,
	rank() over (
			partition by extract(year from order_date) 
			order by sales desc
		) as sales_rank
from orders
order by sales_rank asc, year asc;

-- DENSE_RANK() assigns a rank to each row within a partition, without gaps between ranks.
select 
	extract(year from order_date) as order_year,
	order_id,
	sales,
	dense_rank() over (partition by extract(year from order_date) order by sales desc) as sales_rank
from orders
order by sales_rank asc, order_year asc;

-- ROW_NUMBER() assigns a sequential number to each row within a partition, starting from 1.
select 
  order_year,
  order_id,
  sales,
  sales_rank,
  row_num
from (
  select 
    extract(year from order_date) as order_year,
    order_id,
    sales,
    dense_rank() over (
			partition by extract(year from order_date) 
			order by sales desc
		) as sales_rank,
    row_number() over (
			partition by extract(year from order_date) 
			order by sales desc
		) as row_num
  from orders
) as ranked_orders
where row_num between 20 and 45  -- replace with your pagination logic
order by row_num;

-- PERCENT_RANK() calculates the relative rank of a row within a partition as a percentage.
select 
	extract(year from order_date) as order_year,
	order_id,
	sales,
	percent_rank() over (
			partition by extract(year from order_date) 
			order by sales asc
		) as sales_rank
from orders
order by sales_rank desc, order_year asc;
-- FIRST_VALUE() returns the first value (within a partition) for a specified expression.

-- LAST_VALUE() returns the last value (within a partition) for a specified expression.

-- LAG() retrieves the value of an expression a specified number of rows before the current row.

-- LEAD() retrieves the value of an expression a specified number ofrows after the current row.

-- NTILE() divides the result set into a specified number of partitions (tiles) and assigns a tile number to each row.

-- CUME_DIST() calculates the cumulative distribution of rows within a partition.

