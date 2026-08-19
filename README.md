# Django Advanced Workshop

A structured journey through advanced Django concepts with practical implementations

---

## About This Project

This repository is my personal learning journey through Advanced Django concepts.
Each commit represents a learning milestone, not just code changes.

Work in progress — Backend logic and advanced features are being built.

---

## Features (So Far)

- Custom User Model with email authentication
- User Profile with automatic creation using signals
- Custom Admin panel for user management
- Blog app with Post and Category models
- Class-Based Views (TemplateView, RedirectView)
- URL routing with app_name namespace
- Docker containerization setup
- Environment variables management

---

## Technologies Used

- Python
- Django 5.2
- SQLite (development)
- Docker & Docker Compose
- Git & GitHub

---

## Installation & Setup

### Using Docker
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser


Visit http://localhost:8000

### Without Docker
git clone https://github.com/rezaziaei28/Django-Advanced-Workshop.git
cd core/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Visit http://127.0.0.1:8000/

---

## Project Structure

.
├── core
│   ├── accounts
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_remove_user_published_date_profile.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── blog
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── core
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── settings.cpython-310.pyc
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── staticfile
│   └── templates
├── docker-compose.yml
├── dockerfile
├── requirements.txt
└── venv

---

## What I Learned

- Custom User Model with AbstractBaseUser
- Custom UserManager with create_user and create_superuser
- Profile model with post_save signal
- Admin panel customization with fieldsets
- Class-Based Views (TemplateView, RedirectView)
- URL routing and namespacing
- Static and media file configuration
- Environment variables with python-decouple
- Docker containerization
- Git workflow and meaningful commits

---

## Next Steps

- Add authentication views (login, signup)
- Implement forms and ModelForms
- Add user permissions and groups
- Implement pagination for blog posts
- Add search and filter functionality
- Integrate Django REST Framework

---

## License

MIT License

Copyright (c) 2026 Zia Ziaei
