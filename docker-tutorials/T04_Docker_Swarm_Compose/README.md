### Deploying a stack 

Deploy stack, counter is the name of app
```shell
docker stack deploy -c docker-compose.yml counter
```

See running stacks 
```shell
docker stack ls
```

See more details of stack 
```shell
docker stack services counter
```

See each container 
```shell
docker stack ps counter
```

Remove stack 
```shell
docker stack rm counter
```