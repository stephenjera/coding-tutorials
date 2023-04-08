with source as (

    select * from {{ source('football', 'goals') }}

),

renamed as (

    select
        goal_id,
        player_id,
        match_id,
        time_scored

    from source

)

select * from renamed
