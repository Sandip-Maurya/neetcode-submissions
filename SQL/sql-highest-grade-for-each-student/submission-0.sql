-- Write your query below

select outer_er.student_id, min(outer_er.exam_id) as exam_id, min(score) as score
from exam_results outer_er
where score = (
    select max(inner_er.score)
    from exam_results inner_er
    where outer_er.student_id = inner_er.student_id
)

group by outer_er.student_id

order by outer_er.student_id asc;