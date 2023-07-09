-- Create the "group_name" table
CREATE TABLE thoughtspot.dev.group_name (
  group_id INT AUTOINCREMENT,
  group_name VARCHAR(255),
  PRIMARY KEY (group_id)
);

-- Inserting data into the "group_name" table
INSERT INTO thoughtspot.dev.group_name (group_name)
VALUES
  ('Cohort 4'),
  ('Cohort 5'),
  ('Cohort 6'),
  ('Cohort 7'),
  ('Bench'),
  ('Training Team'),
  ('HR'),
  ('Consultants');


-- Create the "clubs" table
CREATE TABLE thoughtspot.dev.clubs (
  club_id INT AUTOINCREMENT,
  club VARCHAR(255),
  PRIMARY KEY (club_id)
);

-- Inserting data into the "clubs" table
INSERT INTO thoughtspot.dev.clubs (club)
VALUES
  ('Data Masters'),
  ('BI Gods'),
  ('Vis Wizards'),
  ('Data Cleaners');

-- Create the "players" table
CREATE TABLE thoughtspot.dev.players (
  player_id INT AUTOINCREMENT,
  group_id INT,
  club_id INT,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  PRIMARY KEY (player_id),
  FOREIGN KEY (group_id) REFERENCES thoughtspot.dev.group_name(group_id),
  FOREIGN KEY (club_id) REFERENCES thoughtspot.dev.clubs(club_id)
);

-- Inserting data into the "players" table
INSERT INTO thoughtspot.dev.players (first_name, last_name, group_id, club_id)
VALUES
  ('Aedan', 'Petty', 1, 1),
  ('Aliza', 'Santos', 3, 1),
  ('Kaylynn', 'Vaughan', 6, 1),
  ('Arjun', 'Bauer', 4, 1),
  ('Lilian', 'Huber', 2, 1),
  ('Lizeth', 'Roberts', 6, 1),
  ('Nathan', 'Mcdowell', 7, 1),
  ('Alvin', 'Ali', 8, 1),
  ('Jordin', 'Christensen', 7, 1),
  ('Saul', 'Blevins', 7, 1),
  ('Carina', 'Meza', 2, 2),
  ('Isabelle', 'Campos', 5, 2),
  ('Kyleigh', 'Phelps', 1, 2),
  ('Angela', 'Wong', 7, 2),
  ('Kole', 'Rojas', 7, 2),
  ('Martha', 'Potts', 4, 2),
  ('Tomas', 'Powell', 6, 2),
  ('Paxton', 'Clarke', 5, 2),
  ('Jamya', 'Dodson', 8, 2),
  ('Georgia', 'Clements', 8, 2),
  ('Edwin', 'Crawford', 2, 3),
  ('Malachi', 'Osborn', 8, 3),
  ('Zion', 'Kent', 2, 3),
  ('Anahi', 'Reyes', 5, 3),
  ('Maddox', 'Cabrera', 8, 3),
  ('Brody', 'Gutierrez', 4, 3),
  ('Hayley', 'Stevenson', 3, 3),
  ('Kamora', 'Sanchez', 8, 3),
  ('Livia', 'Holmes', 6, 3),
  ('Tanner', 'Jenkins', 8, 3),
  ('Madelyn', 'Meadows', 5, 4),
  ('Paola', 'Wilkerson', 3, 4),
  ('Jared', 'Patton', 6, 4),
  ('Pierre', 'Washington', 8, 4),
  ('Dominik', 'Cochran', 4, 4),
  ('Miya', 'Skinner', 4, 4),
  ('Mara', 'Barnett', 5, 4),
  ('Cornelius', 'Dodson', 2, 4),
  ('Ashleigh', 'Kaiser', 6, 4),
  ('Weston', 'Meza', 6, 4);


-- Create the "venues" table
CREATE TABLE thoughtspot.dev.venues (
  venue_id INT AUTOINCREMENT,
  venue VARCHAR(255),
  PRIMARY KEY (venue_id)
);

-- Inserting data into the "venues" table
INSERT INTO thoughtspot.dev.venues (venue)
VALUES
  ('Wimbledon 1'),
  ('Wimbledon 2'),
  ('Wimbledon 3');


-- Create the "matches" table
CREATE TABLE thoughtspot.dev.matches (
  match_id INT AUTOINCREMENT,
  home_id INT,
  away_id INT,
  venue_id INT,
  date_time TIMESTAMP,
  week INT,
  friendly BOOLEAN,
  home_score INT,
  away_score INT,
  PRIMARY KEY (match_id),
  FOREIGN KEY (home_id) REFERENCES thoughtspot.dev.clubs(club_id),
  FOREIGN KEY (away_id) REFERENCES thoughtspot.dev.clubs(club_id),
  FOREIGN KEY (venue_id) REFERENCES thoughtspot.dev.venues(venue_id)
);

-- Inserting data into the "matches" table
INSERT INTO thoughtspot.dev.matches (home_id, away_id, venue_id, date_time, week, friendly, home_score, away_score)
VALUES
  (1, 2, 1, '2022-10-01 16:00:00', 1, FALSE, 2, 0),
  (3, 4, 2, '2022-10-01 16:00:00', 1, FALSE, 1, 1),
  (1, 3, 2, '2022-08-10 16:00:00', 2, FALSE, 2, 1),
  (2, 4, 3, '2022-08-10 16:00:00', 2, FALSE, 2, 1),
  (1, 4, 3, '2022-10-22 16:00:00', 3, FALSE, 0, 0),
  (2, 3, 2, '2022-10-22 16:00:00', 3, FALSE, 1, 2),
  (2, 1, 1, '2022-10-29 16:00:00', 4, FALSE, 2, 2),
  (4, 3, 3, '2022-10-29 16:00:00', 4, FALSE, 1, 2),
  (3, 1, 3, '2022-11-05 16:00:00', 5, FALSE, 3, 2),
  (4, 2, 1, '2022-11-05 16:00:00', 5, FALSE, 0, 1),
  (4, 1, 2, '2022-12-11 16:00:00', 6, FALSE, 2, 0),
  (3, 2, 3, '2022-12-12 16:00:00', 6, FALSE, 2, 2),
  (4, 1, 1, '2023-11-12 16:00:00', NULL, TRUE, NULL, NULL),
  (3, 2, 3, '2023-11-12 16:00:00', NULL, TRUE, NULL, NULL);


-- Create the "colours" table
CREATE TABLE thoughtspot.dev.colours (
  colour_id INT AUTOINCREMENT,
  colour VARCHAR(255),
  PRIMARY KEY (colour_id)
);

INSERT INTO thoughtspot.dev.colours (colour)
VALUES
    ('Yellow'),
    ('Red');

-- Create the "cards" table
CREATE TABLE thoughtspot.dev.cards (
  card_id INT AUTOINCREMENT,
  player_id INT,
  match_id INT,
  colour_id INT,
  time_given TIMESTAMP,
  PRIMARY KEY (card_id),
  FOREIGN KEY (player_id) REFERENCES thoughtspot.dev.players(player_id),
  FOREIGN KEY (match_id) REFERENCES thoughtspot.dev.matches(match_id),
  FOREIGN KEY (colour_id) REFERENCES thoughtspot.dev.colours(colour_id)
);

INSERT INTO thoughtspot.dev.cards (player_id, match_id, time_given, colour_id)
VALUES
  (12, 1, '2022-10-01 16:00:00', 1),
  (30, 2, '2022-10-01 16:00:00', 1),
  (1, 3, '2022-10-08 16:00:00', 1),
  (9, 3, '2022-10-08 16:00:00', 1),
  (10, 5, '2022-11-05 16:00:00', 1),
  (38, 5, '2022-11-05 16:00:00', 1),
  (3, 7, '2022-10-22 16:00:00', 1),
  (35, 8, '2022-10-29 16:00:00', 1),
  (23, 9, '2022-10-29 16:00:00', 1),
  (32, 10, '2022-11-05 16:00:00', 2),
  (1, 11, '2022-11-05 16:00:00', 2),
  (17, 12, '2022-11-12 16:00:00', 1);


-- Create the "goals" table
CREATE TABLE thoughtspot.dev.goals (
  goal_id INT AUTOINCREMENT,
  player_id INT,
  match_id INT,
  time_scored TIMESTAMP,
  PRIMARY KEY (goal_id),
  FOREIGN KEY (player_id) REFERENCES thoughtspot.dev.players(player_id),
  FOREIGN KEY (match_id) REFERENCES thoughtspot.dev.matches(match_id)
);

-- Inserting data into the "goals" table
INSERT INTO thoughtspot.dev.goals (player_id, match_id, time_scored)
VALUES
  (8, 1, '2022-10-01 16:00:00'),
  (7, 1, '2022-10-01 16:00:00'),
  (27, 2, '2022-10-01 16:00:00'),
  (35, 2, '2022-10-01 16:00:00'),
  (8, 3, '2022-10-08 16:00:00'),
  (8, 3, '2022-10-08 16:00:00'),
  (27, 3, '2022-10-08 16:00:00'),
  (19, 4, '2022-10-08 16:00:00'),
  (17, 4, '2022-10-08 16:00:00'),
  (19, 6, '2022-10-22 16:00:00'),
  (28, 6, '2022-10-22 16:00:00'),
  (27, 6, '2022-10-22 16:00:00'),
  (19, 7, '2022-10-22 16:00:00'),
  (16, 7, '2022-10-22 16:00:00'),
  (8, 7, '2022-10-22 16:00:00'),
  (3, 7, '2022-10-22 16:00:00'),
  (35, 8, '2022-10-29 16:00:00'),
  (25, 8, '2022-10-29 16:00:00'),
  (27, 8, '2022-10-29 16:00:00'),
  (29, 9, '2022-10-29 16:00:00'),
  (29, 9, '2022-10-29 16:00:00'),
  (26, 9, '2022-10-29 16:00:00'),
  (7, 9, '2022-10-29 16:00:00'),
  (8, 9, '2022-10-29 16:00:00'),
  (19, 10, '2022-11-05 16:00:00'),
  (35, 11, '2022-11-05 16:00:00'),
  (37, 11, '2022-11-05 16:00:00'),
  (26, 12, '2022-11-12 16:00:00'),
  (25, 12, '2022-11-12 16:00:00'),
  (19, 12, '2022-11-12 16:00:00'),
  (18, 12, '2022-11-12 16:00:00');


