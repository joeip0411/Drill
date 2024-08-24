WITH last_year AS (
    SELECT
        *
    FROM
        joeip0411.actors
    WHERE
        current_year = 1913
),
this_year AS (
    SELECT
        actor,
        actor_id,
        ARRAY_AGG(
            ROW(
                film,
                votes,
                rating,
                film_id
            )
        ) films,
        CASE
            WHEN AVG(rating) > 8 THEN 'star'
            WHEN AVG(rating) > 7
            AND AVG(rating) <= 8 THEN 'good'
            WHEN AVG(rating) > 6
            AND AVG(rating) <= 7 THEN 'average'
            ELSE 'bad'
        END AS quality_class,
        TRUE AS is_active,
        YEAR AS current_year
    FROM
        bootcamp.actor_films
    WHERE
        YEAR = 1914
    GROUP BY
        actor,
        actor_id,
        YEAR
)
SELECT
    COALESCE(
        ls.actor,
        ts.actor
    ) actor,
    COALESCE(
        ls.actor_id,
        ts.actor_id
    ) actor_id,
    CASE
        WHEN ts.films IS NULL THEN ls.films
        WHEN ts.films IS NOT NULL
        AND ls.films IS NULL THEN ts.films
        WHEN ts.films IS NOT NULL
        AND ls.films IS NOT NULL THEN ts.films || ls.films
    END films,
    CASE
        WHEN ts.quality_class IS NOT NULL THEN ts.quality_class
        ELSE ls.quality_class
    END quality_class,
    CASE
        WHEN ts.is_active THEN TRUE
        ELSE FALSE
    END is_active,
    COALESCE(
        ts.current_year,
        ls.current_year + 1
    ) AS current_year
FROM
    last_year ls full
    OUTER JOIN this_year ts
    ON ls.actor_id = ts.actor_id
