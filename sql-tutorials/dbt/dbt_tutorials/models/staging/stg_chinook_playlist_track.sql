with source as (
      select * from {{ source('chinook', 'PlaylistTrack') }}
),
renamed as (
    select
        "PlaylistId" as playlist_id,
        "TrackId" as track_id
    from source
)
select * from renamed
  