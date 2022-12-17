--\connect Football_db 
-- \c "host=localhost port=5432 dbname=Football_db connect_timeout=10"
set datestyle to SQL,DMY;

COPY group_name(group_name)
FROM '/var/lib/postgresql/data/Tables/Groups.csv'
DELIMITER ','
CSV HEADER;

COPY clubs(club)
FROM '/var/lib/postgresql/data/Tables/Clubs.csv'
DELIMITER ','
CSV HEADER;

delete from players;
ALTER SEQUENCE players_player_id_seq RESTART WITH 1;
COPY players(first_name, last_name, group_id, club_id)
FROM '/var/lib/postgresql/data/Tables/Players.csv'
DELIMITER ','
CSV HEADER;

COPY venues(venue)
FROM '/var/lib/postgresql/data/Tables/Venues.csv'
DELIMITER ','
CSV HEADER;

delete from matches;
ALTER SEQUENCE matches_match_id_seq RESTART WITH 1;
COPY matches(home_id, away_id, venue_id, date_time, week, friendly, home_score, away_score)
FROM '/var/lib/postgresql/data/Tables/Matches.csv'
DELIMITER ','
CSV HEADER;

delete from colours;
ALTER SEQUENCE colours_colour_id_seq RESTART WITH 1;
COPY colours(colour)
FROM '/var/lib/postgresql/data/Tables/Colours.csv'
DELIMITER ','
CSV HEADER;

delete from cards;
ALTER SEQUENCE cards_card_id_seq RESTART WITH 1;
COPY cards(player_id, match_id, time_given, colour_id)
FROM '/var/lib/postgresql/data/Tables/Cards.csv'
DELIMITER ','
CSV HEADER;

delete from goals;
ALTER SEQUENCE goals_goal_id_seq RESTART WITH 1;
COPY goals(player_id, match_id, time_scored)
FROM '/var/lib/postgresql/data//Tables/Goals.csv'
DELIMITER ','
CSV HEADER;
