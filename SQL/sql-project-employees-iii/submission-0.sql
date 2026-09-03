-- Write your query below

with max_experience_employee as (
    select 
        p.project_id,
        max(e.experience_years) as max_exp
    from project p
        join employee e on p.employee_id=e.employee_id
    group by p.project_id  
)

select 
    p.project_id, 
    p.employee_id
from project p
cross join lateral (
    select * from max_experience_employee me where p.project_id = me.project_id
) m 
where p.employee_id in (
    select employee_id from employee where experience_years = m.max_exp
)


