-- Write your query below


select c.customer_id as customer_id, c.name as name
from orders o
join product p on p.product_id = o.product_id
join customers c on c.customer_id = o.customer_id
where o.order_date >= '2020-06-01' and o.order_date <= '2020-07-31'
group by c.customer_id
having 
    sum(
        case
            when o.order_date >= '2020-06-01' and o.order_date <= '2020-06-30' then o.quantity*p.price 
            else 0  
        end 
    ) >= 100
    and 
    sum (
        case
            when o.order_date >= '2020-07-01' and o.order_date <= '2020-07-31' then o.quantity*p.price
            else 0  
        end 
    ) >= 100