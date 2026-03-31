from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_creste_task():
    response = client.post(
        "/tasks",
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
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task_by_id():
    create = client.post(
        "/tasks",
        json={
            "title": "Tarea para buscar 3",
            "description": "Prueba get by id",
            "status": "pending",
        },
    )

    task_id = create.json()["id"]
    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_get_task_not_found():
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_delete_task():
    create = client.post(
        "/tasks",
        json={
            "title": "Tarea a eliminar",
            "description": "Delete test",
            "status": "pending",
        },
    )

    task_id = create.json()["id"]

    delete = client.delete(f"/tasks/{task_id}")
    assert delete.status_code == 204


def test_update_task():
    create = client.post(
        "/tasks", json={"title": "Original", "description": "Antes del update"}
    )

    task_id = create.json()["id"]

    update = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Actualizada",
            "description": "Después del update",
            "status": "completed",
        },
    )

    assert update.status_code == 200
    assert update.json()["status"] == "completed"
