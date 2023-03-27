select card_id, player_id, match_id, colour_id, time_given
from {{ source("football", "cards") }}
