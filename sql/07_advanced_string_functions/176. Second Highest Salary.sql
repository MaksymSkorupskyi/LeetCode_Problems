-- 176. Second Highest Salary
-- Medium
-- Table: Employee
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- id is the primary key (column with unique values) for this table.
-- Each row of this table contains information about the salary of an employee.
--
-- Write a solution to find the second highest salary from the Employee table.
-- If there is no second highest salary, return null (return None in Pandas).
--
-- Example 1:
-- Input:
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- Output:
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+
--
-- Example 2:
-- Input:
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- +----+--------+
-- Output:
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | null                |
-- +---------------------+
# v1 DENSE_RANK()
WITH
  cte_salary_rank AS (
    SELECT
      salary,
      DENSE_RANK() OVER (ORDER BY salary DESC)  AS salary_rank
    FROM
      Employee
  )
SELECT
  IF(
    COUNT(*) > 1,
    (
      SELECT
        MAX(salary)
      FROM
        cte_salary_rank
      WHERE
        salary_rank = 2
    ),
    NULL
  ) AS SecondHighestSalary
FROM
  Employee
;

# v1.1 DENSE_RANK()
WITH
  cte_salary_rank AS (
    SELECT
      salary,
      DENSE_RANK() OVER (ORDER BY salary DESC)  AS salary_rank
    FROM
      Employee
  )
SELECT (
  SELECT
    MAX(salary)
  FROM
    cte_salary_rank
  WHERE
    salary_rank = 2
  ) AS SecondHighestSalary
;

# v2
SELECT (
  SELECT
    salary
  FROM
    Employee
  ORDER BY
    salary DESC
  LIMIT
    1
  OFFSET
    1
) AS SecondHighestSalary
;

# v3
SELECT
  MAX(salary) AS SecondHighestSalary
FROM
  Employee
WHERE
  salary < (SELECT MAX(salary) FROM Employee)
;
