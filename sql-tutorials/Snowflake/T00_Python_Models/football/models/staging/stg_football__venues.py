def model(dbt, session):
    source_df = dbt.source("football", "venues")
    final_df = source_df[["venue_id", "venue"]]
    return final_df
