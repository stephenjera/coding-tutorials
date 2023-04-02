### Docker Swarm

Nodes can be considers as docker hosts e.g. another machine

Initialise a node
```shell
docker swarm init
```

Follow the instruction that appear
```shell
docker swarm join-token manager
```

Keep the token in a safe location
```shell
docker swarm join --token SWMTKN-1-3nci03phc17zne4z7mqzdqd8vnr8bimfujhx7yy65g3s5oeoco-183e01l8okn8yg5za090s11nu 192.168.65.3:2377
```

List the nodes
```shell
docker node ls
```

Join token for workers
```shell
docker swarm join-token worker
```

Set up swarm for app
```shell
docker service create --name web -p 5000:3000 --replicas 3 docker_hub_name/gsd:first-container
```

Show running service 
```shell
docker service ls
```

Show all running containers on local node 
```shell
docker container ls
```

Show container on all nodes
```shell
docker service ps web
```

Scale service 
```shell
docker service scale web=10
```

Clean up service 
```shell
docker service rm web
```

Check service is cleaned up 
```shell
docker service ls
```

Double check clean up 
```shell
docker container ls
```

