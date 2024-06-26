with source as (
      select * from {{ source('chinook', 'MediaType') }}
),
renamed as (
    select
        "MediaTypeId" as media_type_id,
        "Name" as media_type_name
    from source
)
select * from renamed
  