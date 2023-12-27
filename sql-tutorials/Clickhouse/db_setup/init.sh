#!/bin/bash

# Run clickhouse-client on the container
docker exec -it clickhouse bash -c "
  clickhouse-client --user admin --password \$ADMIN_PASSWORD --multiquery '
    CRATE DATABASE IF NOT EXISTS analytics;
  '  
"
