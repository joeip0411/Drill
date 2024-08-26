WITH
  prev_day AS (
    SELECT
      *
    FROM
      joeip0411.hosts_cumulated
    WHERE
      DATE = DATE('2021-01-01')
  ),
  today AS (
    SELECT
      host,
      DATE(event_time) AS event_date
    FROM
      bootcamp.web_events
    WHERE
      DATE(event_time) = DATE('2021-01-02')
    GROUP BY
      host,
      DATE(event_time)
  )
SELECT
  COALESCE(p.host, t.host) AS host,
  CASE
    WHEN p.host_activity_datelist IS NOT NULL
    AND t.event_date IS NOT NULL THEN ARRAY[t.event_date] || p.host_activity_datelist
    WHEN p.host_activity_datelist IS NOT NULL THEN p.host_activity_datelist
    WHEN t.event_date IS NOT NULL THEN ARRAY[t.event_date]
  END AS host_activity_datelist,
  DATE('2021-01-02') AS DATE
FROM
  prev_day p
  FULL OUTER JOIN today t ON t.host = p.host