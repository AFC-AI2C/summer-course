# Docker Hands-On

## Hands-On #1: Working with Containers

These exercises introduce Docker containers, running them, interacting
with them, and managing their lifecycle using the Docker CLI.

------------------------------------------------------------------------

### Exercise 1: Install Docker & Run Your First Container

**Goal**: Verify Docker installation and run a basic container.

1.  Confirm Docker is installed:

``` bash
docker --version
```
or

``` bash
docker info
```


2.  Run the `hello-world` container:

``` bash
docker run hello-world
```

✅ *Check*: You should see a message confirming that Docker ran the
image successfully.

------------------------------------------------------------------------

### Exercise 2: Managing Docker Containers

**Goal**: Practice listing, running, stopping, and removing containers.

-   List **all** containers (running + stopped):

``` bash
docker container ls --all
```

or

``` bash
docker ps --all
```

-   Run a container in **detached mode** using `nginx`:

``` bash
docker run -d nginx
```

-   List currently running containers:

``` bash
docker container ls
```

or

``` bash
docker ps
```

-   Stop a running container (replace `<id>`):

``` bash
docker container stop <id>
```

or

``` bash
docker stop <id>
```

-   Restart a stopped container:

``` bash
docker container start <id>
```

or

``` bash
docker start <id>
```

-   Remove a stopped container:

``` bash
docker container rm <id>
```

or

``` bash
docker rm <id>
```

-   List all containers again:

``` bash
docker container ls --all
```

or

``` bash
docker ps --all
```

------------------------------------------------------------------------

### Exercise 3: Interacting with Running Containers

**Goal**: Use `exec` to access containers and observe state persistence.

1.  Start a detached `httpd` container:

``` bash
docker run -d httpd
```

2.  Access its shell with an interactive tty session:

``` bash
docker exec -it <id> bash
```

3.  Inside the container, update packages and install vim:

``` bash
apt update
apt install -y vim
```

4.  Start a **new** `httpd` container.\
    **Do you expect vim to be installed?**

5.  Stop and restart the **original** container.\
    **Do you expect vim to still be installed?**

------------------------------------------------------------------------

## Hands-On #2: Working with Images

### Exercise 1: Discovering Docker Images

**Goal**: Search, pull, and list images.

-   Search for the official Python image:

``` bash
docker search python
```

-   Pull the latest Python image:

``` bash
docker pull python:latest
```

-   Pull an older version:

``` bash
docker pull python:<version>
```

-   List all images:

``` bash
docker image ls
```
or

``` bash
docker images
```

------------------------------------------------------------------------

### Exercise 2: Inspect & Explore Image History

**Goal**: Investigate layers and metadata of images.

-   Inspect the Python image:

``` bash
docker image inspect python
```

-   View the layer history:

``` bash
docker image history python
```

------------------------------------------------------------------------

### Exercise 3: Managing Docker Images

**Goal**: Tag and remove images.

-   Tag the Python image:

``` bash
docker tag python python:mytag
```

-   Run a container using your new tag:

``` bash
docker run python:mytag
```

-   Remove an unused image:

``` bash
docker image rm <image>
```

or

``` bash
docker rmi <image>
```

-   Remove all unused images:

``` bash
docker image prune
```

------------------------------------------------------------------------

### Exercise 4: Image Size Comparison

**Goal**: Compare the sizes and understand when size matters.

Pull images:

``` bash
docker pull ubuntu:latest
docker pull alpine:latest
docker pull busybox:latest
```

List sizes:

``` bash
docker image ls
```

or

``` bash
docker images
```

------------------------------------------------------------------------

### Exercise 5: Build an Image from a Modified Container

**Goal**: Create an image by committing container changes.

1.  Start an Ubuntu container:

``` bash
docker run -it ubuntu bash
```

2.  Inside the container:

``` bash
apt update
apt install -y curl
```

3.  Commit the container:
    1.  exit Ubuntu shell
    2.  find container_id by listing **all** containers (running + stopped)

``` bash
docker commit <container_id> ubuntu:custom
```

4.  Run your new image:

``` bash
docker run -it ubuntu:custom bash
```

------------------------------------------------------------------------

## Hands-On #3: WordPress Deployment with Docker

### Exercise 1: Create Persistent Volume

``` bash
docker volume create wordpress_data
```

### Exercise 2: Create a Private Network

``` bash
docker network create wordpress_network
```

### Exercise 3: Run MySQL Container

``` bash
docker run -d   --name wordpress_mysql   --network wordpress_network   -v wordpress_data:/var/lib/mysql   -e MYSQL_ROOT_PASSWORD=<your-password>   mysql:latest
```

### Exercise 4: Create WordPress Database

``` bash
docker exec -it wordpress_mysql mysql -u root -p
```

Inside MySQL:

``` sql
CREATE DATABASE wordpress;
```

### Exercise 5: Run WordPress Container

``` bash
docker run -d   --name wordpress_web   --network wordpress_network   -p 8080:80   -e WORDPRESS_DB_HOST=wordpress_mysql   -e WORDPRESS_DB_USER=root   -e WORDPRESS_DB_PASSWORD=<your-password>   wordpress:latest
```

Visit:

    http://localhost:8080

------------------------------------------------------------------------

## Hands-On #4: Task Program Deployment with Docker

### Exercise 1: Make commands.sh script executable

``` bash
chmod +x commands.sh
```

### Exercise 2: Run commands.sh script

``` bash
./commands.sh

```
or

``` bash
sudo ./commands.sh
```

### Exercise 3: Navigate and view program interface

visit http://localhost:8080/todo

### Exercise 4: Verify program is working

-   Create 'test' task using GUI in web browser

### Exercise 5: Stop container program is running in

``` bash
docker container stop <id>
```

## Helpful Commands (Linux)

  -----------------------------------------------------------------------------------------------------------------
  Purpose                           Command
  --------------------------------- -------------------------------------------------------------------------------
  Remove all containers             `docker container rm $(docker container ls --all --quiet)`

  Remove all images                 `docker image rm $(docker image ls --all --quiet)`

  Remove stopped containers         `docker container rm $(docker container ls --filter "status=exited" --quiet)`

  Remove unused images              `docker image prune --all`

  Remove unused networks            `docker network prune`

  -----------------------------------------------------------------------------------------------------------------
