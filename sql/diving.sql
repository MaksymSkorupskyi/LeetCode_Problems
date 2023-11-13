-- > DESCRIBE TABLE dives;
-- +----------+---------+
-- | name     | type    |
-- |----------+---------|
-- | person1  | TEXT    |
-- | person2  | TEXT    |
-- | revenue  | NUMERIC |
-- +----------+---------+
--
-- > DESCRIBE TABLE registrations;
-- +----------+---------+
-- | name     | type    |
-- |----------+---------|
-- | person   | TEXT    |
-- | age      | NUMERIC |
-- | city     | TEXT    |
-- +----------+---------+
--
--
-- You also have two demo tables with a tiny amount of data to help you think about the problem.
--
--
-- > SELECT * FROM dives_demo;
-- +---------+---------+---------+
-- | person1 | person2 | revenue |
-- |---------+---------+---------|
-- | Alice   | Bob     | 500     |
-- | Alice   | Calvin  | 100     |
-- | Calvin  | Bob     | 900     |
-- +---------+---------+---------+
--
-- > SELECT * FROM registrations_demo;
-- +--------+-----+------------+
-- | person | age | city       |
-- |--------+-----+------------|
-- | Alice  | 18  | Clownton   |
-- | Bob    | 48  | Sharksburg |
-- | Calvin | 47  | Clownton   |
-- | Debra  | 24  | Sharksburg |
-- +--------+-----+------------+

-- So, is your average revenue per customer highest for people living in Clownton or Sharksburg?
-- People on the same dive split the price equally.
-- It’s easy enough to see that in this sample Clownton wins with $400 average revenue per registration
-- over Sharksburg’s $350. But what about the full dataset?
-- After a moment’s thought you execute the following query to get the results:
WITH
  cte_person_revenue AS (
    SELECT
      person1       AS person,
      revenue / 2   AS revenue
    FROM
      dives_demo
    UNION ALL
    SELECT
      person2       AS person,
      revenue / 2   AS revenue
    FROM
      dives_demo
  ),

  cte_revenue_aggregated AS (
    SELECT
      person,
      SUM(revenue)   AS revenue
    FROM
      cte_person_revenue
    GROUP BY
      1

  )

SELECT
  city,
  AVG(revenue) AS revenue
FROM
  registrations_demo
LEFT JOIN
  cte_revenue_aggregated
USING
  (person)
GROUP BY
  1
