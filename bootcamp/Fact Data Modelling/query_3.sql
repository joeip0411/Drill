WITH
  prev_day AS (
    SELECT
      *
    FROM
      joeip0411.user_devices_cumulated
    WHERE
      DATE = DATE('2021-01-01')
  ),
  today AS (
    SELECT
      E.user_id,
      d.browser_type,
      DATE(E.event_time) AS event_date
    FROM
      bootcamp.web_events E
      JOIN bootcamp.devices d ON E.device_id = d.device_id
    WHERE
      DATE(E.event_time) = DATE('2021-01-02')
    GROUP BY
      E.user_id,
      d.browser_type,
      DATE(E.event_time)
  )
SELECT
  COALESCE(p.user_id, t.user_id) AS user_id,
  COALESCE(p.browser_type, t.browser_type) AS browser_type,
  CASE
    WHEN p.dates_active IS NOT NULL
    AND t.event_date IS NOT NULL THEN ARRAY[t.event_date] || p.dates_active
    WHEN p.dates_active IS NOT NULL THEN p.dates_active
    WHEN t.event_date IS NOT NULL THEN ARRAY[t.event_date]
  END AS dates_active,
  DATE('2021-01-02') AS DATE
FROM
  prev_day p
  FULL OUTER JOIN today t ON t.user_id = p.user_id
  AND t.browser_type = p.browser_type