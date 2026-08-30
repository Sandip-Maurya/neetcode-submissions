
SELECT distinct l1.account_id as account_id
FROM log_info l1 
JOIN log_info l2 
    ON l1.account_id = l2.account_id 
WHERE l1.ip_address != l2.ip_address
and (l2.login between l1.login and l1.logout)
;