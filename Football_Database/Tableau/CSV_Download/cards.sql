select
    *
from
    dbt_football_fct.fct_football__cards
    inner join dbt_football_dim.dim_football__players using(player_id)
    inner join dbt_football.dim_football__matches using(match_id)