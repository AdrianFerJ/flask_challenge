# flask_challenge
Flask App


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


## Resources:
* TestDriven.io Microservices [tutorial](https://testdriven.io/courses/microservices-with-docker-flask-and-react/part-one-postgres-setup/)
* Flask project layout [Docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/)
* Flask-Alchemy setup [Docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/)
* MySQL + Alchemy configuration [StackOverflow](https://stackoverflow.com/questions/9845102/using-mysql-in-flask)
* 

## TODO
* Enable entrypoint.sh in flask-api/Dockerfile, instead of `CMD python manage.py run -h 0.0.0.0`. This script will make sure the api service will wait for MySQL services to build, be up AND healthy. Need to fix Error: `standard_init_linux.go:211: exec user process caused "exec format error"` 