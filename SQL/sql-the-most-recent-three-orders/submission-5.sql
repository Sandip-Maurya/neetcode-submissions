-- Write your query below

select c.name as customer_name, c.customer_id, ro.order_id, ro.order_date
from customers c 
cross join lateral (
    select o.order_id, o.order_date
    from orders o 
    where o.customer_id = c.customer_id
    order by o.order_date desc 
    limit 3
) ro
order by customer_name asc, customer_id asc, order_date desc, order_id asc;