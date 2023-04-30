import strawberry
import database as db
from datetime import datetime


@strawberry.type
class GroupNameType:
    group_id: int
    group_name: str


@strawberry.type
class ClubsType:
    club_id: int
    club: str


@strawberry.type
class PlayersType:
    player_id: int
    group_id: int
    club_id: int
    first_name: str
    last_name: str


@strawberry.type
class VenuesType:
    venue_id: int
    venue: str


@strawberry.type
class MatchesType:
    match_id: int
    home_id: int
    away_id: int
    venue_id: int
    date_time: datetime
    week: int
    friendly: bool
    home_score: int
    away_score: int


@strawberry.type
class ColoursType:
    colour_id: int
    colour: str


@strawberry.type
class CardsType:
    card_id: int
    player_id: int
    match_id: int
    colour_id: int
    time_given: datetime


@strawberry.type
class GoalsType:
    goal_id: int
    player_id: int
    match_id: int
    time_scored: datetime


# @strawberry.type
# class Query(db.GroupQL):
#     @strawberry.field
#     def all_groups(self) -> list[GroupNameType]:
#         return db.GroupQL.get_all_groups()

#     @strawberry.field
#     def create_group(self) -> GroupNameType:
#         return db.GroupQL.create_group()

#     @strawberry.field
#     def update_group(self) -> GroupNameType | None:
#         return db.GroupQL.update_group()


@strawberry.type
class Query(db.GroupQL):
    @strawberry.field
    def all_groups(self) -> list[GroupNameType]:
        return db.GroupQL.get_all_groups()


@strawberry.type
class Mutation:
    # @strawberry.mutation
    # def create_group() -> GroupNameType:
    #     return db.GroupQL.create_group(group)

    @strawberry.mutation
    def create_group(self, group_name: str, group_id: int | None = None) -> GroupNameType:
        group = db.GroupName(group_id=group_id, group_name=group_name)
        return db.GroupQL.create_group(group)
    

    @strawberry.mutation
    def update_group(self, group_id: int, group_name: str) -> GroupNameType | None:
        return db.GroupQL.update_group(group_id, group_name)

    @strawberry.mutation
    def delete_group(self, group_id: int) -> bool:
        db.GroupQL.delete_group(group_id)
        return True

    

    # @strawberry.mutation
    # def delete_group(self, group_id: int) -> None:
    #     db.GroupQL.delete_group(group_id)


schema = strawberry.Schema(query=Query, mutation=Mutation)
