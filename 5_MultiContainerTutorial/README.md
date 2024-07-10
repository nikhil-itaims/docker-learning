# A brief description on multi container setup with docker

This guide outlines the steps to deploy a multi-container application using Docker, consisting of a Node.js backend (presumably a React frontend) and a MongoDB database.


**Step 1 :** Create a network
```
docker network create multi-container-app
```
**Step 2 :** Pull official mongo image and run mongodb with our network

```
docker pull mongo:latest

docker run --network multi-container-app --name mongodb --rm -d mongo:latest
```

**Step 3 :** Now go to backend folder and build the image

Note - Just change database connection as per **mongo container name** inside app.js

```
mongoose.connect(
  'mongodb://mongodb:27017/course-goals', # old connection string 'mongodb://localhost:27017/course-goals',
  {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  },
  (err) => {
    if (err) {
      console.error('FAILED TO CONNECT TO MONGODB');
      console.error(err);
    } else {
      console.log('CONNECTED TO MONGODB');
      app.listen(3001);
    }
  }
);
```
Now build image and run the container with network so our node app easily communicate with mongodb container
```
docker build -t node-app-image:latest .

docker run --network multi-container-app --name node-app --rm -d -p 3001:3001 node-app-image
```

**Step 4 :** Now we are at the last stage of this deployment. Change directory to frontend and build the docker image and run the container with network so our node app easily communicate with node app container
```
docker build -t react-app-image:latest .

docker run --network multi-container-app --name react-app --rm -d -p 3000:3000 react-app-image:latest
```

