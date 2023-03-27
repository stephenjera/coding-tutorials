# Setting up tutorials

This directory contains files to set up a docker postgres database and pg with persistent memory using volumes.

In this directory run:

```powershell
docker compose up -d
```

Then navigate to **localhost:5050**

email = test@mail.com

password = docker

login to PG admin and create a new server 

```json
"Name": "docker",
        "Group": "Servers",
        "Host": "postgres",
        "Port": 5432,
        "MaintenanceDB": "postgres",
        "Username": "docker",
        "Password": "docker",
        "SSLMode": "prefer",
        "SSLCompression": 0,
        "SavePassword": true,
        "SSLRootCert": "",
        "SSLKey": "",
        "SSLCert": "",
        "Comments": ""
```

finally run the relevant script in the scripts folder to populate the database

