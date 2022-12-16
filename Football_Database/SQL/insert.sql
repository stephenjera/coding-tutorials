/*markdown
Group name
*/

COPY group_name(group_name)
FROM 'C:\Users\StephenJeranyama\OneDrive - Harnham Search and Selection Ltd\Documents\Work\Bench_Projects\Football_database_2\Tables\Groups.csv'
DELIMITER ','
CSV HEADER;

select * from group_name

/*markdown
Clubs
*/

COPY clubs(club)
FROM 'C:\Users\StephenJeranyama\OneDrive - Harnham Search and Selection Ltd\Documents\Work\Bench_Projects\Football_database_2\Tables\Clubs.csv'
DELIMITER ','
CSV HEADER;

select * from clubs

/*markdown
Players
*/

delete from players;
ALTER SEQUENCE players_player_id_seq RESTART WITH 1;
COPY players(first_name, last_name, group_id, club_id)
FROM 'C:\Users\StephenJeranyama\OneDrive - Harnham Search and Selection Ltd\Documents\Work\Bench_Projects\Football_database_2\Tables\Players.csv'
DELIMITER ','
CSV HEADER;

select * from players

/*markdown
Venues
*/

COPY venues(venue)
FROM 'C:\Users\StephenJeranyama\OneDrive - Harnham Search and Selection Ltd\Documents\Work\Bench_Projects\Football_database_2\Tables\Venues.csv'
DELIMITER ','
CSV HEADER;

select * from venues

/*markdown
Matches 
*/

delete from matches;
ALTER SEQUENCE matches_match_id_seq RESTART WITH 1;
COPY matches(home_id, away_id, venue_id, date_time, week, friendly, home_score, away_score)
FROM 'C:\Users\StephenJeranyama\OneDrive - Harnham Search and Selection Ltd\Documents\Work\Bench_Projects\Football_database_2\Tables\Matches.csv'
DELIMITER ','
CSV HEADER;

select * from matches

/*markdown
Colours
*/

delete from colours;
ALTER SEQUENCE colours_colour_id_seq RESTART WITH 1;
COPY colours(colour)
FROM 'C:\Users\StephenJeranyama\OneDrive - Harnham Search and Selection Ltd\Documents\Work\Bench_Projects\Football_database_2\Tables\Colours.csv'
DELIMITER ','
CSV HEADER;

select * from colours

/*markdown
Cards
*/

delete from cards;
ALTER SEQUENCE cards_card_id_seq RESTART WITH 1;
COPY cards(player_id, match_id, time_given, colour_id)
FROM 'C:\Users\StephenJeranyama\OneDrive - Harnham Search and Selection Ltd\Documents\Work\Bench_Projects\Football_database_2\Tables\Cards.csv'
DELIMITER ','
CSV HEADER;

select * from cards

/*markdown
Goals
*/

delete from goals;
ALTER SEQUENCE goals_goal_id_seq RESTART WITH 1;
COPY goals(player_id, match_id, time_scored)
FROM 'C:\Users\StephenJeranyama\OneDrive - Harnham Search and Selection Ltd\Documents\Work\Bench_Projects\Football_database_2\Tables\Goals.csv'
DELIMITER ','
CSV HEADER;

select * from goals