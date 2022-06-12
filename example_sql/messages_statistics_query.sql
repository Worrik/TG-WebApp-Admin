select 
    x.count_messages + coalesce(sum(y.count_messages), 0)
        as "count",
    x.date as "category"
from (
    select date("time") as "date", count(*) as count_messages
    from messages as m
    group by "date"
    order by "date" desc
) x
left outer join
(
    select date("time") as "date", count(*) as count_messages
    from messages as m
    group by "date"
    order by "date" desc
) y on y.date < x.date
group by x.date, x.count_messages
order by x.date desc
limit 14;
