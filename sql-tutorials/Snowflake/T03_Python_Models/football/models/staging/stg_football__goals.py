def model(dbt, session):
    source_df = dbt.source("football", "goals")
    final_df = source_df[["goal_id", "player_id", "match_id", "time_scored"]]
    return final_df
