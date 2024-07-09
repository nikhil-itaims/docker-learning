# A brief description on Docker Networking

Docker networking allows you to establish communication channels between containers and other network resources. It provides a flexible and powerful way to manage inter-container and external network connectivity in your Docker applications.

### Docker Network Drivers
Docker utilizes various network drivers to manage container communication

- `bridge` - The default bridge driver creates a virtual network bridge.
- `overlay` - Used for communication across Docker swarms (clusters of Docker engines).
- `host` - Mounts containers directly onto the host machine's network stack.
- `macvlan` - Allows assigning a MAC address to a container, enabling communication on a specific network segment.
- **Custom drivers** - Integrate with external network technologies like VPNs or cloud provider networks.


### Useful Network Commands:

- `docker network create`
    - Creates a new Docker network with a specified name and driver.
    - Syntax: `docker network create [OPTIONS] <network_name>`
    - Example: `docker network create my-app-network` (creates a network named my-app-network with the default bridge driver)

- `docker network ls`
    - Lists all available Docker networks.
    - Syntax: `docker network ls [OPTIONS]`
    - Example: `docker network ls` (lists all networks)

- `docker network inspect`
    - Provides detailed information about a specific network.
    - Syntax: `docker network inspect <network_name>`
    - Example: `docker network inspect my-app-network` (displays details about my-app-network)

- `docker network connect`
    - Connects a running container to an existing network.
    - Syntax: `docker network connect <network_name> <container_name_or_id>`
    - Example: `docker network connect my-app-network my-container` (connects the container named my-container to the my-app-network)

- `docker network disconnect`
    - Disconnects a container from a network.
    - Syntax: `docker network disconnect <network_name> <container_name_or_id>`
    - Example: `docker network disconnect my-app-network my-container` (disconnects my-container from my-app-network)

- `docker network prune`
    - Removes unused Docker networks.
    - Syntax: `docker network prune [OPTIONS]`
    - Example: `docker network prune -f` (removes all unused networks, forcing deletion) (Use with caution!)


### Example of docker network wit mysql and fastapi

Let's take an example to understand how to use network and why we need them.
Here is the Dockerfile and also attached a sample todo app of fastapi which connected with mysql database in this github repo.

```
# Dockerfile

FROM python:3.8.10

ARG DB_HOST
ARG DB_USER
ARG DB_PASSWORD 
ARG DB_PORT=3306
ARG DB_NAME=todos

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV DB_URL="mysql+pymysql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
```

\
**Step 1:** Pull Docker image for mysql if you already have then ignore this step.
```
docker pull mysql:latest
```
\
**Step 2:** Create a network
```
docker network create fastapi-app-network
```
\
**Step 3:** Run mysql container using the mysql image and here is few more things to note.

Attach a created network using `--network` flag

Add environment variable for root user password `-e MYSQL_ROOT_PASSWORD=Demo123#`

```
docker run --rm --name fastapi-db -d -e MYSQL_ROOT_PASSWORD=Demo123# --network fastapi-app-network mysql:latest
```
\
**Step 4:** Now build docker image for fastapi app but note that we adding build arguments which we defined in the Dockerfile to manage environment variable in fastapi code.

**Note:** Here the **DB_HOST** is nothing but the container name which is running as mysql container. Normally we use DB_HOST as localhost or ip address of host machine and the **DB_PASSWORD** it the same which we used while creating mysql container.

```
docker build -t fastapi-todo:v1 --build-arg DB_HOST=fastapi-db --build-arg DB_USER=root --build-arg DB_PASSWORD=Demo123# .
```

\
**Step 5:** Not we can run docker container of our fastapi app by attaching the same network which we created using `--network` flag.
```
docker run -d -p 5000:5000 --name fastapi-todo-app --rm --network fastapi-app-network fastapi-todo:v1
```

Now you see the http://localhost:5000/docs where your fastapi app is running.
