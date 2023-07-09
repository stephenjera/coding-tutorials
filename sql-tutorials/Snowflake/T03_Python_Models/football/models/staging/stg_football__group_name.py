def model(dbt, session):
    source_df = dbt.source("football", "group_name")
    final_df = source_df[["group_id", "group_name"]]
    return final_df
