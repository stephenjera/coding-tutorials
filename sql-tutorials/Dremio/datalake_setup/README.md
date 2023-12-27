# Setting up connection

Watch [this](https://www.youtube.com/watch?v=G_dbypufGXc) video

## Properties

### nessie source

- name: nessie
- url: <http://nessie:19120/api/v2>

### Bucket setting in advanced

- aws access key = admin
- aws access secret = password (minio user and password)
- turn off encryption

#### connection properties

- fs.s3a.path.style.access = true
- fs.s3a.endpoint = ip address:port (minio:9000) can also use the name of docker container service
- dremio.s3.compat = true

- <https://github.com/hnawaz007/pythondataanalysis/blob/main/data-lakehouse/docker-compose.yml>

Dremio can't write to folder for some reasons

- sudo chmod -R 777 dremio_data

### Dremio user

- username: docker
- password: Docker123
- email: <test@mail.com>

```sql
CREATE BRANCH IF NOT EXISTS dev in nessie;
USE BRANCH dev IN nessie;
CREATE FOLDER IF NOT EXISTS superstore;
CREATE TABLE IF NOT EXISTS nessie.superstore.orders AS
SELECT * FROM testing."global_superstore"."global_superstore_orders_2018.csv";
```
