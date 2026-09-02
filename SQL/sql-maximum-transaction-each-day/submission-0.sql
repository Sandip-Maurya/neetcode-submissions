-- Write your query below

with per_day_max_transaction_amount as (
    select day::date, max(amount) as max_amount from transactions
    group by day::date
)
select t.transaction_id
from transactions t
    join per_day_max_transaction_amount pdmt on pdmt.day = cast(t.day as date)
where t.amount = pdmt.max_amount
order by transaction_id asc