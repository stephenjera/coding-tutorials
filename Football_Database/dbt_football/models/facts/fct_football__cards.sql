with

    -- import CTEs
    cards as (select * from {{ ref("stg_football__cards") }}),
    colours as (select * from {{ ref("stg_football__colours") }}),

    -- logic CTEs
    final as (
        select card_id, player_id, match_id, colour, time_given
        from cards
        join colours using (colour_id)
    )

select *
from final
