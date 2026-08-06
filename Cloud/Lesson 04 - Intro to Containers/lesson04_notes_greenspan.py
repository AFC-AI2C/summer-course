#Linux Commands
docker --version  #Only version of CLI, not version of engine
docker image pull alpine  #If runs, docker engine is already running. If not, can open up Docker Desktop to get it running.
docker --help
docker image --help  #Only images commands.
docker image list #Only local.
'''
alpine:latest   28bd5fe8b56d 
'''
#latest is a 'tag'
#container ID is a hash
docker image pull -a alpine #Docker is very picky about where place options. Here have to place options between pull and name!
#Anything in square brackets is optional.
docker image pull ubuntu:24.04
docker image pull ubuntu:latest
#Can look up tags on https://hub.docker.com/_/ubuntu
docker image inspect alpine #An image is just some metadata
docker container --help  #run, start, and stop
docker container run --help  #Usage:docker container run [OPTIONS] image
docker container run ubuntu
docker container run nginx #Will go find, download, and run.
docker container --help
docker container list #Where did my container go? I ran it.
docker contain list --help #-a says show all containers, default shows just running
docker container list -a #If you don't specify a name, it will build you a name.
docker container run alpine
docker container list -a
#Command is the first thing that runs when you open up that container.
#Ports shows exposed ports.

#Let's talk about commands. Exiting a process returns a status code, e.g., 0. When container does its job, it shuts down. Container kills itself. 

-i #interactive, -tty #teletype
docker container run -interactive -tty alpine
#same as
docker container run -it alpine #Starts in interactive, teletype.
apk add curl
curl google.com
docker container list-a #Shows 2 alpines, the one from earlier is from the run command, every time you execute run it starts a new container
docker container start --help
docker container list-a #To see container IDs.
docker container start -i

docker container start -i amazing_swirlies
docker container start -i 9
docker container list -a
docker container start -i 14c #first digits of hash
docker container --help
docker container exec --help
docker container exec fae8 /bin/ls #Want it to run the ls command
#exec has to be in a running container. The command won't run unless exec is in a running container.
docker container start -i
docker container exec fae8 /bin/ls #Run a command inside a running container and results will print out locally. That is what the exec command is for.
#I have something running. I can use exec to peer into my container without opening my terminal. There is no authentication for that exec.

docker container list -a #[COMMAND] argument will change COMMAND in list -a
docker container run -it ubuntu
#A lot of images are as tiny as possible, so ping won't be installed.
docker container run ubuntu cat /etc/passwd #NMAP?, CALI?
docker container list -a #Notice COMMAND will change
#Might just build a CALI image or an image that has a bunch of tools, run that image, look at the output, then the container stops
docker container list -a
docker container stop fae
docker container stop -f fae
docker container stop -t 0 fae
docker container prune #Removes all stopped containers.

docker container run -itd alpine
docker contain list #validate: -d flag means detached "run it in the background"
docker container run -itd alpine
docker container list
docker container exec --help
docker container exec -it c16 /bin/sh
curl google.com
apk add curl
docker container list
docker container exec -it f78 /bin/sh
curl #expect not found
docker container run -it alpine
curl google.com #not found
#shim [thing on top], things get written in container there
#if not a mounted location, then it just gets written to the shim


#####

docker image pull busybox
docker image save -o busybox.tar busybox
tar tvf busybox.tar
tar xf busybox.tar

docker buildx build -t django_app:latest
#python -m pip install Django #command to install django, needs pip
# As you watch this, you can see it is running all those, it makes each as a layer
# Can has each layer separately.
#diff file
#When run second time, much faster. Each layer was hashed. Can cache hashes. Only rebuild things that were changed.
#GOTCHA: changing order changes hashes, have to rebuild everything
#In build pipline, often force line to run.
