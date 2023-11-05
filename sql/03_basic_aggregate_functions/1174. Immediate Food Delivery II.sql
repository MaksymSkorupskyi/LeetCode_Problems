-- 1174. Immediate Food Delivery II
-- Medium
-- Table: Delivery
-- +-----------------------------+---------+
-- | Column Name                 | Type    |
-- +-----------------------------+---------+
-- | delivery_id                 | int     |
-- | customer_id                 | int     |
-- | order_date                  | date    |
-- | customer_pref_delivery_date | date    |
-- +-----------------------------+---------+
-- delivery_id is the column of unique values of this table.
-- The table holds information about food delivery to customers
-- that make orders at some date and specify a preferred delivery date (on the same order date or after it).
--
-- If the customer's preferred delivery date is the same as the order date, then the order is called immediate;
-- otherwise, it is called scheduled.
--
-- The first order of a customer is the order with the earliest order date that the customer made.
-- It is guaranteed that a customer has precisely one first order.
--
-- Write a solution to find the percentage of immediate orders in the first orders of all customers,
-- rounded to 2 decimal places.
-- The result format is in the following example.
--
-- Example 1:
-- Input:
-- Delivery table:
-- +-------------+-------------+------------+-----------------------------+
-- | delivery_id | customer_id | order_date | customer_pref_delivery_date |
-- +-------------+-------------+------------+-----------------------------+
-- | 1           | 1           | 2019-08-01 | 2019-08-02                  |
-- | 2           | 2           | 2019-08-02 | 2019-08-02                  |
-- | 3           | 1           | 2019-08-11 | 2019-08-12                  |
-- | 4           | 3           | 2019-08-24 | 2019-08-24                  |
-- | 5           | 3           | 2019-08-21 | 2019-08-22                  |
-- | 6           | 2           | 2019-08-11 | 2019-08-13                  |
-- | 7           | 4           | 2019-08-09 | 2019-08-09                  |
-- +-------------+-------------+------------+-----------------------------+
-- Output:
-- +----------------------+
-- | immediate_percentage |
-- +----------------------+
-- | 50.00                |
-- +----------------------+
-- Explanation:
-- The customer id 1 has a first order with delivery id 1 and it is scheduled.
-- The customer id 2 has a first order with delivery id 2 and it is immediate.
-- The customer id 3 has a first order with delivery id 5 and it is scheduled.
-- The customer id 4 has a first order with delivery id 7 and it is immediate.
-- Hence, half the customers have immediate first orders.

-- | customer_id | order_date | customer_pref_delivery_date | rn |
-- | ----------- | ---------- | --------------------------- | -- |
-- | 2           | 2019-08-02 | 2019-08-02                  | 1  |
-- | 4           | 2019-08-09 | 2019-08-09                  | 1  |
WITH
  cte_first_orders AS (
    SELECT
      customer_id,
      order_date,
      customer_pref_delivery_date,
      ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM
      Delivery
  ),

  cte_immediate_first_orders AS (
    SELECT
      *
    FROM
      cte_first_orders
    WHERE
      rn = 1
  )

SELECT
  ROUND(COUNT(*) / (SELECT COUNT(*) FROM cte_immediate_first_orders) * 100, 2)  AS immediate_percentage
FROM
  cte_immediate_first_orders
WHERE
  order_date = customer_pref_delivery_date
;


-- himanshu__mehra__ solition
SELECT
  ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM
  Delivery
WHERE
  (customer_id, order_date) IN (
    SELECT
      customer_id, MIN(order_date)
    FROM
      Delivery
    GROUP BY
      customer_id
  );