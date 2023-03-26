docker exec -it postgres psql -U postgres -d superstore -c "create table if not exists superstore (
    id serial not null,
    ship_model varchar(255) not null,
    segment varchar(255) not null,
    country varchar(255) not null,
    city varchar(255) not null,
    state varchar(255) not null,
    postal_code int not null,
    region varchar(255) not null,
    category varchar(255) not null,
    subcategory varchar(255) not null,
    sales float not null,
    quantity int not null,
    discount float not null,
    profit float not null,
    primary key(id)
) ;"


docker exec -it postgres psql -U docker -d superstore -c "COPY superstore(
    ship_model,
    segment,
    country,
    city,
    state,
    postal_code,
    region,
    category,
    subcategory,
    sales,
    quantity,
    discount,
    profit)
    FROM '/var/lib/postgresql/data/datasets/superstore.csv' DELIMITER ',' CSV HEADER;"