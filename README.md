# flask-docker-course

python+flask+docker+sklearn

Для запуска приложения выполнить

git clone https://github.com/andBabaev/flask-docker-course.git

cd flask-docker-course/for_heroku

heroku login

heroku container:login

heroku create <name>
  
heroku container:push web -a <name>
  
heroku container:release web -a <name>
  
heroku open -a <name>
  
  
Полезные команды

heroku apps

heroku container:rm web -a andbabaev-docker-flask
