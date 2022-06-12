select "id", "user_id", "username", "subscribed", "banned", date("created_at") from users
order by %s
limit ($1::int) offset ($2::int)
