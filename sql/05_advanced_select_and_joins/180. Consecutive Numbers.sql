-- 180. Consecutive Numbers
-- Medium
-- Table: Logs
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- In SQL, id is the primary key for this table.
-- id is an autoincrement column.
--
-- Find all numbers that appear at least three times consecutively.
-- Return the result table in any order.
--
-- Example 1:
-- Input:
-- Logs table:
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+
-- Output:
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- Explanation: 1 is the only number that appears consecutively for at least three times.
# v1 LEAD()
WITH
  cte_sequence AS (
    SELECT
      num,
      num = LEAD(num, 1) OVER() AND num = LEAD(num, 2) OVER() AS is_consecutive
    FROM
      Logs
  )

SELECT
  DISTINCT num  AS ConsecutiveNums
FROM
  cte_sequence
WHERE
  is_consecutive IS TRUE
;


# v2 LEAD() + LAG()
SELECT
  DISTINCT num
FROM
  (
    SELECT
      num,
      LEAD(num) OVER (ORDER BY id) AS lead,
      LAG(num) OVER (ORDER BY id) AS lag
   FROM
     cons_test
  )
WHERE
  num = lead
  AND num = lag
;