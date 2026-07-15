# 🚀 Task Manager API

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST-009688)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-black)
![AWS](https://img.shields.io/badge/Cloud-AWS%20EC2-orange)
![Nginx](https://img.shields.io/badge/Reverse%20Proxy-Nginx-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Task Manager API es un proyecto de portafolio desarrollado con **FastAPI** que demuestra el ciclo completo de desarrollo, pruebas y despliegue automatizado de una aplicación backend.

Además de implementar una API REST segura con autenticación JWT, el proyecto incorpora prácticas DevOps como integración continua, despliegue automático en AWS EC2, administración de servicios Linux mediante **systemd** y publicación mediante **Nginx**.

---

# 🎯 Objetivos del proyecto

Este proyecto fue desarrollado para fortalecer conocimientos en:

- Desarrollo Backend con FastAPI
- Arquitectura por capas
- SQLAlchemy
- Autenticación JWT
- Testing automatizado
- Integración Continua (CI)
- Despliegue Continuo (CD)
- Administración de servidores Linux
- AWS EC2
- Reverse Proxy con Nginx
- Automatización de despliegues

---

# 🏗 Arquitectura

```
                Developer

                    │
              git push main

                    │

             GitHub Repository

                    │

            GitHub Actions

         Ruff • Pytest • Deploy

                    │

              SSH (Secrets)

                    │

             AWS EC2 Ubuntu

                    │

         git fetch / git reset

                    │

       pip install requirements

                    │

       systemctl restart API

                    │

              FastAPI (Uvicorn)

                    │

                 Nginx

                    │

                SQLite
```

---

# 📁 Arquitectura del proyecto

```
app/
├── core/
├── dependencies/
├── models/
├── routers/
├── schemas/
├── services/

alembic/
tests/
.github/
```

El proyecto sigue una arquitectura por capas donde:

- **Routers** reciben las peticiones HTTP.
- **Services** contienen la lógica de negocio.
- **Schemas** validan datos con Pydantic.
- **Models** representan las entidades SQLAlchemy.
- **Core** centraliza configuración, seguridad y base de datos.

---

# 🚀 Tecnologías

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Alembic
- Pydantic

## Testing

- Pytest
- Pytest-cov
- Ruff

## DevOps

- GitHub Actions
- AWS EC2
- Ubuntu
- systemd
- Nginx
- SSH
- Git

---

# ⚙ Instalación local

## Clonar repositorio

```bash
git clone https://github.com/DanielaTola/task-manager-API.git

cd task-manager-API
```

## Crear entorno virtual

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Variables de entorno

Crear un archivo `.env`

```env
DATABASE_URL=sqlite:///./task_manager.db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Ejecutar migraciones

```bash
alembic upgrade head
```

## Levantar aplicación

```bash
uvicorn app.main:app --reload
```

---

# 🔐 Autenticación

La API utiliza JWT Authentication.

Flujo:

```
Register

↓

Login

↓

Access Token

↓

Authorization Bearer Token

↓

Protected Endpoints
```

---

# 📌 Endpoints

## Auth

| Método | Endpoint |
|---------|----------|
| POST | /auth/register |
| POST | /auth/login |

## Tasks

| Método | Endpoint |
|---------|----------|
| GET | /tasks |
| POST | /tasks |
| GET | /tasks/{id} |
| PUT | /tasks/{id} |
| PATCH | /tasks/{id} |
| DELETE | /tasks/{id} |

Cada usuario únicamente puede acceder a sus propias tareas.

---

# 🧪 Testing

Ejecutar pruebas

```bash
pytest
```

Cobertura

```bash
pytest --cov=app
```

Incluye:

- autenticación JWT
- endpoints protegidos
- SQLite aislada
- cobertura

---

# ⚙ CI/CD

El pipeline automatiza completamente el proceso de integración y despliegue.

## Flujo

```
Push a main

↓

GitHub Actions

↓

Ruff

↓

Pytest

↓

SSH

↓

AWS EC2

↓

Actualizar repositorio

↓

Instalar dependencias

↓

Reiniciar servicio systemd

↓

Health Check

↓

Aplicación disponible
```

---

# ☁ Despliegue en AWS

Infraestructura utilizada

- Ubuntu Server
- AWS EC2
- FastAPI
- Uvicorn
- systemd
- Nginx
- SQLite

La aplicación permanece ejecutándose como un servicio Linux mediante **systemd**, mientras que **Nginx** actúa como reverse proxy para exponer la API.

---

# 🔒 Seguridad

Las credenciales de producción **no** forman parte del repositorio.

Se utilizan:

- GitHub Secrets
- Archivo `.env`
- SSH Keys
- Variables de entorno

---

# 📚 Aprendizajes

Durante este proyecto fortalecí conocimientos en:

- Diseño de APIs REST
- Arquitectura por capas
- SQLAlchemy
- JWT
- Testing
- GitHub Actions
- AWS EC2
- Linux
- systemd
- Nginx
- CI/CD
- Automatización de despliegues

---

# 🛣 Roadmap

## Backend

- [ ] Refresh Tokens
- [ ] RBAC
- [ ] Rate Limiting

## Cloud

- [x] AWS EC2
- [ ] Amazon RDS
- [ ] Docker
- [ ] Docker Compose

## DevOps

- [x] GitHub Actions
- [x] Continuous Deployment
- [ ] Terraform
- [ ] CloudWatch
- [ ] Prometheus
- [ ] Grafana
- [ ] Kubernetes

---

# 👩‍💻 Autor

**María Daniela Tola Romero**

QA Engineer | Backend Developer | DevOps Engineer (Learning Journey)

LinkedIn: https://www.linkedin.com/in/maria-daniela-tola-7464071a9/

GitHub: https://github.com/DanielaTola