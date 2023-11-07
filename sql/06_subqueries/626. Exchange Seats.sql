-- 626. Exchange Seats
-- Medium
-- Table: Seat
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | student     | varchar |
-- +-------------+---------+
-- id is the primary key (unique value) column for this table.
-- Each row of this table indicates the name and the ID of a student.
-- id is a continuous increment.
--
-- Write a solution to swap the seat id of every two consecutive students.
-- If the number of students is odd, the id of the last student is not swapped.
-- Return the result table ordered by id in ascending order.
--
-- Example 1:
-- Input:
-- Seat table:
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Abbot   |
-- | 2  | Doris   |
-- | 3  | Emerson |
-- | 4  | Green   |
-- | 5  | Jeames  |
-- +----+---------+
-- Output:
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Doris   |
-- | 2  | Abbot   |
-- | 3  | Green   |
-- | 4  | Emerson |
-- | 5  | Jeames  |
-- +----+---------+
-- Explanation:
-- Note that if the number of students is odd, there is no need to change the last one's seat.

-- | id | student | LEAD(student) OVER () | LAG(student) OVER() |
-- | -- | ------- | --------------------- | ------------------- |
-- | 1  | Abbot   | Doris                 | null                |
-- | 2  | Doris   | Emerson               | Abbot               |
-- | 3  | Emerson | Green                 | Doris               |
-- | 4  | Green   | Jeames                | Emerson             |
-- | 5  | Jeames  | null                  | Green               |
SELECT
  id,
  IFNULL(
    IF(
      MOD(id, 2) = 0,
      LAG(student) OVER(),  # even id
      LEAD(student) OVER () # odd id
    ),
    student
  )         AS student
FROM
  Seat
ORDER BY
  1
