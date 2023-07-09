def model(dbt, session):
    source_df = dbt.source("football", "matches")
    final_df = source_df[
        [
            "match_id",
            "home_id",
            "away_id",
            "venue_id",
            "date_time",
            "week",
            "friendly",
            "home_score",
            "away_score",
        ]
    ]
    return final_df
