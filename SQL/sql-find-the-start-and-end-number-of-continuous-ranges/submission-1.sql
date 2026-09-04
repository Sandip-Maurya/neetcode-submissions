-- Write your query below

with logs_with_ids as (
    select log_id, row_number() over () as id from (
        select log_id from logs order by log_id
    ) 
)

select
    start_id,
    end_id
 from (
    select 
        (log_id-id) as diff, 
        min(log_id) as start_id, 
        max(log_id) as end_id 
    from logs_with_ids 
    group by (log_id - id)
    order by start_id
 )
        