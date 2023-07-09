from snowflake.snowpark.functions import col, when

def model(dbt, session):
    clubs_df = dbt.ref("stg_football__clubs")
    venues_df = dbt.ref("stg_football__venues")
    matches_df = dbt.ref("stg_football__matches")

    points_df = matches_df.join(clubs_df, matches_df.home_id == clubs_df.club_id).join(venues_df, on="venue_id")
    points_df = points_df.select(
        col("match_id"),
        col("venue"),
        col("week"),
        col("date_time"),
        col("club").alias("club_home"),
        col("home_score"),
        col("away_score"),
        col("away_id"),  
        when(col("home_score") > col("away_score"), 3)
            .when(col("home_score") == col("away_score"), 1)
            .when(col("home_score") < col("away_score"), 0)
            .otherwise(None).alias("home_points")
    )

    final_df = points_df.join(clubs_df, points_df.away_id == clubs_df.club_id)
    final_df = final_df.select(
        col("match_id"),
        col("venue"),
        col("week"),
        col("date_time"),
        col("club_home"),
        col("home_score"),
        col("club").alias("club_away"),
        col("away_score"),
        col("home_points"),
        when(col("away_score") > col("home_score"), 3)
            .when(col("away_score") == col("home_score"), 1)
            .when(col("away_score") < col("home_score"), 0)
            .otherwise(None).alias("away_points")
    )

    return final_df.toPandas()
