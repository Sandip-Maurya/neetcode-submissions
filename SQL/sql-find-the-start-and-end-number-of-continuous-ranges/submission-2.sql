-- Write your query below

with numbered_logs as (
    select log_id, log_id - row_number() over (order by log_id) as id from logs
)

select
    min(log_id) as start_id,
    max(log_id) as end_id
from numbered_logs
group by id
order by start_id