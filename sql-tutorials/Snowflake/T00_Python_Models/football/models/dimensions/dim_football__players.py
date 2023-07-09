from snowflake.snowpark.functions import col

def model(dbt, session):
    players_df = dbt.ref("stg_football__players")
    clubs_df = dbt.ref("stg_football__clubs")
    group_name_df = dbt.ref("stg_football__group_name")

    final_df = players_df.join(clubs_df, on="club_id").join(group_name_df, on="group_id")
    final_df = final_df.select(
        col("player_id"),
        col("first_name"),
        col("last_name"),
        col("club"),
        col("group_name")
    )

    return final_df.toPandas()
