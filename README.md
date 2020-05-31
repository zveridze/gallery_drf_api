# Gallery api server.

## How to start
#### Docker way
1. ```git clone``` this repo
2. ```docker-compose up -d```

#### Manual way
1. ```git clone``` this repo 
2. run django server ```python manage.py runserver```

## Endpoints:
1. admin/ - django admin
2. api/v1/ pictures/ (GET, POST)
3. api/v1/ pictures/<int:pk> (GET, PUT, DELETE)
4. api/v1/ comments/ (GET, POST)
5. api/v1/ comments/<int:pk> (GET, PUT, DELETE)
6. api/v1/ likes/ (GET, POST)
7. api/v1/ likes/<int:pk> (DELETE)
8. api/v1/ login/ (POST)
9. api/v1/ logout/ (POST)
10. api/v1/ registration/ (POST)