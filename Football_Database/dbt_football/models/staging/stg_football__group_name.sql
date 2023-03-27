select group_id, group_name from {{ source("football", "group_name") }}
