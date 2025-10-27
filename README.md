# moguls

This Python and Django project is a Freestyle Moguls Competition Scoring System. You can use it to create events, add participants, record its score and get the ranking listing.

---

## Setup it locally

### 1. Set the virtual environment

We are using [uv](https://github.com/astral-sh/uv) for managing this project. Run the sync command, so `uv` can create a new virtual environment using a compatible python version and install all required dependencies. See below:

```bash
$ uv sync
```

Then activate the virtual environment:

```bash
$ source .venv/bin/activate
```

### 2. Environment variables

Create a new `.env` file for setting your environment variables. You can use the `.env.example` file as reference.

```bash
$ cp .env.example .env
```

### 4. Run the migrations

By default it uses SqLite database.

```bash
$ python src/manage.py migrate
```

### 5. Seed data

Populate the development database with seed data

```bash
$ python src/manage.py seed_data
```

### 6. Run the local development server

Run the following command and then access the http://localhost:8000/.

```bash
$ python src/manage.py runserver
```

---

### Running tests locally

```
$ python src/manage.py test src/apps
```
