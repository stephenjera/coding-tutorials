CREATE ROLE account_admin;

GRANT ALL PRIVILEGES ON *.* TO account_admin;

CREATE USER admin IDENTIFIED BY 'admin';

GRANT account_admin TO admin;


CREATE ROLE IF NOT EXISTS sysadmin;
GRANT CREATE ON *.* TO sysadmin;
GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO sysadmin;
GRANT sysadmin TO admin;

SET ROLE sysadmin;
CRATE DATABASE IF NOT EXISTS analytics;