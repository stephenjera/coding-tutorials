with source as (
      select * from {{ source('chinook', 'Album') }}
),
renamed as (
    select
        "AlbumId" as album_id,
        "Title" as title,
        "ArtistId" as artist_id
    from source
)
select * from renamed
  