# Highest salaried employee from each department
WITH
  cte_max_salary AS (
    SELECT
      department_id,
      MAX(salary)   AS max_salary
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
  cte_max_salary
ON
  employee.department_id = cte_max_salary.department_id
  AND employee.salary = cte_max_salary.max_salary
;

# v2
WITH
  cte_max_salary AS (
    SELECT
      department_id,
      MAX(salary)   AS max_salary
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
  cte_max_salary
USING
  (department_id)
WHERE
  employee.salary = cte_max_salary.max_salary
;

