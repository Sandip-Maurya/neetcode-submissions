-- Write your query below

select seat_id
from (
    select seat_id,
    free,
    lag(free) over (
        order by seat_id
    ) as pre_seat,
    lead(free) over (
        order by seat_id
    ) as next_seat
    from cinema 

) t
where free = 1 
and (pre_seat = 1 
 or next_seat = 1)

order by seat_id asc;