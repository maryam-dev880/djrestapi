# Django Task Management REST API

A RESTful API built with Django REST Framework for managing tasks — supports full CRUD operations, token authentication, custom validation, and pagination.

## Features

- Full CRUD operations (Create, Read, Update, Delete)
- Token-based authentication
- Custom validation (title length, completed task rules)
- Custom endpoints for completed and pending tasks
- Configurable pagination

## Tech Stack

- Python 3.12
- Django 6.1
- Django REST Framework
- SQLite

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks/` | List all tasks |
| POST | `/tasks/` | Create a task |
| GET | `/tasks/<id>/` | Get a specific task |
| PUT | `/tasks/<id>/` | Update a task |
| PATCH | `/tasks/<id>/` | Partially update a task |
| DELETE | `/tasks/<id>/` | Delete a task |
| GET | `/tasks/completed/` | List completed tasks |
| GET | `/tasks/pending/` | List pending tasks |

## Setup

```bash
git clone https://github.com/maryam-dev880/<repo-name>.git
cd djrestapi
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Generate a token from the Django admin panel (`/admin/`) to authenticate API requests.

## Author

**Maryam**
GitHub: [maryam-dev880](https://github.com/maryam-dev880)

## License

© 2026 Maryam. All rights reserved. This project is shared for portfolio and educational viewing purposes only. Copying, reusing, or redistributing this code without permission is not allowed.