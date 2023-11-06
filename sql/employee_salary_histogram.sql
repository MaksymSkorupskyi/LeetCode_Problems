# Salary band distribution a.k.a. histogram of the salaries to understand company expenses.
WITH
  cte_salary_band AS (
    SELECT
      FLOOR(salary / 1000)  AS salary_band,
      COUNT(*)              AS employee_count
    FROM
      employee
    GROUP BY
      1
  )

SELECT
  salary_band,
  salary_band / (SELECT COUNT(*) FROM employee) * 100 AS salary_band_percentage
FROM
  cte_salary_band
ORDER BY
  1