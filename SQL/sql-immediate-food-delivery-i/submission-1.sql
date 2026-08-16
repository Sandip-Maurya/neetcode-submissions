-- Write your query below

select round(
    avg(
        case when order_date = customer_pref_delivery_date 
            then 100.0 
            else 0
        end
    )
    , 
    2
) as immediate_percentage 
from delivery