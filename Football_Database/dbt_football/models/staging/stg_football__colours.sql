with source as (

    select * from {{ source('football', 'colours') }}

),

renamed as (

    select
        colour_id,
        colour

    from source

)

select * from renamed
