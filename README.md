# Banking App

A simple full-stack banking app built with FastAPI, PostgreSQL, SQLAlchemy, Alembic, and Tailwind CSS.

This project includes:
- user sign up and login
- password hashing
- session-based authentication
- protected pages
- real database-backed transactions
- dashboard totals
- money transfer by email between users

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Jinja2
- Tailwind CSS

## Features

- Create an account
- Log in and log out
- Store users in PostgreSQL
- Hash passwords securely with bcrypt/passlib
- View a dashboard with balance, income, and expense totals
- View transactions and filter by income or expense
- Transfer money to another user by email

## Project Structure

```text
Back_end/
  alembic/
  config.py
  database.py
  main.py
  models.py
front_end/
  dashboard.html
  login.html
  profile.html
  sign_up.html
  transaction.html
  transfer.html
alembic.ini
.env.example
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Amin-khattab/Banking-App.git
cd Banking-App
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install backend dependencies

```bash
pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary python-dotenv jinja2 passlib bcrypt itsdangerous python-multipart
```

### 4. Create the environment file

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/banking_app
```

You can also copy from `.env.example`.

### 5. Run migrations

```bash
alembic upgrade head
```

### 6. Start the app

Run from the project root:

```bash
uvicorn Back_end.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

## Notes

- Transfers work by recipient email.
- The sender's balance decreases and the recipient's balance increases.
- Each transfer creates two transaction records:
  - sender: expense
  - recipient: income

## Future Improvements

- better validation and error messages
- account settings/profile editing
- cleaner UI polish
- transfer success/failure feedback
- better transaction search and filtering
- tests

## Author

Amin Khattab
