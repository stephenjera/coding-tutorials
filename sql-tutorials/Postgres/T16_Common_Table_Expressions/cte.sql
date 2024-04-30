with orders_by_month as (
    select
        date_part('year', order_date) as order_year,
        date_part('month', order_date) as order_month,
        count(*) as order_count
    from
        orders
    group by
        date_part('year', order_date),
        date_part('month', order_date)
)
select
    order_year,
    order_month,
    order_count
from
    orders_by_month
order by
    order_year,
    order_month;