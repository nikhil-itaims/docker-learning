
# A brief description on Docker Image

#### List or find docker images 
\
To list all images available locally
```
docker images
```

Optionally you can filter image by repository
```
docker images repository-name
```

Optionally you can filter image by tag
```
docker images tag-name
```

Optionally you can filter image by repository and tag name
```
docker images repository-name:tag-name
```

Optionally you can filter image by tag name (In case you have multiple images with same tag)
```
docker images *:tag-name
```

# Build docker image


```python 
# test.py

print("Hello World!")
```


```Dockerfile
# Sample docker file

FROM python:3

WORKDIR /app

COPY test.py /app

```

To build docker image
```
docker build .
docker images
```

| REPOSITORY | TAG       | IMAGE ID       |  CREATED         |  SIZE    |
| :--------- | :-------- | :-----------   |  :-------------- | :------- |
| `<none>`   |  `<none>` | `4ca998804211` | `55 minutes ago` | `1.02GB` |

\
You can specify docker image name and tag for identification
```
docker build -t tutorial-1:v1 .
docker images
```

| REPOSITORY   | TAG      | IMAGE ID       |  CREATED         |  SIZE    |
| :----------- | :------- | :------------- |  :-------------- | :------- |
| `tutorial-1` |  `v1`    | `4ca998804211` | `55 minutes ago` | `1.02GB` |


#### Some of other docker images related commands:

**Note:** [] in commands which means optional

`docker image inspect <image_name>[:<tag>]` : Shows detailed information about a specific image.
\
`docker pull <image_name>[:<tag>]` : Downloads an image from a Docker registry (e.g., Docker Hub).
\
`docker push <image_name>[:<tag>]` : Uploads an image to a Docker registry (requires proper permissions).
\
`docker tag <source_image> <target_image>` : Creates a new tag for an existing image.
\
`docker image rm <image_name>[:<tag>]` : Removes an image.
\
`docker image prune -a` : Removes all dangling images (unused images without containers referencing them).
\
`docker save <image_name>[:<tag>] > <image_file.tar>` : Saves an image to a tar archive file.
\
`docker load < <image_file.tar>` : Loads an image from a tar archive file.
\
`docker search <term>` : Searches for images on Docker Hub based on a keyword.


#### These are flags that modify the build behavior. Some common options include:

`-t, --tag image_name:tag` : To specify a name and tag for the image you're building. (e.g., -t myapp:latest)
\
`-f, --file <file>` : To specify a Dockerfile path other than the default Dockerfile.
\
`-c, --cache-from images` : To build the image using the cache from existing images.
\
`-m, --memory memory_limit` : To set the memory limit for the build process.
\
`--rm` : To remove the intermediate container used for building after the process is complete.
\
`-v, --volume host_path:container_path` : To mount volumes during the build process.