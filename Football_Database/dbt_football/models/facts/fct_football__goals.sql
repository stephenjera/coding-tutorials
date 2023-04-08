with
    goals as (select * from {{ ref("stg_football__goals") }}),

    final as (select goal_id, player_id, match_id, time_scored from goals)

select *
from final
