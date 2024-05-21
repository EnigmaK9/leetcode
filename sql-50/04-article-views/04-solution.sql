-- Select the distinct author_id as id from the Views table
-- where the author_id is equal to the viewer_id
-- This identifies authors who viewed at least one of their own articles

select
    distinct author_id as id  -- Select distinct author_id and rename it as id
from
    views                    -- The table containing article views
where
    author_id = viewer_id    -- Condition where the author is also the viewer
order by
    id;                      -- Sort the result by id in ascending order

