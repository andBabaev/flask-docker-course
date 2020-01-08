docker exec -it flaskhello_flask_1 bash

curl localhost:5000/iris_post --data '{"flower": "1,2,3,4"}' --header 'Content-Type: application/json' --request POST 
