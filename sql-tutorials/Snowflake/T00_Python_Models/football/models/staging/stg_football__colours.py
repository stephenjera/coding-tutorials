def model(dbt, session):
    source_df = dbt.source("football", "colours")
    final_df = source_df[["colour_id", "colour"]]
    return final_df
