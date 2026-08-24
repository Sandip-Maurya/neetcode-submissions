-- Write your query below

with ordered_point as (
    select x, lead(x) over (order by x) as next_x  from point
)

select min(abs(x-next_x)) as shortest from ordered_point;
