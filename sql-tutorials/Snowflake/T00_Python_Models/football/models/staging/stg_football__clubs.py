def model(dbt, session):
    source_df = dbt.source("football", "clubs")
    final_df = source_df[["club_id", "club"]]
    return final_df