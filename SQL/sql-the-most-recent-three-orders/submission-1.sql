-- Write your query below

with ranked_orders as (
    select 
        order_id,
        row_number() over(
            partition by customer_id
            order by order_date desc 
        ) as order_rank
    from orders
)

select 
    c.name as customer_name, 
    c.customer_id as customer_id,
    o.order_id as order_id,
    o.order_date as order_date
from orders o 
    join customers c on c.customer_id = o.customer_id
    join ranked_orders ro on ro.order_id = o.order_id
where ro.order_rank <= 3
order by c.name asc, c.customer_id, o.order_date desc