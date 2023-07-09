def model(dbt, session):
    source_df = dbt.source("football", "players")
    final_df = source_df[
        [
            "player_id",
            "group_id",
            "club_id",
            "first_name",
            "last_name",
        ]
    ]
    return final_df
