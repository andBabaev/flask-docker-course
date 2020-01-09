sudo docker run -p 8888:8888 jupyter/scipy-notebook:17aba6048f44

sudo docker run -v /home/andrei/docker:/home/jovyan/ -p 8888:8888 jupyter/scipy-notebook:17aba6048f44

sudo docker run -v /home/andrei/docker:/home/jovyan/ -p 8888:8888 .

docker build docker_test .

sudo docker run -v /home/andrei/docker:/home/jovyan/ -p 8888:8888  19859ffb4c5d
sudo docker run -v /home/andrei/docker:/home/jovyan/ -p 8888:8888  docker_test

docker exec -it 75ebd2ab088e bash
docker exec -it -u root docker_jupyter_1 bash

docker cp wine.data 75ebd2ab088e:/home/jovyan/wine.data

docker-compose up