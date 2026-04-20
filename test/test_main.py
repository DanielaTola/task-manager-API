import uuid

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def create_user_and_get_token():
    unique_id = str(uuid.uuid4())[:8]
    register_data = {
        "name": "Test User",
        "last_name": "Test",
        "date_of_birth": "1990-01-01",
        "username": f"testuser{unique_id}",
        "email": f"testuser_{unique_id}@pruebas.com",
        "password": "Testpassword123."
    }
    register_response =client.post("/auth/register", json=register_data)
    assert register_response.status_code in [200, 201]

    login_data = {
        "username": f"testuser{unique_id}",
        "password": "Testpassword123."
    }
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"} 


def test_create_task():
    headers = create_user_and_get_token()
    response = client.post(
        "/tasks",
        headers=headers,
        json={
            "title": "Aprender testing 3",
            "description": "Escribir tests para la API",
            "status": "pending",
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Aprender testing 3"
    assert data["status"] == "pending"


def test_get_tasks():
    headers = create_user_and_get_token()
    response = client.get("/tasks", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task_by_id():
    headers = create_user_and_get_token()
    create = client.post(
        "/tasks",
        headers=headers,
        json={
            "title": "Tarea para buscar 3",
            "description": "Prueba get by id",
            "status": "pending",
        },
    )

    task_id = create.json()["id"]
    response = client.get(f"/tasks/{task_id}", headers=headers)

    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_get_task_not_found():
    headers = create_user_and_get_token()
    response = client.get("/tasks/non-existent-id", headers=headers)

    assert response.status_code == 404


def test_delete_task():
    headers = create_user_and_get_token()
    create = client.post(
        "/tasks",
        headers=headers,
        json={
            "title": "Tarea a eliminar",
            "description": "Delete test",
            "status": "pending",
        },
    )

    task_id = create.json()["id"]

    delete = client.delete(f"/tasks/{task_id}", headers=headers)
    assert delete.status_code == 204


def test_update_task():
    headers = create_user_and_get_token()
    create = client.post(
        "/tasks", 
        headers=headers, 
        json={
            "title": "Original", 
            "description": "Antes del update",
            "status": "pending"
        }
    )

    assert create.status_code == 201
    
    task_id = create.json()["id"]

    update = client.put(
        f"/tasks/{task_id}",
        headers=headers,
        json={
            "title": "Actualizada",
            "description": "Después del update",
            "status": "completed",
        },
    )

    assert update.status_code == 200
    assert update.json()["status"] == "completed"
