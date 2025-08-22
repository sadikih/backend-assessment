# Backend Assessment Project

This is a Django REST Framework project created for a backend assessment.  
It provides a simple **Items API** with CRUD operations, automated testing, and a GitHub Actions CI/CD pipeline.  

---

## Features
- Django REST API with CRUD for `Item`
- PostgreSQL database support
- Unit tests to verify functionality
- GitHub Actions CI pipeline that runs tests automatically

---

## Setup Instructions

Clone repository:
```bash
git clone https://github.com/sadikih/backend-assessment.git
cd backend-assessment
```

Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create `.env` file in project root:
```ini
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=backend_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

Run migrations:
```bash
python manage.py migrate
```

Start server:
```bash
python manage.py runserver
```
API will be available at:
👉 http://127.0.0.1:8000/api/items/

---

## Running Tests

Run all tests with:
```bash
python manage.py test api
```

Example real test output:
```
Found 4 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 0.047s

OK
Destroying test database for alias 'default'...
```

---

## CI/CD with GitHub Actions

A workflow is configured in `.github/workflows/ci.yml`.

On every push:
- Python is set up
- Dependencies installed
- PostgreSQL service started
- Tests are executed automatically

Results can be seen in the **Actions** tab on GitHub.

---

## API Endpoints

| Method | Endpoint           | Description    |
|--------|--------------------|----------------|
| GET    | `/api/items/`      | List all items |
| POST   | `/api/items/`      | Create item    |
| GET    | `/api/items/{id}/` | Retrieve item  |
| PUT    | `/api/items/{id}/` | Update item    |
| DELETE | `/api/items/{id}/` | Delete item    |

Example `curl` usage:

```bash
# Create item
curl -X POST http://127.0.0.1:8000/api/items/ -H "Content-Type: application/json" -d '{"name": "Laptop"}'

# Get all items
curl http://127.0.0.1:8000/api/items/

# Update item
curl -X PUT http://127.0.0.1:8000/api/items/1/ -H "Content-Type: application/json" -d '{"name": "Tablet Pro"}'

# Delete item
curl -X DELETE http://127.0.0.1:8000/api/items/1/
```

---

## Author
- **Name:** Sadik  
- **GitHub:** [sadikih](https://github.com/sadikih)
