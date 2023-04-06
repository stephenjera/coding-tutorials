#!/bin/bash

# Create the configuration file
echo '{
    "Servers": [
      {
        "Name": "Docker",
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
      }
    ]
}' > /var/lib/pgadmin/pgadmin4.db

# Call the original entrypoint script to start the pgAdmin container
exec /entrypoint.sh "$@"
