/*markdown
1. Listing all students, who play for a particular department (i.e. Cohort 4 group).
*/

select  first_name, last_name, group_name
from players
    join group_name using(group_id)
where group_name = 'Cohort 4'

/*markdown
2. Listing all fixtures for a specific date (i.e. 29th of October 2022).
*/

create or replace view fixtures as 
    with t1 as (
        select  week, date_time, club as home_team,  
                away_id, venue, friendly
        from matches
            join clubs on home_id = club_id
            join venues on matches.venue_id = venues.venue_id
        ),
        t2 as (
            select  week, date_time, home_team, club as away_team, venue, friendly
            from t1
                join clubs on away_id = club_id
        )
        select * from t2

select week, date_time, home_team, away_team, venue
from fixtures
where date_time::date = '2022-10-01';

/*markdown
3. Listing all the players who have scored more than 2 goals.
*/

select first_name, last_name, goals
from
    (
        select first_name, last_name, count(*) as goals
        from players
            join goals using(player_id)
        group by first_name, last_name
    ) total_goals
where goals > 2

select  sum(goals) as total_season_goals
from
    (
        select first_name, last_name, count(*) as goals
        from players
            join goals using(player_id)
            join matches using(match_id)
        where date_time::date >= '2022-10-01' 
              and   date_time::date <  '2023-10-01'
        group by first_name, last_name
    ) total_goals

/*markdown
5. Return the number of goals in favour, goals against, goals difference and point
*/

create or replace view score_board as 
    with t1 as (
        select  week, date_time, club as home_team, home_score, 
                away_id, away_score,
                case 
                    when home_score > away_score then 3
                    when home_score = away_score then 1
                    when home_score < away_score then 0
                    else null 
                end as home_points, 
                case 
                    when away_score > home_score then 3
                    when away_score = home_score then 1
                    when away_score < home_score then 0
                    else null 
                end as away_points
    from matches
        join clubs on home_id = club_id
        join venues on matches.venue_id = venues.venue_id
    where friendly = false
    ),
    t2 as (
        select  week, date_time, home_team, home_score, 
            club as away_team, away_score, home_points, away_points
        from t1
            join clubs on away_id = club_id
    )
    select * from t2;

select * from score_board

-- Calculate goals and points for when same team is playing home and away
create or replace view results_analysis as 
       with t1 as(
       select home_team, sum(home_score) as goals_for, sum(away_score) as goals_against,
              sum(home_points) as points 
       from score_board
       group by home_team
       union all
       select away_team, sum(away_score) as goals_for, sum(home_score) as goals_against,
              sum(away_points) as points
       from score_board
       group by away_team
       ),
       t2 as (
       select home_team as club, sum(goals_for) as goals_for, sum(goals_against) as goals_against,
              sum(points) as points
       from t1
       group by home_team
       )
       select club, points, goals_for, goals_against,
              (goals_for - goals_against) as goal_differnece
       from t2

select * 
from results_analysis
order by points desc;

/*markdown
6. Listing the number of cards (yellow and red) per team.
*/

select club, colour, count(*) as num_cards
from cards
    join colours using(colour_id)
    join players using(player_id)
    join clubs using (club_id)
group by club, colour
order by club 

select date_time, home_team, away_team, venue
from fixtures
where friendly = true;

/*markdown
8. Develop a store procedure to add new players. It needs to consider warnings
and exceptions.
*/

create or replace procedure add_player(
    _group_id smallint,
    _club_id smallint, 
    _first_name text,
    _last_name text
)
language plpgsql    
as $BODY$
begin
        -- add player to players
        insert into players(group_id, club_id, first_name, last_name)
        values(_group_id, _club_id, _first_name, _last_name);
end;
$BODY$

call add_player('1', '1', 'pen', 'pax')

SELECT * FROM PLAYERS
order by player_id desc