select player_id, group_id, club_id, first_name, last_name
from {{ source("football", "players") }}
