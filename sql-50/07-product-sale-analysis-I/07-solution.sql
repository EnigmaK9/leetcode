-- Select the product name, year, and price for each sale from the Sales table
-- Join the Sales table with the Product table to get the product name

select
    p.product_name,  -- Select the product name from the Product table
    s.year,          -- Select the year from the Sales table
    s.price          -- Select the price from the Sales table
from
    sales s          -- The table containing sales information
join
    product p        -- The table containing product information
on
    s.product_id = p.product_id;  -- Join condition to match product IDs

