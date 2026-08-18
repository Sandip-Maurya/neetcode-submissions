-- Write your query below


select u.name as name, 
    sum(t.amount) as balance
from users u
join transactions t on t.account = u.account
group by u.name
having sum(t.amount) > 10000;

