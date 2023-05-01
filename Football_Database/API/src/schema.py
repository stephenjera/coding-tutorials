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
    group: GroupNameType
    club: ClubsType

    @strawberry.field
    def group(self, info) -> GroupNameType:
        group = db.get_group(self.group_id)
        return GroupNameType(group_id=group.group_id, group_name=group.group_name)

    @strawberry.field
    def club(self, info) -> ClubsType:
        club = db.get_club(self.club_id)
        return ClubsType(club_id=club.club_id, club=club.club)


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
    week: int | None
    friendly: bool
    home_score: int | None
    away_score: int | None
    home_team: ClubsType
    away_team: ClubsType
    venue: VenuesType

    @strawberry.field
    def home_team(self, info) -> ClubsType:
        home_team = db.get_club(self.home_id)
        return ClubsType(club_id=home_team.club_id, club=home_team.club)

    @strawberry.field
    def away_team(self, info) -> ClubsType:
        away_team = db.get_club(self.away_id)
        return ClubsType(club_id=away_team.club_id, club=away_team.club)

    @strawberry.field
    def venue(self, info) -> VenuesType:
        venue = db.get_venue(venue_id=self.venue_id)
        return VenuesType(venue_id=venue.venue_id, venue=venue.venue)


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
    player: PlayersType
    match: MatchesType

    @strawberry.field
    def player(self, info) -> PlayersType:
        # Fetch the related player from the database using the player_id
        player = db.get_player(self.player_id)
        return PlayersType(
            player_id=player.player_id,
            group_id=player.group_id,
            club_id=player.club_id,
            first_name=player.first_name,
            last_name=player.last_name,
        )

    @strawberry.field
    def match(self, info) -> MatchesType:
        # Fetch the related match from the database using the match_id
        match = db.get_match(match_id=self.match_id)
        return MatchesType(
            match_id=match.match_id,
            home_id=match.home_id,
            away_id=match.away_id,
            venue_id=match.venue_id,
            date_time=match.date_time,
            week=match.week,
            friendly=match.friendly,
            home_score=match.home_score,
            away_score=match.away_score,
        )

    @strawberry.field
    def colour(self, info) -> ColoursType:
        # Fetch the related colour from the database using the colour_id
        colour = db.get_colour(colour_id=self.colour_id)
        return ColoursType(colour_id=colour.colour_id, colour=colour.colour)


@strawberry.type
class GoalsType:
    goal_id: int
    player_id: int
    match_id: int
    time_scored: datetime
    player: PlayersType
    match: MatchesType  # match is a keyword but it works U0001F603

    @strawberry.field
    def player(self, info) -> PlayersType:
        # Fetch the related player from the database using the player_id
        player = db.get_player(self.player_id)
        return PlayersType(
            player_id=player.player_id,
            group_id=player.group_id,
            club_id=player.club_id,
            first_name=player.first_name,
            last_name=player.last_name,
        )

    @strawberry.field
    def match(self, info) -> MatchesType:
        # Fetch the related match from the database using the match_id
        match = db.get_match(match_id=self.match_id)
        return MatchesType(
            match_id=match.match_id,
            home_id=match.home_id,
            away_id=match.away_id,
            venue_id=match.venue_id,
            date_time=match.date_time,
            week=match.week,
            friendly=match.friendly,
            home_score=match.home_score,
            away_score=match.away_score,
        )


@strawberry.type
class Query:
    @strawberry.field
    def clubs(self, info) -> list[ClubsType]:
        # Fetch all clubs from the database
        clubs = db.get_all_clubs()
        return [ClubsType(club_id=club.club_id, club=club.club) for club in clubs]

    @strawberry.field
    def groups(self) -> list[GroupNameType]:
        return db.get_all_groups()

    @strawberry.field
    def players(self, info) -> list[PlayersType]:
        players = db.get_all_players()
        return [
            PlayersType(
                player_id=player.player_id,
                group_id=player.group_id,
                club_id=player.club_id,
                first_name=player.first_name,
                last_name=player.last_name,
            )
            for player in players
        ]

    @strawberry.field
    def matches(self, info) -> list[MatchesType]:
        matches = db.get_all_matches()
        return [
            MatchesType(
                match_id=match.match_id,
                home_id=match.home_id,
                away_id=match.away_id,
                venue_id=match.venue_id,
                date_time=match.date_time,
                week=match.week,
                friendly=match.friendly,
                home_score=match.home_score,
                away_score=match.away_score,
            )
            for match in matches
        ]

    @strawberry.field
    def cards(self, info) -> list[CardsType]:
        cards = db.get_all_cards()
        return [
            CardsType(
                card_id=card.card_id,
                player_id=card.player_id,
                match_id=card.match_id,
                colour_id=card.colour_id,
                time_given=card.time_given,
            )
            for card in cards
        ]

    @strawberry.field
    def goals(self, info) -> list[GoalsType]:
        goals = db.get_all_goals()
        return [
            GoalsType(
                goal_id=goal.goal_id,
                player_id=goal.player_id,
                match_id=goal.match_id,
                time_scored=goal.time_scored,
            )
            for goal in goals
        ]


# @strawberry.type
# class Mutation:
#     # @strawberry.mutation
#     # def create_group() -> GroupNameType:
#     #     return db.GroupName.create_group(group)

#     @strawberry.mutation
#     def create_group(
#         self, group_name: str, group_id: int | None = None
#     ) -> GroupNameType:
#         group = db.GroupName(group_id=group_id, group_name=group_name)
#         return db.GroupName.create_group(group)

#     @strawberry.mutation
#     def update_group(self, group_id: int, group_name: str) -> GroupNameType | None:
#         return db.GroupName.update_group(group_id, group_name)

#     @strawberry.mutation
#     def delete_group(self, group_id: int) -> bool:
#         db.GroupName.delete_group(group_id)
#         return True

#     @strawberry.mutation
#     def delete_group(self, group_id: int) -> None:
#         db.GroupName.delete_group(group_id)

schema = strawberry.Schema(query=Query)
# schema = strawberry.Schema(query=Query, mutation=Mutation)
