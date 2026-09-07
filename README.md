# Django Advanced Workshop

This repository is my hands-on learning project for exploring more advanced Django concepts.

After learning the basics of Django, I wanted a separate place where I could practice new concepts step by step instead of adding everything to my first Django project.

I usually follow tutorials or other learning resources, then implement what I learn in this repository. The project continues to grow as I learn new Django concepts.

This is not intended to be a finished product. It is a learning workspace where I experiment, practice, make mistakes, and gradually build a better understanding of Django.

---

## Why I Built This Repository

After learning the basics of Django, I wanted to focus more on backend concepts that I had not worked with before.

My goal was to learn topics such as:

- Custom User Models
- Authentication
- Class-Based Views
- Forms
- Permissions
- Testing
- Django REST Framework

Instead of only reading about these concepts, I wanted to implement them in a real Django project.

---

## How I Use This Repository

I use this repository as a hands-on learning workspace.

When I learn a new Django concept, I try to implement it in the project and build on top of what I have already learned.

Because of this, the repository has grown step by step, and the commit history shows different parts of my learning journey.

---

## What I Have Learned and Implemented

### Custom User Model

I implemented a custom user model using AbstractBaseUser.

I also created a custom UserManager with methods for creating regular users and superusers.

This helped me understand how Django handles users and why creating a custom user model early in a project can be useful.

---

### User Profiles and Signals

I created a Profile model connected to users.

I also practiced using Django signals and post_save to automatically create a profile when a new user is created.

This was one of my first practical experiences using signals in Django.

---

### Django Admin Customization

I customized the Django admin panel for managing users and other project data.

This helped me understand how Django's admin can be customized instead of only using the default configuration.

---

### Class-Based Views

One of the main reasons I created this repository was to practice Class-Based Views.

So far, I have worked with views such as:

- TemplateView
- RedirectView
- ListView
- DetailView
- CreateView
- UpdateView
- DeleteView

I am continuing to learn when Class-Based Views are useful and how they compare to Function-Based Views.

---

### Authentication

I have started implementing authentication-related features and practicing Django's authentication system.

This includes topics such as:

- Login
- Logout
- Authentication views
- LoginRequiredMixin

---

### Blog Models

I created a blog application to practice working with Django models and relationships.

The project includes models such as:

- Posts
- Categories

I use this part of the project to practice queries, views, URLs, and other Django concepts.

---

### URL Routing and Namespaces

I practiced organizing URLs using application namespaces with app_name.

This helped me better understand how larger Django projects can organize URL patterns and avoid naming conflicts.

---

### Environment Variables

I practiced managing configuration values using environment variables and python-decouple.

This was useful for understanding how sensitive or environment-specific settings can be separated from the main project configuration.

---

### Docker

I added Docker and Docker Compose to the project.

My goal was to understand how a Django application can run inside containers and how the development environment can be configured separately from the application code.

---

## Django REST Framework

I recently started learning Django REST Framework.

So far, I have started working with:

- Serializers
- Converting Django model data to JSON
- API views
- GET requests
- POST requests
- Creating new objects through an API
  
I am still learning DRF and will continue adding more concepts as I progress.

---

## Current Status

Work in Progress

This repository is still actively growing as I continue learning Django.

I do not consider myself finished with the topics in this project, and I will continue improving and expanding it.

---

## What I Plan to Learn Next

Some of the topics I plan to continue working on are:

- Django Forms and ModelForms
- User permissions and groups
- Pagination
- Search and filtering
- Django testing
- More Django REST Framework concepts
- API authentication and permissions

---

## Technologies Used

- Python
- Django 5.2
- Django REST Framework
- SQLite
- Docker
- Docker Compose
- python-decouple
- Git
- GitHub

---

## Running the Project

### Using Docker

```bash
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### Then open 
http://localhost:8000

### Whiteout Docker 

```bash
git clone https://github.com/rezaziaei28/Django-Advanced-Workshop.git
cd Django-Advanced-Workshop
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## License

MIT License

Copyright (c) 2026 Zia Ziaei
