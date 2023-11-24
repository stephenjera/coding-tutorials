-- Select all orders that have a higher sales amount than the average order amount
select *
from orders
where sales > (
        select avg(sales)
        from orders
    );

-- Select all orders that have been returned and for which the shipping cost is greater than the average shipping cost 
select *
from orders
    inner join returns on orders.order_id = returns.order_id
where shipping_cost > (
        select avg(shipping_cost)
        from orders
    );