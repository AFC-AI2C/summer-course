#!/bin/sh
docker buildx build -t todo_django:latest .

docker image inspect todo_django
docker image inspect todo_django | jq .[0].RootFS

docker image pull python:3.12-alpine
docker image inspect python:3.12-alpine | jq .[0].RootFS

mkdir data
chmod 777 data 2>/dev/null || true  
chmod 666 data/*.sqlite3 2>/dev/null || true
docker container run --rm -v ./data:/data -p 8080:8000 todo_django
docker container list

docker container exec -it <container_name> /bin/sh
docker inspect --format "{{json .State.Health }}" <container_name> | jq

docker image save -o busybox.tar busybox
tar tvf busybox.tar
tar xf busybox.tar -C busybox/
cat manifest.json