WITH t02_update AS (
    SELECT * FROM {{ ref('t02_update') }}
),

soft_delete AS (
    SELECT
        *,
        CASE
            WHEN total > 10 THEN TRUE
            ELSE FALSE
        END AS deleted_flag
    FROM t02_update
)

SELECT * FROM soft_delete --WHERE deleted_flag = FALSE
