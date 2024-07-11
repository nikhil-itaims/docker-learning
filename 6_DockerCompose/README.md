# A brief description on Docker Compose

#### What is Docker Compose?

Docker Compose is a tool specifically designed to manage multi-container applications. It simplifies the process of defining and running applications that consist of multiple interacting Docker containers.

**How it works:**

- **Define your application:** You describe your application's services (containers) and their configurations in a YAML file called docker-compose.yml (or docker-compose.yaml). This file specifies things like:
  - Which Docker image to use for each service.
  - How containers should be linked or communicate with each other.
  - Environment variables for each service.
  - Volumes to persist data.


- **Single command control:** With the docker-compose command, you can perform actions on your entire application defined in the YAML file. For example:
  - `docker-compose up` - Starts all the services defined in your application.
  - `docker-compose down` - Stops all running services.
  - `docker-compose build` - Builds images for all the services.
\
**Benefits of using Docker Compose:**

- **Simplified development workflow:** Easily spin up and manage your entire application with a single command.
- **Reproducible environments:** The YAML file ensures consistent environments across development, testing, and production.
- **Improved maintainability:** Centralized configuration makes it easier to understand and manage complex applications.


### Let's take a mern stack web app example

Building on our previous tutorial on multi-container setups, we'll revisit the same application. Previously, we managed individual containers with separate commands and a dedicated network. Docker Compose offers a streamlined approach, allowing you to run all three containers with a single command. This eliminates the need for multiple commands and simplifies the overall management process.

Here is basic **docker-compose.yaml** file

```
version: "3.8"

services:
  mongodb:
    image: mongo:latest
    container_name: mongodb

    volumes:
      - data:/data/db

  node_app:
    build: ./backend
    image: node_app_image:latest
    container_name: node_app

    ports:
      - "3001:3001"

    depends_on:
      - mongodb

  react_app:
    build: ./frontend
    image: react_app_image:latest
    container_name: react_app

    ports:
      - "3000:3000"

    depends_on:
      - node_app

volumes:
  data:

```

Breakdown of docker-compose.yaml file

- **`version: "3.8"`** - This line specifies the version of the Docker Compose file format being used. In this case, it's version 3.8. Different versions may have slight variations in syntax and supported features.

- **`services:`** - This section defines the individual services that make up your multi-container application. Each service represents a container you want to run.

- **`mongodb:`** 
  - This block defines a service named "mongodb".

  - `image: mongo:latest` - This line specifies the Docker image to use for this service. Here, it's using the official "mongo" image with the "latest" tag.

  - `container_name: mongodb` - This line assigns a custom name to the container created from this service. It's optional, but helpful for identification

  - `volumes:`
    - `data:/data/db` - This line defines a volume for the service. The local directory "data" on your host machine is mounted to the "/data/db" directory within the container. This ensures persistence of data stored by the MongoDB database.


- **`node_app:`**

  - This block defines a service named "node_app".

  - `build: ./backend` - This line instructs Docker Compose to build the image for this service from the Dockerfile located in the "./backend" directory of your project.

  - `image: node_app_image:latest` - This line assigns a tag ("node_app_image:latest") to the image built for this service.

  - `container_name: node_app` - Similar to "mongodb", this assigns a custom name to the container.

  - `ports:`
    - `"3001:3001"` - This line maps the container's port 3001 to port 3001 on your host machine. This allows you to access the Node.js application running in the container from your browser at http://localhost:3001.

  - `depends_on:`

    - `mongodb` - This line specifies that the "node_app" service depends on the "mongodb" service. This ensures the MongoDB container starts before the Node.js application container, allowing the application to connect to the database properly.

- **`react_app:`**

  - This block defines a service named "react_app". It follows a similar structure as "node_app" with a few differences:
    - It builds the image from the Dockerfile located in the "./frontend" directory.
    - It maps container port 3000 to host port 3000 for the React application.
    - It depends on the "node_app" service, ensuring the Node.js application starts before the React application attempts to connect to it.

- **`volumes:`**

  - `data` - This section defines a named volume named "data". This volume was referenced earlier in the "mongodb" service definition to persist the database data.


Now setup is done we just need to run one command to build the image and run all three containers in a same network.

Docker Compose creates a single network for all the services defined in your docker-compose.yml file. This means all the containers (mongodb, node_app, and react_app) will be able to communicate with each other using their service names (e.g., mongodb, node_app, or react_app) as hostnames.

**Running Containers in Detached Mode:**

- The command `docker-compose up -d` is accurate. The `-d` flag instructs Docker Compose to run all services defined in the **docker-compose.yml** file in detached mode. This means the containers will start in the background, allowing you to continue working on your terminal without them blocking it.

**Stopping and Removing Services:**

- You're absolutely right about `docker-compose down`. This single command effectively stops and removes all containers, networks, and volumes (by default) associated with the docker-compose project.

**Preserving or Removing Volumes:**

- By default, the `docker-compose down` command does not remove volumes. This is because volumes can be reused by other services or projects. However, you can include the `-v` flag with docker-compose down to explicitly remove volumes along with containers and networks.

| **Command**              | **Action**                                              |
| :----------------------- | :------------------------------------------------------ |
| `docker-compose up -d`   | Starts all services in detached mode (background)       |
| `docker-compose down`    | Stops and removes all containers, networks              | 
| `docker-compose down -v` | Stops and removes all containers, networks, and volumes |

