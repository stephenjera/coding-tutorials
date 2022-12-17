# Football Database

**To run the project docker is required.**

1. Download the project and in the project folder run ```docker compose up```

1. Navigate to a web browser and type **localhost:5050**

1. Login to PG Admin **username=test@mail.com** and **password=docker**

1. Navigate to the PG Admin dashboard and click add new server

1. In the general tab set the name to docker

1. In the connection tab set the hostname to **dockerhost**, the username to **docker** and the password to **docker** then hit save

1. In the servers list docker should now be available, inside should be **footbal_db** right click it and select query tool

1. When finished run ```docker compose down``` to close the project

The database is now set up and ready for use, the queries used to test it can be found [here](https://github.com/stephenjera/SQL-Projects/tree/master/Football_Database/SQL)
