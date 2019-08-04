# flask_challenge
Flask App

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

## API usage example

* Run commands in python (make sure to `import requests`).


### Get all comments

```python
URL = 'http://localhost:5000/'
r = requests.get(URL)
r.status_code # 200
r.json()
# {'cm1': {'title': 'First comment', 'text': 'first text'}, 'cm2': {'title': '2nd comment', 'text': 'not much text'}, 'cm3': {'title': 'No title?', 'text': '???'}}
```

### Post new comment

```python
new_comment = json.dumps({
    'title': 'Any title',
    'text' : 'An appropirate text. Can be anything'
})
r = requests.post(URL, data = new_comment)
r.status_code # 201
r.json()
# {'title': 'Any title', 'text': 'An appropirate text. Can be anything'}
```

## Thanks to this good resources

- Easy WebSockets with Flask and Gevent [blog](https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent)
