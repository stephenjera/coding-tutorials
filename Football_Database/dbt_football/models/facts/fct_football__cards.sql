select card_id, player_id, match_id, colour, time_given
from {{ ref("stg_football__cards") }}
join {{ ref("stg_football__players") }} using (player_id)
join {{ ref("stg_football__matches") }} using (match_id)
join {{ ref("stg_football__colours") }} using (colour_id)
