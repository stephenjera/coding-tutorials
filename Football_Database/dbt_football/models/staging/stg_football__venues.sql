with
    source as (select * from {{ source("football", "venues") }}),

    renamed as (select venue_id, venue from source)

select *
from renamed
