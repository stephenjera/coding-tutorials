select
    match_id,
    home_id,
    away_id,
    venue_id,
    date_time,
    week,
    friendly bool,
    home_score,
    away_score
from {{ source("football", "matches") }}
