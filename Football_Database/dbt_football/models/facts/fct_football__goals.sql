


select goal_id, player_id, match_id, time_scored from {{ ref("stg_football__goals") }}
