with 

-- import CTEs
players as (
    select * from {{ ref("stg_football__players") }}
    ),

clubs as (
    select * from {{ ref("stg_football__clubs") }}
),

group_name as (
    select * from {{ ref("stg_football__group_name") }}
),

-- Logic CTEs
final as (
    select player_id, first_name, last_name, club, group_name
from players
inner join clubs using (club_id)
inner join group_name using (group_id)
)

select * from final

