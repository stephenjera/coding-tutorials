WITH existing_data AS (
    -- Pull all current data from the staging model
    SELECT *
    FROM {{ ref('stg_chinook_invoice') }}
),

new_data AS (
    -- Define the new data to be inserted
    SELECT
        1002 AS invoice_id,
        6 AS customer_id,
        '2024-12-01 14:00:00'::timestamp AS invoice_date,
        '123 Main St' AS billing_address,
        'New York' AS billing_city,
        'NY' AS billing_state,
        'USA' AS billing_country,
        '10001' AS billing_postal_code,
        25.50::numeric AS total
)

-- Combine the existing data with the new data to simulate the "INSERT"
SELECT * FROM existing_data
UNION ALL
SELECT * FROM new_data
