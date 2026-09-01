-- Write your query below

select customer_name, customer_id, order_id, order_date
from (
    select 
        c.name as customer_name, 
        c.customer_id as customer_id,
        o.order_id as order_id,
        o.order_date as order_date,
        row_number() over (
            partition by o.customer_id
            order by o.order_date desc
        ) as ranking 
    from orders o 
        join customers c on c.customer_id = o.customer_id

)
where ranking <= 3
order by customer_name asc, customer_id asc, order_date desc, order_id asc;