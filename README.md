### Technologies used:

- Python/Django-rest framework
- Bash scripting
- Docker/Docker compose

# How to run the application

```
$ docker-compose up -d --build

```

- How to stop the application and delete docker volumes

```
$ docker-compose down --volumes  # deletes persistent data
```

- Show status of running containers by running 
```
$ docker-compose ps
```
- It will show

```
annie@annies-mbp~/Documents/ratestask/ratetask> (main)docker-compose ps
       Name                      Command               State                    Ports                 
------------------------------------------------------------------------------------------------------
ratetask_pgadmin_1    /entrypoint.sh                   Up      443/tcp, 0.0.0.0:5050->5050/tcp, 80/tcp
ratetask_postgres_1   docker-entrypoint.sh postgres    Up      5432/tcp                               
ratetask_ratetask_1   /bin/sh ./entrypoint.sh py ...   Up      0.0.0.0:8080->8080/tcp 
```

# How to view logs for each service

Run docker-compose logs -f <service_name> in your terminal for example

- Database

```
annie@annies-mbp~/Documents/ratestask/ratetask> (main)docker-compose logs postgres
Attaching to ratetask_postgres_1
postgres_1  | The files belonging to this database system will be owned by user "postgres".
postgres_1  | This user must also own the server process.
postgres_1  | 
postgres_1  | The database cluster will be initialized with locale "en_US.utf8".
postgres_1  | The default database encoding has accordingly been set to "UTF8".
postgres_1  | The default text search configuration will be set to "english".
postgres_1  | 
postgres_1  | Data page checksums are disabled.
postgres_1  | 
postgres_1  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
postgres_1  | creating subdirectories ... ok
postgres_1  | selecting dynamic shared memory implementation ... posix
postgres_1  | selecting default max_connections ... 100
postgres_1  | selecting default shared_buffers ... 128MB
postgres_1  | selecting default time zone ... Etc/UTC
postgres_1  | creating configuration files ... ok
postgres_1  | running bootstrap script ... ok
postgres_1  | performing post-bootstrap initialization ... ok
postgres_1  | syncing data to disk ... ok
```

# More docker commands

View all your docker images

```
$ docker image ls
```

Stop all running containers

```
$ docker-compose down
```

You can bring everything down, removing the containers entirely, with the down command. Pass --volumes to also remove the data volume

```
$ docker-compose down --volumes
```

When you make a change within the codebase, you will need to build and restart the application by running this command

```
$ docker-compose build && docker-compose up -d
```

View docker volumes

```
$ docker volume ls
```

Delete docker volumes

```
$ docker volume rm -f <volume_name>
```

View docker containers

```
$ docker container ls
```

# The .env file

The .env file is the one that contains all your configurations, generated keys and passwords, etc.

Depending on your workflow, you could want to exclude it from Git, for example if your project is public. In that case, you would have to make sure to set up a way for your CI tools to obtain it while building or deploying your project.

One way to do it could be to add each environment variable to your CI/CD system, and updating the docker-compose.yml file to read that specific env var instead of reading the .env file. Happy
