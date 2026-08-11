-- Write your query below


select 
    e.left_operand,
    e.operator,
    e.right_operand,
    -- v_left.value AS left_value,
    -- v_right.value AS right_value,
    case e.operator
        when '>' then v_left.value > v_right.value
        when '<' then v_left.value < v_right.value
        when '=' then v_left.value = v_right.value
    end as value

from expressions e
join variables v_left
on v_left.name = e.left_operand
join variables v_right
on v_right.name = e.right_operand
