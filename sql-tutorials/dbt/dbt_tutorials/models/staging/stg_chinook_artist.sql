with source as (
      select * from {{ source('chinook', 'Artist') }}
),
renamed as (
    select
        "ArtistId" as artist_id,
         "Name" as artist_name
    from source
)
select * from renamed
  