# A brief description on Docker Container

Docker volumes provide a mechanism for persisting data used by Docker containers. They offer several advantages over storing data directly within containers:

**Persistence:** Data volumes survive container restarts, unlike data stored in the container's writable layer.
\
**Sharing:** Volumes can be mounted by multiple containers, enabling data sharing between them.
\
**Flexibility:**: Volumes are independent of container lifecycles, allowing you to manage data separately from container images.

Here's a deeper dive into key concepts and considerations:

**Volume Types**

**Local Volumes:** These are directories on the Docker host machine that are mounted into containers. They're suitable for development and simple data storage.
\
**Named Volumes:** These are volumes explicitly created and managed by Docker. They're useful for sharing data between containers or persisting data across container restarts.
\
**External Volumes:** These leverage plugins to integrate Docker with external storage providers like cloud storage or network-attached storage (NAS).

#### Run docker container by docker image (Sample flask app example)

```python 
# main.py

from fastapi import FastAPI, UploadFile
import os
import uuid

app = FastAPI()

UPLOADS_FOLDER = "uploads"

@app.get("/")
async def home():
    return {"message": "Welcome to Docker tutorial on volume"}

@app.get("/list-files/")
async def list_files():
    try:
        files = os.listdir(UPLOADS_FOLDER)
        return {"files": files}
    except Exception as e:
        return {"message": f"Error while loading files: {str(e)}"}

@app.post("/upload-file")
async def upload_file(file: UploadFile):
    try:
        filename = file.filename
        file_extension = filename.split(".")[1]
        filepath = os.path.join(UPLOADS_FOLDER, f"{str(uuid.uuid4())}.{file_extension}")

        with open(filepath, "wb") as f:
            f.write(file.file.read())

        return {"message": "File uploaded successfully"}
    
    except Exception as e:
        return {"message": f"Error uploading file: {str(e)}"}
```


```
# Dockerfile

FROM python:3.8.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
```

First build docker image and list docker images
```
docker build -t fastapi-app-image:v1 .
docker images
```

| REPOSITORY           |  TAG     | IMAGE ID       |  CREATED       |  SIZE    |
| :------------------- | :------- | :------------- |  :------------ | :------- |
| `fastapi-app-image`  |  `v1`    | `8cc150b08961` | `1 minute ago` | `1.03GB` |

\
Now we are running container using below command

```
docker run -d -p 5000:5000 --rm --name fastapi-app fastapi-app-image:v1
```
Our fastapi app is running now and we can upload file in it.
\
The problem: -
When we container stop container or create new container we lose our files stored which we uplaoded. To overcome this issue we can attach volume to container.

\
Now we are adding named volume for managing persistent data 

```
docker run -d -p 5000:5000 --rm --name fastapi-app -v uploads:/app/uploads fastapi-app-image:v1
```

The fastapi app uploads folder now connected with host machines volume. Now whenever container stops or container is being created you can get all files stored from volume.


Creating and Managing Volumes:

`docker volume create <volume_name>` : Creates a named volume.
\
`docker volume inspect <volume_name>` : Shows details about a volume.
\
`docker volume ls` : Lists all volumes.
\
`docker volume rm <volume_name>` : Delete specific volume.
\
`docker volume prune` : Removes unused volumes (use with caution).
