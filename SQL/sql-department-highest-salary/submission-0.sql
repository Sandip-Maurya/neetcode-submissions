-- Write your query below
with department_max_salary as (
    select
    d.id as department_id,
    d.name as department,
    max(e.salary) as salary
    from employee e
    join department d on e.department_id = d.id
    group by d.id, d.name
)

select 
    dm.department as department,
    e.name as employee,
    dm.salary as salary
from employee e 
join department_max_salary dm on e.department_id = dm.department_id
where e.salary = dm.salary