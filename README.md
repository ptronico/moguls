# moguls

This Python and Django project is a Freestyle Moguls Competition Scoring System. You can use it to create events, add participants, record its score and get the ranking listing.

---

### Setup it locally

We are using [uv](https://github.com/astral-sh/uv) for managing this project. Run the sync command, so `uv` can create a new virtual environment using a compatible python version and install all required dependencies. See below:

```bash
$ uv sync
```

Then activate the virtual environment:

```bash
$ source .venv/bin/activate
```

#### Running it locally

Run the following command and then access the http://localhost:8000/.

```
$ python src/manage.py runserver
```

#### Running tests locally

```
$ python src/manage.py test
```
