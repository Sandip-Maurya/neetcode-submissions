-- Write your query below

select users.name as name, COALESCE(sum(rides.distance), 0) as travelled_distance  from users 
left join rides
on users.id = rides.user_id 
group by name
ORDER BY travelled_distance desc, name asc
