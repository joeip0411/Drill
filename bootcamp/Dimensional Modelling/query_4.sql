WITH
  lagged AS (
    SELECT
      actor,
      actor_id,
      lag(quality_class) OVER (
        PARTITION BY
          actor_id
        ORDER BY
          current_year ASC
      ) AS prev_class,
      quality_class AS this_class,
      lag(is_active) OVER (
        PARTITION BY
          actor_id
        ORDER BY
          current_year ASC
      ) AS prev_active,
      is_active AS this_active,
      current_year
    FROM
      joeip0411.actors
    WHERE
	    current_year <= 2021
  ),
  changed AS (
    SELECT
      *,
      CASE
        WHEN prev_class != this_class
        OR prev_active != this_active THEN 1
        ELSE 0
      END AS has_changed
    FROM
      lagged
  ),
  streak AS (
    SELECT
      *,
      sum(has_changed) OVER (
        PARTITION BY
          actor_id
        ORDER BY
          current_year ASC
      ) AS streak_id
    FROM
      changed
  )
SELECT
  actor_id,
  actor,
  this_class as quality_class,
  this_active as is_active,
  min(current_year) as start_date,
  max(current_year) as end_date
FROM
  streak
GROUP BY
  actor,
  actor_id,
  streak_id,
  this_active,
  this_class