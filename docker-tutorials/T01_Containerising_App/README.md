# Commands to run in terminal

docker_hub_name/repository:container_name .

```shell
docker image build -t docker_hub_name/gsd:first-container .
```

Push to docker hub
```shell
docker image push docker_hub_name/gsd:first-container
```

If image is not local it will search docker hub
```shell
docker container run --name web -p 5000:3000 docker_hub_name/gsd:first-container
```

Stop docker container
```shell
docker container stop web
```

Show all containers 
```shell
docker container ls -a
```

Start container again
```shell
docker container start web
```

delete container 
```shell
docker container rm web
```