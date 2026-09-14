# chmURL ☁️
A DRF server for URL shortening.

## Installation
First, clone the repo:
``` sh
git clone git@github.com:aszc-dev/chmurl.git && cd chmurl
```
Then, proceed to setup.

### With uv
> [!NOTE]
> Visit https://github.com/astral-sh/uv to learn more on how to install and use uv.

``` sh
uv sync
uv run manage.py migrate
```

## Running
With dependencies installed and migrations done, run the server with:

``` sh
uv run manage.py runserver
```

## Testing
Testing suite is implemented using pytest with pytest-django. To be able to run it, install development dependencies:
``` sh
uv sync --dev
```
After that, running tests is done either with `manage.py` or `pytest` directly:

``` sh
uv run manage.py test
# or
uv run pytest
```
