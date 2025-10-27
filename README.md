# moguls

This Python and Django project is a Freestyle Moguls Competition Scoring System. You can use it to create events, add participants, record its score and get the ranking listing.

For more information on Freestyle Moguls and its Scoring see the following links:

- [Mogul Skiing](https://en.wikipedia.org/wiki/Mogul_skiing)
- [Fis Freestyle Skiing Judging Handbook](https://assets.fis-ski.com/f/252177/x/1eedc72758/freestyle-skiing-judging-handbook-august-2024.pdf)
- [Judges Cards Moguls Turns Freestyle Skiing](https://assets.fis-ski.com/f/252177/7ae160397a/judges_cards_moguls_turns_freestyle_skiing_2020.pdf)

---

## Setup it locally

After clonning the repository and change your directory, follow the steps below:

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

## Other operations

### Create a supersuser account

This allows you to access Django Admin and manage Events, Participants and Scores.

```
$ python src/manage.py createsuperuser
```


### Running tests locally

```
$ python src/manage.py test src/apps
```
