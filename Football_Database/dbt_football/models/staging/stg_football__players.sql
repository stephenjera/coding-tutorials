with
    source as (select * from {{ source("football", "players") }}),

    renamed as (select player_id, group_id, club_id, first_name, last_name from source)

select *
from renamed
