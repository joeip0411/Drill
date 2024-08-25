SELECT
    e.user_id,
    d.browser_type,
    date(e.event_time) AS event_date
FROM
    bootcamp.web_events e
    JOIN bootcamp.devices d ON e.device_id = d.device_id
LIMIT
    10