# flask_challenge

The challenge :

[-]  Prepare on docker a MySQL (for comments) *BUG* Docker image is set, but can't get Flask to migrate model to db. Temporarily witched back to an old sqlite db for demo.

[X] Prepare a web server (on Docker) to Host a comment website where people will have a section to post comments. Backend is Flask.

[X] Create a front end can be generated with Flask or be on Angular or React.

[x] Use websockets to enable live updates (When comments are posted, they will be displayed on the website instantly. If I open two tabs in my browser I should be able to see the previous feed and see live what’s happening.

[X] If user clicks on the name of someone (list of comments) it will trigger a mailto hyperlink

[] Host docker image on docker hub

## Setup for development

*Note* Run from flask-app project using Python virtual env

```bash
# set virtual env
$ python3.7 -m venv env
$ source env/bin/activate

# install requirements
$ (env) pip install -r requirements.txt

# Create db (Sqlite) -> comments.db
$ (env) python create_db.py

# Run App
$ python app.py

# Run tests (app shouldn't be running)
$ python test_app.py
```

## Run App with Docker

*Note* Run from root project

```bash
# Build containers using composer
$ docker-compose build

# Start services (add -d to run detached)
$ docker-compose up

# Run tests
$ docker-compose exec server python test_app.py

# Check logs (if running detached)
$ docker-compose logs
# If succesfull, it will display the port where app is running:
# server_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

## Thanks to these great resources

- Flaskr tutorial [mjhea0](https://github.com/mjhea0/flaskr-tdd#add-some-color)
- Websockets with flask and jQuery in the forntend[miguel grinberg](https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent)
- Dockerizing flask and a more complex project layout [tdd.io](https://testdriven.io/courses/microservices-with-docker-flask-and-react/part-one-getting-started/)
- MySQL config (grr) [docker-docs](https://docs.docker.com/samples/library/mysql/) [Max Goh](https://medium.com/free-code-camp/how-to-develop-a-flask-graphql-graphene-mysql-and-docker-starter-kit-4d475f24ee76) [Stav Shamir](https://medium.com/@shamir.stav_83310/dockerizing-a-flask-mysql-app-with-docker-compose-c4f51d20b40d)
- And of course the Docs for Flask, sql-alchemy, socketio, flask-socketio, etc. as well as a few other resources that helped me in one or another way.
