select club_id, club from {{ source("football", "clubs") }}
