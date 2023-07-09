USE ROLE USERADMIN;

CREATE ROLE tableau_user;

CREATE USER tableau_user
PASSWORD = 'strong_password';

GRANT ROLE tableau_user TO ROLE SYSADMIN;
GRANT ROLE tableau_user TO USER tableau_user;
ALTER USER tableau_user SET DEFAULT_ROLE = 'tableau_user';

USE ROLE SYSADMIN;
CREATE WAREHOUSE compute_xs;
CREATE DATABASE tableau;
CREATE SCHEMA tableau.tableau_data;
CREATE OR REPLACE TABLE tableau.tableau_data.forex_data (
    date DATE,
    currency_from STRING,
    currency_to STRING,
    exchange_rate FLOAT
);

INSERT INTO forex_data (date, currency_from, currency_to, exchange_rate)
VALUES
    ('2022-01-01', 'USD', 'EUR', 0.85),
    ('2022-01-02', 'USD', 'EUR', 0.86),
    ('2022-01-03', 'USD', 'EUR', 0.87),
    ('2022-01-04', 'USD', 'EUR', 0.88),
    ('2022-01-05', 'USD', 'EUR', 0.89);

CREATE OR REPLACE VIEW tableau.tableau_data.forex_data_view AS
SELECT *
FROM forex_data;

USE ROLE SECURITYADMIN;
GRANT USAGE ON WAREHOUSE compute_xs TO ROLE tableau_user;
GRANT USAGE ON DATABASE tableau TO ROLE tableau_user;
GRANT USAGE ON ALL SCHEMAS IN DATABASE tableau TO ROLE tableau_user;
GRANT SELECT ON ALL TABLES IN DATABASE tableau TO ROLE tableau_user;
GRANT SELECT ON ALL VIEWS IN DATABASE tableau TO ROLE tableau_user;
-- for demo only ----------------------------------------------------------------------
GRANT CREATE SCHEMA, MODIFY, MONITOR, USAGE ON DATABASE Tableau TO ROLE tableau_user;
GRANT ALL PRIVILEGES ON FUTURE SCHEMAS IN DATABASE Tableau TO ROLE tableau_user;
GRANT ALL PRIVILEGES ON FUTURE TABLES IN DATABASE Tableau TO ROLE tableau_user;
GRANT ALL PRIVILEGES ON FUTURE VIEWS IN DATABASE Tableau TO ROLE tableau_user;
GRANT ALL PRIVILEGES ON FUTURE FUNCTIONS IN DATABASE Tableau TO ROLE tableau_user;
GRANT ALL PRIVILEGES ON FUTURE PROCEDURES IN DATABASE Tableau TO ROLE tableau_user;
---------------------------------------------------------------------------------------

select * from forex_data;

