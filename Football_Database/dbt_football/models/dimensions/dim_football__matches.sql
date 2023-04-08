with
    -- import CTEs
    clubs as (
        select * from {{ ref("stg_football__clubs") }}
    ),

    venues as (
        select * from {{ ref("stg_football__venues") }}
    ),

    matches as (
        select * from {{ ref("stg_football__matches") }}
    ),

    -- logic CTEs
    points as (
        select
            match_id,
            week,
            date_time,
            club as home_team,
            home_score,
            away_id,
            away_score,
            venue,
            case
                when home_score > away_score
                then 3
                when home_score = away_score
                then 1
                when home_score < away_score
                then 0
                else null
            end as home_points,
            case
                when away_score > home_score
                then 3
                when away_score = home_score
                then 1
                when away_score < home_score
                then 0
                else null
            end as away_points
        from matches
        inner join clubs on home_id = club_id
        inner join venues using (venue_id)
    ),

    final as (
        select
            match_id,
            venue,
            week,
            date_time,
            home_team,
            home_score,
            club as away_team,
            away_score,
            home_points,
            away_points
        from points
        join {{ ref("stg_football__clubs") }} on away_id = club_id
    )
    
select *
from final
