WITH
  today AS (
    SELECT
      *
    FROM
      joeip0411.user_devices_cumulated
    WHERE
      DATE = DATE('2021-01-04')
  )
SELECT
  user_id,
  browser_type,
  cast(
    SUM(
      CASE
        WHEN CONTAINS(dates_active, sequence_date) THEN pow(2, 31 - date_diff('day', sequence_date, DATE))
        ELSE 0
      END
    ) AS bigint
  ) history_int
FROM
  today
  CROSS JOIN UNNEST (
    SEQUENCE(
      DATE('2021-01-04') - INTERVAL '6' DAY,
      DATE('2021-01-04')
    )
  ) AS t (sequence_date)
GROUP BY
  user_id,
  browser_type