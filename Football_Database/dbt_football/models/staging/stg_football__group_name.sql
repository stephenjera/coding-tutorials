with
    source as (select * from {{ source("football", "group_name") }}),

    renamed as (select group_id, group_name from source)

select *
from renamed
