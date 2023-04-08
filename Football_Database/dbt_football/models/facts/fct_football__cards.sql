with

    -- import CTEs
    cards as (select * from {{ ref("stg_football__cards") }}),
    players as (select * from {{ ref("stg_football__players") }}),
    matches as (select * from {{ ref("stg_football__matches") }}),
    clubs as (select * from {{ ref("stg_football__clubs") }}),
    colours as (select * from {{ ref("stg_football__colours") }}),

    -- logic CTEs
    final as (
        select card_id, player_id, match_id, colour, time_given
        from cards
        join players using (player_id)
        join matches using (match_id)
        join colours using (colour_id)
    )

select *
from final
