select colour_id, colour from {{ source("football", "colours") }}
