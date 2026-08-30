-- Write your query below
with activity_with_first_login as (
    select 
        player_id,
        device_id,
        event_date,
        min(event_date) over(
            partition by player_id
        ) as first_login 
    from activity
)

select distinct player_id, device_id
from activity_with_first_login
where event_date = first_login