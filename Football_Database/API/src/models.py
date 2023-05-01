from sqlmodel import SQLModel, Field
from datetime import datetime


class GroupName(SQLModel, table=True):
    __tablename__ = "group_name"
    group_id: int | None = Field(default=None, primary_key=True)
    group_name: str


class Clubs(SQLModel, table=True):
    club_id: int | None = Field(default=None, primary_key=True)
    club: str


class Players(SQLModel, table=True):
    player_id: int | None = Field(default=None, primary_key=True)
    group_id: int | None = Field(default=None, foreign_key="group_name.group_id")
    club_id: int | None = Field(default=None, foreign_key="clubs.club_id")
    first_name: str
    last_name: str


class Venues(SQLModel, table=True):
    venue_id: int | None = Field(default=None, primary_key=True)
    venue: str


class Matches(SQLModel, table=True):
    match_id: int | None = Field(default=None, primary_key=True)
    home_id: int | None = Field(default=None, foreign_key="clubs.club_id")
    away_id: int | None = Field(default=None, foreign_key="clubs.club_id")
    venue_id: int | None = Field(default=None, foreign_key="venues.venue_id")
    date_time: datetime
    week: int
    friendly: bool
    home_score: int
    away_score: int


class Colours(SQLModel, table=True):
    colour_id: int | None = Field(default=None, primary_key=True)
    colour: str


class Cards(SQLModel, table=True):
    card_id: int | None = Field(default=None, primary_key=True)
    player_id: int | None = Field(default=None, foreign_key="players.player_id")
    match_id: int | None = Field(default=None, foreign_key="matches.match_id")
    colour_id: int | None = Field(default=None, foreign_key="colours.colour_id")
    time_given: datetime


class Goals(SQLModel, table=True):
    goal_id: int | None = Field(default=None, primary_key=True)
    player_id: int | None = Field(default=None, foreign_key="players.player_id")
    match_id: int | None = Field(default=None, foreign_key="matches.match_id")
    time_scored: datetime
