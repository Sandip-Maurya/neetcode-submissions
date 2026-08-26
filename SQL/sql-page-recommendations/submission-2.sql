-- Write your query below
with user_one_friends as 
    (select 
        case when user1_id = 1 then user1_id
            when user2_id = 1 then user2_id
        end as user_one,
        case when user1_id = 1 then user2_id
            when user2_id = 1 then user1_id
        end as friend 
    from friendship
    where user1_id = 1 OR user2_id = 1
    )

select distinct l.page_id as recommended_page from user_one_friends uf
join likes l on l.user_id = uf.friend 
where l.page_id not in (
    select page_id from likes where user_id = 1
)