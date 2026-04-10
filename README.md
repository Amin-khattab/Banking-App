# Banking App

A full-stack banking application built with FastAPI, PostgreSQL, SQLAlchemy, Alembic, and Tailwind CSS.

The app supports account creation, login/logout, transaction tracking, money transfers between users, and an AI assistant powered by OpenAI that answers questions using the signed-in user's financial data.

## Features

- Sign up with email and password
- Log in with session-based authentication
- Secure password hashing with `passlib` and `bcrypt`
- Dashboard with current balance, income total, and expense total
- Transaction history with optional income/expense filtering
- Transfer money to another user by email
- AI assistant powered by OpenAI for quick account insights
- PostgreSQL persistence with Alembic migrations

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Jinja2
- Tailwind CSS
- OpenAI API

## Project Structure

```text
Back_end/
  alembic/
  config.py
  database.py
  main.py
  models.py
front_end/
  assistant.html
  assistant.js
  dashboard.html
  login.html
  profile.html
  sign_up.html
  transaction.html
  transfer.html
screenshots/
  Ai.png
  Dashboard.png
  login.png
  profile.png
  sign_up.png
  transaction.png
  transfer.png
.env.example
README.md
alembic.ini
```

## Prerequisites

- Python 3.10+
- PostgreSQL

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

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary python-dotenv jinja2 passlib bcrypt itsdangerous python-multipart openai
```

### 4. Configure environment variables

Copy the example file:

```bash
cp .env.example .env
```

Then update `.env` with your local values:

```env
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/banking_app
OPENAI_API_KEY=your_openai_api_key_here
```

`OPENAI_API_KEY` is required only if you want to use the AI assistant page.

### 5. Run database migrations

```bash
alembic upgrade head
```

### 6. Start the development server

```bash
uvicorn Back_end.main:app --reload
```

Open the app at:

```text
http://127.0.0.1:8000
```

## Main Routes

- `/` - sign-up page
- `/login` - login page
- `/dashboard` - account overview
- `/transaction` - full transaction history
- `/transfer` - transfer money to another user
- `/assistant` - AI banking assistant
- `/profile` - profile page

## Screenshots

### Sign Up

![Sign Up Page](./screenshots/sign_up.png)

### Login

![Login Page](./screenshots/login.png)

### Dashboard

![Dashboard Page](./screenshots/Dashboard.png)

### Transactions

![Transactions Page](./screenshots/transaction.png)

### Transfer

![Transfer Page](./screenshots/transfer.png)

### AI Assistant

![AI Assistant Page](./screenshots/Ai.png)

### Profile

![Profile Page](./screenshots/profile.png)

## Notes

- Transfers create two transaction records: one `expense` record for the sender and one `income` record for the recipient
- Transaction pages can be filtered with `?type=income` or `?type=expense`
- The current session secret is hardcoded for local development and should be moved to environment variables before production use

## Future Improvements

- Better transfer validation and user feedback
- Stronger production auth/session configuration
- Profile editing
- Better transaction search and filters
- Automated tests
- Deployment setup

## Author

Amin Khattab
