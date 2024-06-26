with source as (
      select * from {{ source('chinook', 'Customer') }}
),
renamed as (
    select
        "CustomerId" as customer_id,
        "FirstName" as first_name,
        "LastName" as last_name,
        "Company" as company,
        "Address" as address,
        "City" as city,
        "State" as state,
        "Country" as country,
        "PostalCode" as postal_code,
        "Phone" as phone,
        "Fax" as fax,
        "Email" as email,
        "SupportRepId" as support_rep_id

    from source
)
select * from renamed
  