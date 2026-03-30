# Task Manager API

This project is a REST API for task management built with **FastAPI**.
It is the natural evolution of the previous project
[Task Manager CLI](https://github.com/DanielaTola/task_manager_cli),
which started as a command-line application and was designed from the beginning
to later evolve into a backend API.

The goal of this repository is to apply backend best practices such as
API design, automated testing, database isolation, and code quality controls.

---

## 🚀 Project Evolution

- **Phase 1**: Task Manager CLI  
  A command-line application written in Python that manages tasks stored locally.
- **Phase 2 (this repository)**: Task Manager API  
  A RESTful API that exposes similar functionality through HTTP endpoints,
  using FastAPI and SQLAlchemy, and introducing automated testing and CI-ready setup.

This evolution reflects a real-world development path: starting with a simple
local application and progressively moving towards a backend service.

---

## 🛠️ Technologies Used

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Pytest

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/DanielaTola/task-manager-API.git
cd task-manager-API
```
Create and activate a virtual environment:

```Linux / Mac
python -m venv env
source env/bin/activate   
```

```bash
env\Scripts\activate      
```

Install dependencies:

```bash
pip install -r requirements.txt   
```

---

## ▶️ Running the API

Start the development server with:

```bash
uvicorn app.main:app --reload 
```
The API will be available at:

http://127.0.0.1:8000
Swagger documentation: http://127.0.0.1:8000/docs


---
## 📌 Endpoints principales

| Método | Endpoint       | Descripción               |
|--------|----------------|---------------------------|
| POST   | /tasks         | Crear una nueva tarea     |
| GET    | /tasks         | Obtener todas las tareas  |
| GET    | /tasks/{id}    | Obtener una tarea por ID  |
| PUT    | /tasks/{id}    | Actualizar una tarea      |
| DELETE | /tasks/{id}    | Eliminar una tarea        |

---
## 🧪 Testing
The project includes automated tests written with pytest.
To run the test suite:
```bash
pytest
```
Tests are executed using a SQLite in-memory database, ensuring:

 - Full isolation from production data
 - Deterministic and repeatable test runs
 - Compatibility with Continuous Integration pipelines