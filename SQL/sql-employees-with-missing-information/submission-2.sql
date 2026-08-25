-- Write your query below

select COALESCE(e.employee_id, s.employee_id) as employee_id
from employees e
    full join salaries s on s.employee_id = e.employee_id
where e.name is null 
    or s.salary is null 
order by employee_id asc