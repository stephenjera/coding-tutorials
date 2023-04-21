# Setting up Postgres Database

This directory contains files to set up a postgres database and pg admin with docker.

## Setup database

In this directory run:

```powershell
docker compose up -d
```

## Setup PG Admin

Navigate to **localhost:5050**

email = test@mail.com

password = docker

login to PG admin 
## Load datasets
In the scripts folder run the following for windows systems 
```shell
 wsl bash load_databases.sh
 ```
or the command below for linux systems
```shell
bash load_databases.sh
 ```


