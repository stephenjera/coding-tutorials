WITH t01_insert AS (
    -- Reference the combined data from the `t01_insert` model
    SELECT * FROM {{ ref('t01_insert') }}
),

updated_data AS (
    SELECT
        invoice_id,
        customer_id,
        invoice_date,
        billing_address,
        billing_city,
        billing_state,
        billing_country,
        billing_postal_code,
        -- Apply the update conditionally
        CASE
            WHEN invoice_id = 1002 THEN 30.00  -- Update total to 30.00
            ELSE total
        END AS total
    FROM t01_insert
)

SELECT * FROM updated_data
