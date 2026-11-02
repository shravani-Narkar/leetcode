SELECT player_id, MIN(event_date) as first_login
FROM (
    SELECT player_id, event_date,
    DENSE_RANK() OVER (PARTITION BY player_id ORDER BY event_date) rn
    FROM Activity
)t
GROUP BY player_id