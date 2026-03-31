# Task Manager API

Task Manager API is a REST API built with **FastAPI**, **SQLite**, and **SQLAlchemy** for managing tasks.

This project is the continuation of my previous **Task Manager CLI** project.
The main goal of this version was to evolve from a command-line tool into a backend application with HTTP endpoints, database persistence, and a structure closer to real backend and DevOps workflows.

---

## Project Goal

This project is part of my learning path as I transition from **Manual QA** into **DevOps / Backend Engineering**.

With this API version, I wanted to practice:

* designing REST endpoints
* working with FastAPI
* persisting data with SQLite
* organizing backend code by layers
* preparing the project for Docker and CI/CD

---

## From CLI to API

This repository represents the next step after my previous CLI project.

### Previous version

* Python CLI application
* JSON file persistence
* local command execution
* tests and GitHub Actions pipeline

### Current version

* FastAPI REST API
* SQLite database persistence
* HTTP endpoints
* backend-oriented structure
* prepared for Docker and CI/CD

This progression is important to me because it shows not only the final result, but also my learning process and technical growth.

---

## Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy
* Pydantic
* Pytest

---

## Project Structure

```text
task-manager-API/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── service.py
│   └── crud.py
├── test/
├── requirements.txt
└── README.md
```

---

## Architecture Overview

This project follows a simple layered structure:

```text
Client / Swagger / Postman
            ↓
        FastAPI routes
            ↓
         service.py
            ↓
           crud.py
            ↓
     SQLite + SQLAlchemy
```

### Responsibilities

* **main.py**: defines the API endpoints
* **service.py**: contains business rules and validations
* **crud.py**: handles database operations
* **models.py**: defines database models
* **schemas.py**: defines request and response schemas
* **database.py**: manages the database connection and session

---

## Main Features

* Create tasks
* Get all tasks
* Get a task by ID
* Filter tasks by status
* Update tasks
* Mark tasks as completed
* Delete tasks

---

## API Endpoints

| Method | Endpoint                 | Description             |
| ------ | ------------------------ | ----------------------- |
| POST   | `/tasks/`                | Create a new task       |
| GET    | `/tasks/`                | Get all tasks           |
| GET    | `/tasks/{task_id}`       | Get a task by ID        |
| GET    | `/tasks/?status=pending` | Filter tasks by status  |
| PUT    | `/tasks/{task_id}`       | Update a task           |
| PATCH  | `/tasks/{task_id}`       | Partially update a task |
| DELETE | `/tasks/{task_id}`       | Delete a task           |

---

## How to Run the Project

### 1. Create and activate a virtual environment

On Windows:

```bash
python -m venv env
env\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the API

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Once the server is running, you can open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically generates Swagger UI, where you can test all endpoints interactively.

---

## Example Request

### Get tasks filtered by status

```http
GET /tasks/?status=pending
```

---

## What I Learned

This project helped me reinforce and better understand:

* the difference between a CLI application and an API
* how REST endpoints work
* how to use FastAPI for backend development
* how to move from JSON persistence to a relational database
* how to separate responsibilities in backend code
* how debugging backend issues works in practice
* how backend projects start becoming DevOps-ready

---

## Main Challenges

Some of the things I had to solve while building this project were:

* dependency injection issues with FastAPI
* confusion between path parameters and query parameters
* database session handling
* response handling for different HTTP status codes
* debugging why some filters were not working as expected

These challenges were a big part of the learning value of the project.

---

## Why This Project Matters

This is not just a simple CRUD project.

For me, it represents a clear evolution:

```text
CLI → API → Docker → CI/CD → Deployment
```

It shows my progress from building a local Python tool to designing a backend application with persistence and a structure that can later be containerized, tested automatically, and deployed.

---

## Next Steps

The next improvements planned for this project are:

* add Docker support
* add GitHub Actions CI workflow
* improve API test coverage
* improve validation and error handling
* deploy the API
* continue evolving the project toward a more production-like backend

---

## Related Project

This API is the continuation of my previous CLI project:

* **Task Manager CLI**: a command-line version built with Python

---

## About Me

I am a QA professional currently transitioning into **DevOps / Backend Engineering**.

I am using projects like this to document my learning process, strengthen my technical foundations, and build a portfolio that reflects real progress over time.
