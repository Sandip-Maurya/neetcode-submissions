-- Write your query below

SELECT s.seller_name
FROM seller s
LEFT JOIN orders o
ON s.seller_id = o.seller_id
and (o.sale_date BETWEEN '2020-01-01' and '2020-12-31' )
where order_id is null 
ORDER BY seller_name;