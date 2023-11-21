SELECT
  client_id,
  DATE(Timestamp)   AS date,
  SUM(page_views)   AS page_views
#   ROW_NUMBER() OVER (PARTITION BY DATE(Timestamp) ORDER BY DATE(Timestamp))
FROM
  table
GROUP BY
  client_id,
  DATE(Timestamp)


WITH
  cte_url_views AS (
  SELECT
    client_id,
    url,
    SUM(page_views) AS page_views,
    ROW_NUMBER() OVER ( PARTITION BY client_id, url ORDER page_views DESC) AS rn
  FROM
    table
  GROUP BY
    1,
    2
  )

SELECT
  client_id,
  URL
FROM
  cte_url_views
WHERE
  rn = 1


SELECT
  client_id,
  MAX(URL)  AS url
FROM
  cte_url_views
GROUP BY
  1



# WHERE
#   page_views = SELECT(MAX(page_views) FROM cte_url_views)

SELECT
  client_id,
  SUM(page_views)
FROM
  table
GROUP BY
  client


cl1, url1, 3
cl1, url2, 2