# Dockerizing Django with Postgres, Gunicorn, and Nginx

## Want to use this project?

### Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.

### Create superuser

docker exec -it mentoro_web-prod_1 python manage.py createsuperuser
docker exec -it mentoro_web-prod_1 python manage.py makemigrations

### make migrations
docker exec -it mentoro_web_1 python manage.py makemigrations
### make migrate
docker exec -it mentoro_web-prod_1 python manage.py migrate
### make fake migrate
docker exec -it mentoro_web-prod_1 python manage.py migrate --fake
### collectstatic files
docker exec -it mentoro_web-prod_1 python manage.py collectstatic

### update repo
git pull origin master