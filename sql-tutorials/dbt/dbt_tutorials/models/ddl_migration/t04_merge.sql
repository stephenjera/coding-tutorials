WITH 
t03_delete as (SELECT * FROM {{ ref('t03_delete') }}),
using_clause AS (
    -- Simulate incoming data to merge, like `rides_to_load` in the example
    SELECT 
        1002 AS invoice_id,
        6 AS customer_id,
        '2024-12-01 15:00:00'::timestamp AS invoice_date,
        '789 Broadway St' AS billing_address,
        'Boston' AS billing_city,
        'MA' AS billing_state,
        'USA' AS billing_country,
        '02118' AS billing_postal_code,
        35.00::numeric AS total
    UNION ALL
    SELECT 
        1003 AS invoice_id,
        7 AS customer_id,
        '2024-12-01 16:00:00'::timestamp AS invoice_date,
        '456 Elm St' AS billing_address,
        'Chicago' AS billing_city,
        'IL' AS billing_state,
        'USA' AS billing_country,
        '60616' AS billing_postal_code,
        45.00::numeric AS total
),

updates AS (
    -- Identify updates: match `invoice_id` and use new data for matching rows
    SELECT 
        base.invoice_id,
        u.customer_id,
        u.invoice_date,
        u.billing_address,
        u.billing_city,
        u.billing_state,
        u.billing_country,
        u.billing_postal_code,
        u.total
    FROM t03_delete as base
    JOIN using_clause u ON base.invoice_id = u.invoice_id
),

inserts AS (
    -- Identify inserts: include only records that don't match existing `invoice_id`
    SELECT 
        u.invoice_id,
        u.customer_id,
        u.invoice_date,
        u.billing_address,
        u.billing_city,
        u.billing_state,
        u.billing_country,
        u.billing_postal_code,
        u.total
    FROM using_clause u
    LEFT JOIN t03_delete as base ON base.invoice_id = u.invoice_id
    WHERE base.invoice_id IS NULL
)

-- Combine updates and inserts to mimic the merge
SELECT * FROM updates
UNION ALL
SELECT * FROM inserts
