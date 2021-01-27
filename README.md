# vcokltfre/compliment-api

## This is a simple API that lets you compliment people

Usage: send a GET request to `/compliment/random/{name}` and the API will return a JSON object looking like this:

```json
{
    "status":"ok",
    "compliment":"{name} is an impressive genius"
}
```

Here's a simple python program to get an compliment for a name:

```py
from requests import get

def compliment(name: str):
    result = get(f"http://localhost:6969/compliment/random/{name}").json()
    return result['compliment']

print(compliment("Bob"))
```

---

## API Routes

### `GET /`
Retuns a list of endpoints.

### `GET /compliment/random`
Return an compliment for a random name.

### `GET /compliment/random/{name}`
Return an compliment for a name.

### `GET /compliment/random/{name}/{amount}`
Return a list of compliments for a name, to a maximum of 32.

### `GET /compliment/randomdouble`
Return an compliment with 2 adjectives for a random name.

### `GET /compliment/randomdouble/{name}`
Return an compliment with 2 adjectives for a name.

### `GET /compliment/randomdouble/{name}/{amount}`
Return a list of compliments with 2 adjectives for a name, to a maximum of 32.

---

### Server Setup

- Make a copy of `docker-compose.example.yml` called `docker-compose.yml`
- Run `docker-compose up -d`
- By default the server runs on port 6969, but this can be changed in `docker-compose.yml`

---

### Contributing

More adjectives and nouns are always welcome to be added to `data/random.json`, just add some and make a pull request.