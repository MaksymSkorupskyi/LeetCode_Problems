# Create a report comparing
# the number of ride requests to rides completed
# by geographic region and day.
# Rides completed have an associated dropoff.
SELECT
  region,
  ds,
  --  total dropoffs / total ride requests
  AVG(COUNT(IF(dropoff_timestamp IS NOT NULL, 1, 0)) / COUNT(*)) AS dropoff_pct
FROM
  fact_rides
WHERE
  region IS NOT NULL
GROUP BY
  1, 2
;


SELECT
  region,
  day,
  # total_rides_completed
  SUM(COUNT(IF(dropoff_ts IS NOT NULL, 1, 0 )))
  /
  # total_rides_request
  SUM(COUNT(*))       AS dropoff_ratio,
FROM
  fact_rides
GROUP BY
  region,
  day

SELECT
  region,
  day,
  # total_rides_completed / total_rides_request
  AVG(
    COUNT(
      IF(
        dropoff_ts IS NOT NULL,
        1,
        NULL
      )
    )
    /
    COUNT(*)
  )                   AS dropoff_ratio,
FROM
  fact_rides
GROUP BY
  region,
  day

# Lyft solution
SELECT
  region,
  ds,
  --  total dropoffs / total ride requests
  AVG(
    COUNT(
      CASE
        WHEN dropoff_timestamp IS NOT NULL THEN 1
      END
    )
    /
   COUNT(*)
  )         AS dropoff_pct
FROM
 fact_rides
GROUP BY
  1, 2
WHERE
  region IS NOT NULL