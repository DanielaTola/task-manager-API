# Task Manager API

REST API for task management built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

This project is the **evolution of a previous CLI application**, redesigned as a backend service and progressively improved with **testing, Docker, and CI/CD practices**.

---

## Project Evolution

This repository continues:

👉 https://github.com/DanielaTola/task_manager_cli

Progression:

```text
CLI → API → Docker → CI → Code Quality → (Next: Deployment)
```

This reflects a real learning path toward **DevOps / Backend Engineering**.

---

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pytest + pytest-cov
- Docker
- GitHub Actions
- Ruff + Black (code quality)

---

## Features

- Create, read, update, delete tasks
- Filter tasks by status
- Mark tasks as completed
- Automated tests with coverage
- Dockerized application
- CI pipeline (GitHub Actions)
- Code linting and formatting

---

## Project Structure

```text
task-manager-API/
├── app/
│   ├── data/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── test/
├── .github/workflows/
├── Dockerfile
├── pyproject.toml
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## How to Run

### 1. Setup

```bash
git clone https://github.com/DanielaTola/task-manager-API.git
cd task-manager-API
python -m venv env
env\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 2. Run API

```bash
uvicorn app.main:app --reload
```

Docs:
```
http://127.0.0.1:8000/docs
```

---

## Running Tests

```bash
pytest
```

Includes:
- isolated test database
- coverage validation

---

## Docker

```bash
docker build -t task-manager-api .
docker run -p 8000:8000 task-manager-api
```

---

## CI (GitHub Actions)

Pipeline runs automatically on push:

- install dependencies
- run tests
- validate coverage
- build Docker image

---

## Code Quality

```bash
ruff check . --fix
black .
```

Ensures:
- clean code
- consistent style
- fewer basic errors

---

## What This Project Demonstrates

- evolution from CLI to API
- layered backend structure
- automated testing practices
- containerization with Docker
- CI pipeline setup
- code quality enforcement

---

## About

This project is part of my transition from **Manual QA → DevOps / Backend Engineering**, focused on building real-world skills step by step.