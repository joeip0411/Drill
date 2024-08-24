WITH
  prev_scd AS (
    SELECT
      *
    FROM
      joeip0411.actors_history_scd
    WHERE
      end_date <= 1915
  ),
  this_scd AS (
    SELECT
      *
    FROM
      joeip0411.actors
    WHERE
      current_year = 1916
  ),
  combined AS (
    SELECT
      coalesce(p.actor_id, t.actor_id) actor_id,
      coalesce(p.actor, t.actor) actor,
      coalesce(p.start_date, t.current_year) AS start_date,
      coalesce(p.end_date, t.current_year) AS end_date,
      CASE
        WHEN p.is_active != t.is_active
        OR p.quality_class != t.quality_class THEN 1
        WHEN p.is_active = t.is_active
        AND p.quality_class = t.quality_class THEN 0
      END AS changed,
      p.is_active AS prev_active,
      t.is_active AS this_active,
      p.quality_class AS prev_class,
      t.quality_class AS this_class,
      t.current_year
    FROM
      prev_scd p
      FULL OUTER JOIN this_scd t ON p.actor_id = t.actor_id
      AND p.end_date + 1 = t.current_year
  ),
  changed AS (
    SELECT
      actor_id,
      actor,
      CASE
        WHEN changed = 0 THEN ARRAY[
          cast(
            row(prev_active, prev_class, start_date, end_date + 1) AS row(
              is_active boolean,
              quality_class varchar,
              start_date integer,
              end_date integer
            )
          )
        ]
        WHEN changed IS NULL THEN ARRAY[
          cast(
            row(
              coalesce(prev_active, this_active),
              coalesce(prev_class, this_class),
              coalesce(start_date, current_year),
              coalesce(end_date, current_year)
            ) AS row(
              is_active boolean,
              quality_class varchar,
              start_date integer,
              end_date integer
            )
          )
        ]
        WHEN changed = 1 THEN ARRAY[
          cast(
            row(prev_active, prev_class, start_date, end_date) AS row(
              is_active boolean,
              quality_class varchar,
              start_date integer,
              end_date integer
            )
          ),
          cast(
            row(
              this_active,
              this_class,
              current_year,
              current_year
            ) AS row(
              is_active boolean,
              quality_class varchar,
              start_date integer,
              end_date integer
            )
          )
        ]
      END AS change_array
    FROM
      combined
  )
SELECT
  actor_id,
  actor,
  arr.quality_class,
  arr.is_active,
  arr.start_date,
  arr.end_date
FROM
  changed
  CROSS JOIN UNNEST (change_array) AS arr