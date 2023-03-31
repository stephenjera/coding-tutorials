select player_id, first_name, last_name, club, group_name
from {{ ref("stg_football__players") }}
inner join {{ ref("stg_football__clubs") }} using (club_id) as c
inner join {{ ref("stg_football__group_name") }} using (group_id) as g
