-- Write your query below
with call_logs as  
(
    select caller_id as person_id, duration from calls
    union all 
    select callee_id as person_id, duration from calls 
)

select c.name as country 
from country c
join person on c.country_code = left(person.phone_number, 3)
join call_logs on call_logs.person_id = person.id
group by c.name
having avg(duration) > (
    select avg(duration) from call_logs
)