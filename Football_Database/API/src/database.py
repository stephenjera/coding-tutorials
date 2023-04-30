from datetime import datetime
from sqlmodel import SQLModel, Field, create_engine, Session
from sqlmodel import Session, select

POSTGRES_USER = "docker"
POSTGRES_PW = "docker"
POSTGRES_DB = "football_db"
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PW}@localhost/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL, echo=True)


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


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


class GroupQL:
    # Query methods
    @staticmethod
    def get_all_groups() -> list[GroupName]:
        with Session(engine) as session:
            groups = session.exec(select(GroupName)).all()
        return groups

    # Mutation methods
    @staticmethod
    def create_group(group: GroupName) -> GroupName:
        with Session(engine) as session:
            session.add(group)
            session.commit()
            session.refresh(group)
        return group

    @staticmethod
    def create_group(group: GroupName) -> GroupName:
        with Session(engine) as session:
            session.add(group)
            session.commit()
            session.refresh(group)
        return group

    @staticmethod
    def update_group(group_id: int, group_name: str) -> GroupName:
        with Session(engine) as session:
            group = session.get(GroupName, group_id)
            if group is not None:
                group.group_name = group_name
                session.add(group)
                session.commit()
                session.refresh(group)
        return group

    @staticmethod
    def delete_group(group_id: int) -> None:
        with Session(engine) as session:
            group = session.get(GroupName, group_id)
            if group is not None:
                session.delete(group)
                session.commit()
                return True
            return False
