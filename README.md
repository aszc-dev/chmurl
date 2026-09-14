# chmURL ☁️

A DRF server for URL shortening.

## Installation

First, clone the repository using git:

```sh
git clone git@github.com:aszc-dev/chmurl.git && cd chmurl
```

Then, proceed to setup with uv.

> [!NOTE]
> Visit https://github.com/astral-sh/uv to learn more on how to install and use uv.

```sh
uv sync                     # install the dependencies
uv run manage.py migrate    # migrate the db before running the first time
```

With dependencies installed and migrations done, run the server with:

```sh
uv run manage.py runserver
```

## Using the API

### Shortening a url

To shorten a URL, make a POST request with a JSON object containing "address" string - your long URL. See the example below:

```sh
curl -X POST "http://localhost:8000/" \
     -H "Content-Type: application/json" \
     -d '{"address": "<some_long_url>"}'
```

Response:

```json
{ "id": 234, "address": "<some_long_url>", "alias": "<alias>" }
```

Then, you can verify the redirection works by visiting `http://localhost:8000/<alias>`.

## Testing

```sh
uv run manage.py test
```

## TODO

- [x] URL validation + tests
- [ ] Collision prevention (CRC32)
