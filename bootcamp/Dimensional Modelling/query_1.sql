CREATE TABLE joeip0411.actors (
    actor VARCHAR,
    actor_id VARCHAR,
    films ARRAY(
        ROW(
            film VARCHAR,
            votes INTEGER,
            rating DOUBLE,
            film_id VARCHAR
        )
    ),
    quality_class VARCHAR,
    is_active BOOLEAN,
    current_year INTEGER
)