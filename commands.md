Docker

sudo docker run -p 8888:8888 jupyter/scipy-notebook:17aba6048f44

sudo docker run -v /home/andrei/docker:/home/jovyan/ -p 8888:8888 jupyter/scipy-notebook:17aba6048f44

sudo docker run -v /home/andrei/docker:/home/jovyan/ -p 8888:8888 .



sudo docker run -v /home/andrei/docker:/home/jovyan/ -p 8888:8888  19859ffb4c5d
sudo docker run -v /home/andrei/docker:/home/jovyan/ -p 8888:8888  docker_test

docker exec -it 75ebd2ab088e bash
docker exec -it -u root docker_jupyter_1 bash

docker cp wine.data 75ebd2ab088e:/home/jovyan/wine.data

docker build docker_test .

docker-compose up --build

Сервер

curl localhost:5000/iris_post --data '{"flower": "1,2,3,4"}' --header 'Content-Type: application/json' --request POST 

heroku create <name>
heroku container:push web -a andbabaev-docker-flask
heroku container:release web -a andbabaev-docker-flask
heroku open -a andbabaev-docker-flask

pip freeze > requirements.txt

heroku container:rm web -a andbabaev-docker-flask