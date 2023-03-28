select venue_id, venue from {{ source("football", "venues") }}
