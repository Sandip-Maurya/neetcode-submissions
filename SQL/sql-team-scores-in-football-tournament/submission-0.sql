WITH match_points AS (
    SELECT
        t.team_id,
        t.team_name,
        CASE
            WHEN t.team_id = m.host_team
                 AND m.host_goals > m.guest_goals THEN 3
            WHEN t.team_id = m.guest_team
                 AND m.guest_goals > m.host_goals THEN 3
            WHEN m.host_goals = m.guest_goals THEN 1
            ELSE 0
        END AS points_per_match
    FROM teams AS t
    LEFT JOIN matches AS m
        ON t.team_id = m.host_team
        OR t.team_id = m.guest_team
)

select team_id, team_name,
    sum(points_per_match) as num_points 
from match_points
group by team_id, team_name
order by num_points desc, team_id asc;