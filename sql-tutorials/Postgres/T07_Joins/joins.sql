-- Select all orders and the corresponding return information from the orders and returns tables
select orders.*,
    returns.returned
from orders
    inner join returns on orders.order_id = returns.order_id;

-- Select all people, orders, and returns in the South Asian region
select people.*,
    orders.*,
    returns.*
from people
    inner join orders on people.region = orders.region
    inner join returns on orders.order_id = returns.order_id
where people.region = 'Southern Asia';