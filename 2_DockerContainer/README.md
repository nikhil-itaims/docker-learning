
# A brief description on Docker Container

#### Run docker container by docker image (Sample flask app example)

```python 
# test.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"
```


```
# Dockerfile

FROM python:3

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["flask", "--app", "test", "run", "--host=0.0.0.0"]
```

First build docker image and list docker images
```
docker build -t flask-app:v1 .
docker images
```

| REPOSITORY   |  TAG     | IMAGE ID       |  CREATED       |  SIZE    |
| :----------- | :------- | :------------- |  :------------ | :------- |
| `flask-app`  |  `v1`    | `8cc150b08961` | `1 minute ago` | `1.03GB` |

\
Now run docker container based on image id

```
docker run -p 5000:5000 d7afdb7ffdf2
```

You will see the the container is running in terminal and get output as below
```
* Serving Flask app 'test'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
* Running on http://172.17.0.2:5000
Press CTRL+C to quit
```
\
You can run container in detached mode using -d flag so our container will run in background.

```
docker run -d -p 5000:5000 d7afdb7ffdf2
```

You can run container by specifying image_name:tag rather than image id.

```
docker run -d -p 5000:5000 flask-app:v1
```

After run container in background mode you will see output after running this command (A hashed string for container)
```
b8fc8ed3690b00152d132b7c3ed0093e11100f2d1207eb466ebfed31a7d930a2
```


You can list running containers using
```
docker ps
```

You can list all (running or stopped) containers using 
```
docker ps -a
```

| CONTAINER ID   | IMAGE           | COMMAND                |  CREATED         |  STATUS             |  PORTS                                      | NAMES        |
| :------------  | :---------------| :--------------------- |  :-------------- | :------------------ | :----------------------------------------   | :-----------  |
| `b8fc8ed3690b` |  `d7afdb7ffdf2` | `flask --app test ru…` | `2 minutes ago`  | `Up About a minute` | `0.0.0.0:5000->5000/tcp, :::5000->5000/tcp` | `objective_wu` |


How to access docker container? (by specifying container id or container name)

```
# by specifying container id
docker exec -it b8fc8ed3690b bash

# by specifying container name
docker exec -it objective_wu bash
```


To stop running container (by specifying container id or container name)
```
# by specifying container id
docker stop b8fc8ed3690b

# by specifying container name
docker stop objective_wu
```

To start stopped container (by specifying container id or container name)
```
# by specifying container id
docker start b8fc8ed3690b

# by specifying container name
docker start objective_wu
```

To delete stopped container (by specifying container id or container name)

```
# by specifying container id
docker rm b8fc8ed3690b

# by specifying container name
docker rm objective_wu

```

#### Some of other docker container related commands:

**Note:** [] in commands which means optional

`docker run [OPTIONS] <image_name>[:<tag>] [command] [args]`
\
`docker run` : This is the core command to start a container.

`-d, --detached` : To run the container in the background.
\
`-i, --interactive` : To keep the standard input open for attaching to the container.
\
`-t, --tty` : To allocate a pseudo-TTY (teletype) for the container. (Useful for interactive shells)
\
`-p, --publish <host_machine_port>:<container_port>` : To map ports between the container and the host machine. (e.g., -p 8080:80)
\
`-v, --volume <host_path:container_path>` : To mount volumes from the host machine into the container.
\
`-e, --env <key=value>` : To set environment variables for the container.
\
`--name <container_name>` : To assign a name to the container.
\
`-m, --memory <memory_limit>` : To set the memory limit for the container.
\
`-c, --cpu-shares <cpu_shares>` : To set the CPU share for the container.
\
`--user <username>` : To specify the user inside the container to run the process.
\
`<image_name>[:<tag>]` : This specifies the name of the Docker image you want to run, optionally including a tag (e.g., ubuntu:latest).


\
Here are some examples of docker run commands with arguments:

Run a container in detached mode and publish port 80:
```
docker run -d -p 80:80 nginx:latest
```

Run a container interactively and allocate a pseudo-TTY:
```
docker run -it ubuntu:latest bash
```
Run a container with a custom environment variable:
```
docker run -e DB_HOST=localhost mysql:latest
```
Mount a volume from the host and set a memory limit:
```
docker run -v ~/data:/app/data -m 1g myapp:v1.0
```