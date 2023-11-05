-- 550. Game Play Analysis IV
-- Medium
-- Table: Activity
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | player_id    | int     |
-- | device_id    | int     |
-- | event_date   | date    |
-- | games_played | int     |
-- +--------------+---------+
-- (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
-- This table shows the activity of players of some games.
-- Each row is a record of a player who logged in and played a number of games (possibly 0)
-- before logging out on someday using some device.
--
-- Write a solution to report the fraction of players
-- that logged in again on the day after the day they first logged in,
-- rounded to 2 decimal places.
-- In other words, you need to count the number of players that logged in for at least two consecutive days
-- starting from their first login date, then divide that number by the total number of players.
--
-- The result format is in the following example.
--
-- Example 1:
-- Input:
-- Activity table:
-- +-----------+-----------+------------+--------------+
-- | player_id | device_id | event_date | games_played |
-- +-----------+-----------+------------+--------------+
-- | 1         | 2         | 2016-03-01 | 5            |
-- | 1         | 2         | 2016-03-02 | 6            |
-- | 2         | 3         | 2017-06-25 | 1            |
-- | 3         | 1         | 2016-03-02 | 0            |
-- | 3         | 4         | 2018-07-03 | 5            |
-- +-----------+-----------+------------+--------------+
-- Output:
-- +-----------+
-- | fraction  |
-- +-----------+
-- | 0.33      |
-- +-----------+
-- Explanation:
-- Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33
WITH
  cte_first_login AS (
    SELECT
      player_id,
      event_date,
      ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn
    FROM
      Activity
  )

SELECT
  ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2)  AS fraction
FROM
  cte_first_login AS first_login
JOIN
  Activity
ON
  first_login.player_id = Activity.player_id
  AND first_login.event_date = DATE_SUB(Activity.event_date, INTERVAL 1 DAY)
WHERE
  first_login.rn = 1
;


# Editorial Solution
SELECT
  ROUND(
    COUNT(A1.player_id)
    / (SELECT COUNT(DISTINCT A3.player_id) FROM Activity A3)
  , 2) AS fraction
FROM
  Activity A1
WHERE
  (A1.player_id, DATE_SUB(A1.event_date, INTERVAL 1 DAY)) IN (
    SELECT
      A2.player_id,
      MIN(A2.event_date)
    FROM
      Activity A2
    GROUP BY
      A2.player_id
  );