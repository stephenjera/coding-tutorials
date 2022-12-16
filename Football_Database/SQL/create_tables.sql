CREATE TABLE "group_name" (
  "group_id" serial,
  "group_name" text,
  PRIMARY KEY ("group_id")
);

CREATE TABLE "clubs" (
  "club_id" serial,
  "club" text,
  PRIMARY KEY ("club_id")
);

CREATE TABLE "players" (
  "player_id" serial,
  "group_id" smallint,
  "club_id" smallint,
  "first_name" text,
  "last_name" text,
  PRIMARY KEY ("player_id"),
  CONSTRAINT "FK_players.group_id"
    FOREIGN KEY ("group_id")
      REFERENCES "group_name"("group_id"),
  CONSTRAINT "FK_players.club_id"
    FOREIGN KEY ("club_id")
      REFERENCES "clubs"("club_id")
);

CREATE TABLE "venues" (
  "venue_id" serial,
  "venue" text,
  PRIMARY KEY ("venue_id")
);

CREATE TABLE "matches" (
  "match_id" serial,
  "home_id" smallint,
  "away_id" smallint,
  "venue_id" smallint,
  "date_time" timestamp,
  "week" smallint,
  "friendly" bool,
  "home_score" smallint,
  "away_score" smallint,
  PRIMARY KEY ("match_id"),
  CONSTRAINT "FK_matches.away_id"
    FOREIGN KEY ("away_id")
      REFERENCES "clubs"("club_id"),
  CONSTRAINT "FK_matches.venue_id"
    FOREIGN KEY ("venue_id")
      REFERENCES "venues"("venue_id"),
  CONSTRAINT "FK_matches.home_id"
    FOREIGN KEY ("home_id")
      REFERENCES "clubs"("club_id")
);

CREATE TABLE "colours" (
  "colour_id" serial,
  "colour" text,
  PRIMARY KEY ("colour_id")
);

CREATE TABLE "cards" (
  "card_id" serial,
  "player_id" smallint,
  "match_id" smallint,
  "colour_id" smallint,
  "time_given" timestamp,
  PRIMARY KEY ("card_id"),
  CONSTRAINT "FK_cards.player_id"
    FOREIGN KEY ("player_id")
      REFERENCES "players"("player_id"),
  CONSTRAINT "FK_cards.match_id"
    FOREIGN KEY ("match_id")
      REFERENCES "matches"("match_id"),
  CONSTRAINT "FK_cards.colour_id"
    FOREIGN KEY ("colour_id")
      REFERENCES "colours"("colour_id")
);

CREATE TABLE "goals" (
  "goal_id" serial,
  "player_id" smallint,
  "match_id" smallint,
  "time_scored" timestamp,
  PRIMARY KEY ("goal_id"),
  CONSTRAINT "FK_goals.match_id"
    FOREIGN KEY ("match_id")
      REFERENCES "matches"("match_id"),
  CONSTRAINT "FK_goals.player_id"
    FOREIGN KEY ("player_id")
      REFERENCES "players"("player_id")
);
