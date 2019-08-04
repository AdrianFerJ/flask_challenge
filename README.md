# flask_challenge

The challenge :

[-]  Prepare on docker a MySQL (for comments) *BUG* Docker image is set, but can't get Flask to migrate model to db. Temporarily witched back to an old sqlite db for demo.

[X] Prepare a web server (on Docker) to Host a comment website where people will have a section to post comments. Backend is Flask.

[-] Create a front end can be generated with Flask or be on Angular or React. *Incomplete* 

[x] Use websockets to enable live updates (When comments are posted, they will be displayed on the website instantly. If I open two tabs in my browser I should be able to see the previous feed and see live what’s happening.

[] If user clicks on the name of someone (list of comments) it will trigger a mailto hyperlink

[] Host docker image on docker hub

## Setup for development

*Note* Run from flask-app project

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
# If succesfull, it will display (in logs):
# server_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
