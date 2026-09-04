# Django Task Management REST API

A RESTful API built with Django REST Framework for managing tasks — supports full CRUD operations, token authentication, user-specific data, search, and pagination. Includes a simple HTML/CSS/JavaScript frontend that consumes the API.

## Features

- Full CRUD operations (Create, Read, Update, Delete)
- Token-based authentication (including a login endpoint that returns a token)
- User-specific tasks — each user can only see and manage their own tasks
- Search functionality (search tasks by title or description)
- Custom validation (title length, completed task rules)
- Custom endpoints for completed and pending tasks
- Configurable pagination
- Simple frontend (login, add/search/update/delete tasks) built with vanilla HTML, CSS, and JavaScript

## Tech Stack

- Python 3.12
- Django 6.1
- Django REST Framework
- SQLite
- django-cors-headers (for frontend-backend communication)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api-token-auth/` | Log in with username/password, returns an auth token |
| GET | `/tasks/` | List the logged-in user's tasks |
| GET | `/tasks/?search=keyword` | Search tasks by title or description |
| POST | `/tasks/` | Create a task (owned by the logged-in user) |
| GET | `/tasks/<id>/` | Get a specific task |
| PUT | `/tasks/<id>/` | Update a task |
| PATCH | `/tasks/<id>/` | Partially update a task |
| DELETE | `/tasks/<id>/` | Delete a task |
| GET | `/tasks/completed/` | List the logged-in user's completed tasks |
| GET | `/tasks/pending/` | List the logged-in user's pending tasks |

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

Generate a token either from the Django admin panel (`/admin/`) or by sending a POST request to `/api-token-auth/` with a username and password.

## Frontend

A simple frontend is included in the `frontend/` folder (`index.html`). It lets a user log in, view their tasks, add new tasks, search, update task status, and delete tasks — all through the API above.

To use it, open `frontend/index.html` directly in a browser while the Django development server is running.

## Author

**Maryam**
GitHub: [maryam-dev880](https://github.com/maryam-dev880)

## License

© 2026 Maryam. All rights reserved. This project is shared for portfolio and educational viewing purposes only. Copying, reusing, or redistributing this code without permission is not allowed.