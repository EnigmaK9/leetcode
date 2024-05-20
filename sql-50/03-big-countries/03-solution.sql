-- Select the name, population, and area of countries that meet the criteria for being big
-- A country is considered big if:
-- 1. It has an area of at least three million (3000000 km^2), or
-- 2. It has a population of at least twenty-five million (25000000)

select
    name,            -- Name of the country
    population,      -- Population of the country
    area             -- Area of the country
from
    world            -- The table containing country information
where
    area >= 3000000  -- Condition for being big based on area
    or               -- Logical OR to combine both conditions
    population >= 25000000;  -- Condition for being big based on population

