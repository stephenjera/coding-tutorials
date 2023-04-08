with source as (

    select * from {{ source('football', 'matches') }}

),

renamed as (

    select
        match_id,
        home_id,
        away_id,
        venue_id,
        date_time,
        week,
        friendly,
        home_score,
        away_score

    from source

)

select * from renamed
