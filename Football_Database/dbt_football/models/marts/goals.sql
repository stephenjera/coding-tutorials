select
    g.*
    {{ dbt_utils.star(from=ref("dim_football__players"), except=["player_id"]) }},
    {{ dbt_utils.star(from=ref("dim_football__matches"), except=["match_id"]) }}
from {{ ref("fct_football__goals") }} as g
inner join {{ ref("dim_football__players") }} as p on p.player_id = g.player_id
inner join {{ ref("dim_football__matches") }} as m on m.match_id = g.match_id
