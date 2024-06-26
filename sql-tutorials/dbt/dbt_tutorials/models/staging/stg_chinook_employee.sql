with source as (
      select * from {{ source('chinook', 'Employee') }}
),
renamed as (
    select
        "EmployeeId" as employee_id,
        "LastName" as last_name,
        "FirstName" as first_name,
        "Title" as title,
        "ReportsTo" as reports_to,
        "BirthDate" as birth_date,
        "HireDate" as hire_date,
        "Address" as address,
        "City" as city,
        "State" as state,
        "Country" as country,
        "PostalCode" as postal_code,
        "Phone" as phone,
        "Fax" as fax,
        "Email" as email
    from source
)
select * from renamed
  