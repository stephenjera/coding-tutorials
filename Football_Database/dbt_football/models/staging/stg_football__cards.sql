with source as (

    select * from {{ source('football', 'cards') }}

),

renamed as (

    select
        card_id,
        player_id,
        match_id,
        colour_id,
        time_given

    from source

)

select * from renamed
