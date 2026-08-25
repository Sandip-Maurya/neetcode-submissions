-- Write your query below

select 
    case 
        when e.employee_id is not null then e.employee_id
        when s.employee_id is not null then s.employee_id
    end as employee_id
from employees e
    full join salaries s on s.employee_id = e.employee_id
where e.name is null 
    or s.salary is null 
order by employee_id asc