-- Write your query below

with unpivoted_championships as (
    select 
        year, 
        wimbledon as champion_player_id
    from championships 
    union all
    select 
        year,
        fr_open as champion_player_id
    from championships 
    union all
    select 
        year,
        us_open as champion_player_id
    from championships 
    union all
    select 
        year,
        au_open as champion_player_id
    from championships 
)

select 
    players.player_id,
    players.player_name,
    count(unpivoted_championships.champion_player_id) as grand_slams_count
from unpivoted_championships
join players on players.player_id = unpivoted_championships.champion_player_id
group by players.player_id, players.player_name
