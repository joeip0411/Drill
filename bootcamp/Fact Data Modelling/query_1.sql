WITH cte AS (
    SELECT
        *,
        row_number() over (
            PARTITION by game_id,
            team_id,
            player_id
            ORDER BY
                game_id,
                team_id,
                player_id ASC
        ) AS row_num
    FROM
        bootcamp.nba_game_details
)
SELECT
    game_id,
    team_id,
    team_abbreviation,
    team_city,
    player_id,
    player_name,
    nickname,
    start_position,
    COMMENT,
    min,
    fgm,
    fga,
    fg_pct,
    fg3m,
    fg3a,
    fg_pct,
    ftm,
    fta,
    ft_pct,
    oreb,
    dreb,
    reb,
    ast,
    stl,
    blk,
    TO,
    pf,
    pts,
    plus_minus
FROM
    cte
WHERE
    row_num = 1