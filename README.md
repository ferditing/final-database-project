# 🚖 Simple Uber-like API (Project)

A lightweight **FastAPI + SQLAlchemy + MySQL** backend that mimics a simplified Uber system.
It supports **Users** (passengers/drivers) and **Rides**, with full CRUD for users and ride creation/tracking.

---

##  Setup Instructions

### 1. Clone repository

```bash
git clone https://github.com/ferditing/final-database-project.git
cd final-database-project
```

### 2. Create virtual environment

```bash
# Linux/Mac
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Create a MySQL database:

```sql
CREATE DATABASE uberdb;
```

Update the connection string in **`database.py`**:

```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/uber_db"
```

### 5. Run the app

```bash
uvicorn main:app --reload
```

The API will be available at:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

##  API Endpoints

### Users

* `POST /users/` → Create user
* `GET /users/` → Get all users
* `GET /users/{id}` → Get single user
* `PUT /users/{id}` → Update user
* `DELETE /users/{id}` → Delete user

###  Rides

* `POST /rides/` → Create ride
* `GET /rides/` → Get all rides
* `GET /rides/{id}` → Get ride by id

---

##  Testing with Postman

We’ve included a **Postman Collection** in this repo: `uber-api.postman_collection.json`

### How to Use:

1. Open **Postman**
2. Click **Import**
3. Select `uber-api.postman_collection.json`
4. Run the preconfigured requests:

   * Create User
   * Get Users
   * Create Ride
   * Get Rides

---

##  Project Structure

```
final-database-project/
│── main.py              # FastAPI entry point
│── database.py          # DB connection setup
│── models.py            # SQLAlchemy models
│── schemas.py           # Pydantic schemas
│── crud.py              # Database operations
│── requirements.txt     # Dependencies
│── uber-api.postman_collection.json  # Postman tests
│── README.md            # Project documentation
```

---

