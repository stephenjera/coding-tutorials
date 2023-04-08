with
    source as (select * from {{ source("football", "clubs") }}),

    renamed as (select club_id, club from source)

select *
from renamed
