select goal_id, player_id, match_id, time_scored from {{ source("football", "goals") }}
