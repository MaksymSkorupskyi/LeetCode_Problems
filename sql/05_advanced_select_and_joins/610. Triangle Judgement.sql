-- 610. Triangle Judgement
-- Easy
-- Table: Triangle
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | x           | int  |
-- | y           | int  |
-- | z           | int  |
-- +-------------+------+
-- In SQL, (x, y, z) is the primary key column for this table.
-- Each row of this table contains the lengths of three line segments.
--
-- Report for every three line segments whether they can form a triangle.
-- Return the result table in any order.
--
-- Example 1:
-- Input:
-- Triangle table:
-- +----+----+----+
-- | x  | y  | z  |
-- +----+----+----+
-- | 13 | 15 | 30 |
-- | 10 | 20 | 15 |
-- +----+----+----+
-- Output:
-- +----+----+----+----------+
-- | x  | y  | z  | triangle |
-- +----+----+----+----------+
-- | 13 | 15 | 30 | No       |
-- | 10 | 20 | 15 | Yes      |
-- +----+----+----+----------+

-- Three lines can form a triangle when they satisfy the Triangle Inequality Theorem.
-- This theorem states that for three line segments to create a triangle,
-- the sum of the lengths of any two sides must be greater than the length of the third side.
-- In other words, if you have three line lengths, A, B, and C, they can form a triangle if:
-- A + B > C
-- A + C > B
-- B + C > A
-- If these conditions are met, then the three lines can indeed form a triangle.
-- If any of the conditions is not satisfied, a triangle cannot be formed with those three lines
-- https://www.wikihow.com/Determine-if-Three-Side-Lengths-Are-a-Triangle
-- https://www.ck12.org/book/ck-12-geometry-concepts/section/5.7/
SELECT
  x,
  y,
  z,
  IF(
    x + y > z
    AND x + z > y
    AND y + z > x
    ,
    'Yes',
    'No'
  ) AS triangle
FROM
  Triangle
