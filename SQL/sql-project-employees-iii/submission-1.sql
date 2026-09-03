-- Write your query below

select me.project_id, me.employee_id 
from (
    select 
        p.project_id,
        e.employee_id,
        rank() over(
            partition by p.project_id order by e.experience_years desc
        ) as max_exp_ranking
    from project p join employee e on e.employee_id=p.employee_id
) me 
where me.max_exp_ranking = 1

