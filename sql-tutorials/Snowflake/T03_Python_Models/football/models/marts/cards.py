from snowflake.snowpark.functions import col


def model(dbt, session):
    cards_df = dbt.ref("fct_football__cards")
    players_df = dbt.ref("dim_football__players")
    matches_df = dbt.ref("dim_football__matches")

    final_df = cards_df.join(players_df, on="player_id").join(matches_df, on="match_id")

    players_columns = [
        col("first_name"),
        col("last_name"),
        col("club"),
        col("group_name"),
    ]
    matches_columns = [
        col("venue"),
        col("week"),
        col("date_time"),
        col("club_home"),
        col("home_score"),
        col("club_away"),
        col("away_score"),
        col("home_points"),
        col("away_points"),
    ]

    final_columns = (
        [col(column) for column in cards_df.columns] + players_columns + matches_columns
    )

    final_df = final_df.select(*final_columns)

    return final_df.toPandas()
