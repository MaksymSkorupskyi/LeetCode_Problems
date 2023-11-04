-- 197. Rising Temperature
-- Easy
-- Table: Weather
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the column with unique values for this table.
-- This table contains information about the temperature on a certain day.
--
-- Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
-- Return the result table in any order.
-- The result format is in the following example.
--
-- Example 1:
-- Input:
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Output:
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
-- Explanation:
-- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

-- Example 2:
-- | id | recordDate | temperature |
-- | -- | ---------- | ----------- |
-- | 1  | 2000-12-16 | 3           |
-- | 2  | 2000-12-15 | -1          |
-- Output:
-- | Id |
-- | -- |
-- | 1  |
SELECT
  current_day.id
FROM
  Weather AS current_day
JOIN
  Weather AS previous_day
ON
  current_day.recordDate = previous_day.recordDate + 1
WHERE
  current_day.temperature > previous_day.temperature


SELECT
  weather.id AS 'Id'
FROM
  weather
JOIN
  weather w
ON
  DATEDIFF(weather.recordDate, w.recordDate) = 1 AND weather.Temperature > w.Temperature