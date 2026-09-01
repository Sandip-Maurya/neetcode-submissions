-- Write your query below

select 
    p.product_name as product_name,
    p.product_id as product_id,
    o.order_id as order_id,
    o.order_date as order_date
from orders o 
    join products p on p.product_id = o.product_id

where (o.product_id, o.order_date) in (
    select product_id, max(order_date) as order_date from orders group by product_id
)

order by product_name  asc, product_id asc, order_id asc 