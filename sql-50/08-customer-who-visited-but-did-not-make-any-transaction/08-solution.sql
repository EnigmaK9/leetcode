/*
This SQL query retrieves the customer IDs of those who visited the mall but did not make any transactions.
It also counts the number of such visits for each customer.
The result is sorted in ascending order by customer_id.
*/

-- Select customer_id and count of visits without transactions
select
    v.customer_id, -- Select customer_id from the visits table
    count(v.visit_id) as count_no_trans -- Count the number of visits with no transactions
from
    visits v -- From the visits table
left join
    transactions t -- Perform a left join with the transactions table
on
    v.visit_id = t.visit_id -- Join condition on visit_id
where
    t.transaction_id is null -- Filter for visits that have no corresponding transaction
group by
    v.customer_id -- Group the result by customer_id
order by
    v.customer_id; -- Sort the result by customer_id in ascending order

