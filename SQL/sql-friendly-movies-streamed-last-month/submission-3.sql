-- Write your query below

select distinct c.title 
from tv_program t
    join content c on c.content_id = t.content_id
where t.program_date >= '2020-06-01' 
    and t.program_date < '2020-07-01'
    and c.kids_content = 'Y'
    and c.content_type = 'Movies'