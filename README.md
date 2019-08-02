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
