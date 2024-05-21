-- Select the name and the unique_id of each employee
-- If the employee does not have a unique_id, show null

select
    e.name,                        -- Select the employee's name
    eu.unique_id                   -- Select the employee's unique_id
from
    employees e                    -- The table containing employee information
left join
    employeeuni eu                 -- The table containing employee unique IDs
on
    e.id = eu.id;                  -- Join condition to match employee IDs

