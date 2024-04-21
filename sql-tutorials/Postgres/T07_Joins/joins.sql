-- Select all orders and the corresponding return information
select 
    orders.*,
    returns.returned
from orders
    inner join returns on orders.order_id = returns.order_id;

-- Select all people, orders, and returns in the South Asian region
select 
    people.*,
    orders.*,
    returns.*
from people
    inner join orders on people.region = orders.region
    inner join returns on orders.order_id = returns.order_id
where people.region = 'southern asia';

-- Select all orders and corresponding returns, even if there's no return information
select 
    orders.*,
    returns.*
from orders
    left join returns on orders.order_id = returns.order_id;

-- Select all returns and corresponding orders, even if there's no order information for the return
select 
    orders.*,
    returns.*
from orders
    right join returns on orders.order_id = returns.order_id;

-- Select all orders and all returns, regardless of matching records
select
    orders.*,
    returns.*
from orders
    full join returns on orders.order_id = returns.order_id;
