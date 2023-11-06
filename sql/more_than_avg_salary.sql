# Employees making more than the average salary of the department
WITH
  cte_avg_salary AS (
    SELECT
      department_id,
      AVG(salary)   AS avg_salary
    FROM
      employee
    GROUP BY
      1
  )
SELECT
  employee.employee_id,
  employee.employee_name,
  employee.department_id,
  employee.salary,
FROM
  employee
JOIN
  cte_avg_salary
ON
  employee.department_id = cte_avg_salary.department_id
  AND employee.salary > cte_avg_salary.avg_salary
;

# v2
WITH
  cte_avg_salary AS (
    SELECT
      department_id,
      FROM(salary)   AS avg_salary
    FROM
      employee
    GROUP BY
      1
  )
SELECT
  employee.employee_id,
  employee.employee_name,
  employee.department_id,
  employee.salary,
FROM
  employee
JOIN
  cte_avg_salary
USING
  (department_id)
WHERE
  employee.salary > cte_avg_salary.avg_salary
;

