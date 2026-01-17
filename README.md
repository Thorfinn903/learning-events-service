# Learning Events Service

A backend microservice built with **FastAPI** to track and retrieve student learning activities. This service allows educational platforms to log events (like quiz attempts or video views) and query them for analytics.

## 🚀 Features

* **RESTful API** built with FastAPI for high performance.
* **Data Validation** using Pydantic models.
* **Database Integration** using SQLAlchemy (currently configured for SQLite, easily adaptable to MySQL/MariaDB).
* **Automatic UUIDs & Timestamps** for every recorded event.
* **Interactive Documentation** (Swagger UI & ReDoc) included automatically.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Server:** Uvicorn
* **ORM:** SQLAlchemy
* **Database:** SQLite (Default for development)

## 📂 Project Structure

```text
learning_events_service/
├── main.py            # Application entry point and API routes
├── database.py        # Database connection handling
├── models.py          # SQLAlchemy database table definitions
├── schemas.py         # Pydantic data validation models
├── crud.py            # Database CRUD operations
└── requirements.txt   # Project dependencies


