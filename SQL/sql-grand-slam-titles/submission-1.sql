-- Write your query below

select 
    p.player_id, 
    p.player_name,
    count(*) as grand_slams_count
from championships c 
cross join unnest(
    array[
        c.wimbledon, c.fr_open, c.us_open, c.au_open
    ]
) as u(player_id)
join players p on p.player_id = u.player_id
group by p.player_id, p.player_name
