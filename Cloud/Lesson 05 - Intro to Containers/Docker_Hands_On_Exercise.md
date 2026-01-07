# Docker Hands-On

## Hands-On #1: Working with Containers

These exercises introduce Docker containers, running them, interacting
with them, and managing their lifecycle using the Docker CLI.  It is meant to be exploratory,
if you run into issues, please consult the solution.

You should make extensive use of the `--help` flag and a docker cheatsheet.
[Here](https://docs.docker.com/get-started/docker_cheatsheet.pdf) is one example

------------------------------------------------------------------------

### Exercise 1: Install Docker & Run Your First Container

**Goal**: Verify Docker installation and run a basic container.

1.  Confirm Docker is installed.
2.  Run the `hello-world` container.

------------------------------------------------------------------------

### Exercise 2: Managing Docker Containers

**Goal**: Practice listing, running, stopping, and removing containers.

-   Find the command to list all containers.
-   Run an image in detached mode.
-   View running containers.
-   Stop a running container.
-   Restart a stopped container.
-   Remove a container.
-   List all containers again.

------------------------------------------------------------------------

### Exercise 3: Interacting with Running Containers

**Goal**: Use `exec` to access containers and observe state persistence.

1.  Start a detached `httpd` container.
2.  Access a shell inside it.
3.  Update packages and install vim.
4.  Start a new `httpd` container --- reflect on whether vim should be
    installed.
5.  Restart the original container --- reflect on whether vim should
    still be installed.

------------------------------------------------------------------------

## Hands-On #2: Working with Images

### Exercise 1: Discovering Docker Images

**Goal**: Search, pull, and list images.

-   Search for the official Python image.
-   Pull the latest Python image.
-   Pull an older version.
-   List all images on your system.

------------------------------------------------------------------------

### Exercise 2: Inspect & Explore Image History

**Goal**: Investigate layers and metadata of images.

-   Inspect the Python image.
-   View the image history.

------------------------------------------------------------------------

### Exercise 3: Managing Docker Images

**Goal**: Tag and remove images.

-   Tag the Python image.
-   Run a container using the new tag.
-   Remove an unused image.

------------------------------------------------------------------------

### Exercise 4: Image Size Comparison

**Goal**: Compare the sizes and understand when size matters.

-   Pull ubuntu, alpine, and busybox.
-   Compare their sizes.
-   Discuss scenarios where image size matters.

------------------------------------------------------------------------

### Exercise 5: Build an Image from a Modified Container

**Goal**: Create an image by committing container changes.

1.  Start an Ubuntu container.
2.  Update packages and install a tool inside it.
3.  Commit the container into a new image.
4.  Run the new image and verify changes persisted.

------------------------------------------------------------------------

## Hands-On #3: WordPress Deployment with Docker

### Exercise 1: Create Persistent Volume

-   Create a Docker volume named `wordpress_data`.

### Exercise 2: Create a Private Network

-   Create a Docker network named `wordpress_network`.

### Exercise 3: Run MySQL Container

-   Start a MySQL container on the new network.
-   Use a root password.
-   Store data in the created volume.

### Exercise 4: Create WordPress Database

-   Connect to the MySQL container.
-   Create a new database called `wordpress`.

### Exercise 5: Run WordPress Container

-   Start a WordPress container.
-   Connect it to the same network.
-   Expose port 80 to port 8080 on the host.
-   Visit `localhost:8080` to finish setup.

------------------------------------------------------------------------

## Hands-On #4: Task Program Deployment with Docker

### Exercise 1: Make commands.sh script executable

-   Change permissions on commands.sh to make it executable.

### Exercise 2: Run commands.sh script

-   Execute commands.sh script.

### Exercise 3: Navigate and view program interface

-   Find how to navigate and view program in web browser (view startup.sh).

### Exercise 4: Verify program is working

-   Create 'test' task in program to verify proper operation.

### Exercise 5: Stop container program is running in

-   Stop container to end program.

------------------------------------------------------------------------

## Helpful Commands (Linux)

These are intentionally omitted here so students can research them
independently.

  Purpose:                     Command
  --------------------------- --------------------------------
  Remove all containers:       <*Fill in the correct command.*>

  Remove all images:           <*Fill in the correct command.*>

  Remove stopped containers:   <*Fill in the correct command.*>

  Remove unused images:        <*Fill in the correct command.*>

  Remove unused networks:      <*Fill in the correct command.*>
