def model(dbt, session):
    source_df = dbt.source("football", "cards")
    final_df = source_df[["card_id", "player_id", "match_id", "colour_id", "time_given"]]
    return final_df
