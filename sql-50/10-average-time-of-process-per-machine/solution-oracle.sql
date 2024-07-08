with process_times as (
    select
        machine_id,
        process_id,
        max(case when activity_type = 'end' then timestamp end) -
        max(case when activity_type = 'start' then timestamp end) as process_time
    from activity
    group by machine_id, process_id
)

select
    machine_id,
    round(avg(process_time), 3) as processing_time
from process_times
group by machine_id;

