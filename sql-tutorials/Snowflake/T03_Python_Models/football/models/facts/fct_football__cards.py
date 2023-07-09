from snowflake.snowpark.functions import col

def model(dbt, session):
    cards_df = dbt.ref("stg_football__cards")
    colours_df = dbt.ref("stg_football__colours")

    final_df = cards_df.join(colours_df, on="colour_id")
    final_df = final_df.select(
        col("card_id"),
        col("player_id"),
        col("match_id"),
        col("colour"),
        col("time_given")
    )

    return final_df.toPandas()
