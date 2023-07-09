def model(dbt, session):
    goals_df = dbt.ref("stg_football__goals")
    final_df = goals_df[
        [
            "goal_id",
            "player_id",
            "match_id",
            "time_scored",
        ]
    ]
    return final_df
