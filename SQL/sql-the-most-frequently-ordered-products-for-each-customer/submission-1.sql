-- Write your query below

select 
    rk_orders.customer_id, 
    rk_orders.product_id, 
    products.product_name
from (
    select 
        customer_id, 
        product_id, 
        rank() over (
            partition by customer_id order by count(*) desc
        ) as product_rank 

    from orders
    group by customer_id, product_id
) rk_orders
join products on rk_orders.product_id = products.product_id
join customers on rk_orders.customer_id = customers.customer_id

where rk_orders.product_rank = 1
-- order by 