WITH yesterday AS (
    SELECT
        *
    FROM
        joeip0411.host_activity_reduced
    WHERE
        month_start = '2021-01-01'
),
today AS (
    SELECT
        *
    FROM
        joeip0411.daily_web_metrics
    WHERE
        DATE = DATE('2021-01-02')
)
SELECT
    coalesce(y.host, t.host) as host,
    coalesce(y.metric_name, t.metric_name) as metric_name,
    coalesce(
        y.metric_array,
        REPEAT(
        NULL,
        CAST(
            DATE_DIFF('day', DATE('2021-01-01'), t.date) AS INTEGER
        )
        )
    ) || ARRAY[t.metric_value] AS metric_array,
    '2021-01-01' as month_start
FROM
    today t FULL OUTER JOIN yesterday y
    ON y.host = t.host
    AND y.metric_name = t.metric_name
