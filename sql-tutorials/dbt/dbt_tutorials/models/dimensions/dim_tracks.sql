with track as (
    select * from {{ ref('stg_chinook_track') }}
),
genre as (
    select * from {{ ref('stg_chinook_genre') }}
),
media_type as (
    select * from {{ ref('stg_chinook_media_type') }}
),
album as (
    select * from {{ ref('stg_chinook_album') }}
),
artist as (
    select * from {{ ref('stg_chinook_artist') }}
),
final as (
    select
        track_id,
        track_name,
        composer,
        unit_price,
        genre_name,
        media_type_name,
        title,
        artist_name
    from track
        join genre on track.genre_id = genre.genre_id
        join media_type on track.media_type_id = media_type.media_type_id
        join album on track.album_id = album.album_id
        join artist on album.artist_id = artist.artist_id
)

select * from final