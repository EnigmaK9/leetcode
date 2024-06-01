select
    w1.id
from
    weather w1
join
    weather w2
on
    date_sub(w1.recorddate, interval 1 day) = w2.recorddate
where
    w1.temperature > w2.temperature;

