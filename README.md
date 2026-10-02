# Django Advanced Workshop

This repository is my hands-on learning project for exploring more advanced Django concepts.

After learning the basics of Django, I wanted a separate place where I could practice new concepts step by step instead of adding everything to my first Django project.

I follow tutorials to learn new concepts, then adapt and implement them in this project in my own way. The project continues to grow as I learn new Django concepts.

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

I started learning DRF step by step and implemented many concepts in this project.

### Serializers

I learned how to use ModelSerializer for Post and Category and I also learned how to add ReadOnlyField with source to bring model methods into the serializer and how to use SerializerMethodField for fields that need the request object and how to use write_only for sensitive fields like passwords and how to write a custom validate method and how to override create to set the author from the request user.

### Views

I learned all the different levels of DRF views and used them in the project and this includes function-based views with the api_view decorator and APIView class and generics like ListCreateAPIView and RetrieveUpdateDestroyAPIView and mixins like ListModelMixin and CreateModelMixin and concrete view classes and ViewSets and ModelViewSet and DefaultRouter.

### Serializer Advanced

I learned how to use to_representation to customize the output for list and detail and how to show nested category with CategorySerializer and how to remove fields based on the view and how to add custom fields like state and relative_url.

### Permissions

I used IsAuthenticatedOrReadOnly and I also wrote my own custom permission called IsOwnerOrReadOnly with has_object_permission to check if the request user owns the object.

### ViewSet Features

I learned how to use the action decorator for custom endpoints and how to add filtering with DjangoFilterBackend and search with SearchFilter and search_fields and ordering with OrderingFilter and ordering_fields and I also learned lookup expressions like exact and in for filterset_fields.

### Pagination

I wrote a custom DefultPagination with PageNumberPagination and set page_size and override get_paginated_response to add links and total counts.

### Authentication for API

I learned token authentication and added CustomObtainAuthToken and CustomDiscardAuthToken and I also learned JWT authentication with rest_framework_simplejwt and added token create refresh and verify endpoints.

### User Registration API

I wrote a RegisterSerializer with password and password1 fields and a custom validate method using Django password validators and a RegisterAPIView that creates a user and returns the email.

### API Documentation

I added Swagger and ReDoc with drf-yasg and a schema_view with openapi info and a JSON schema output for client generators.

### API Testing

I used Postman to test all the API endpoints and I tested register login logout token and JWT endpoints and I tested CRUD operations on posts and categories and I tested filtering searching ordering and pagination and I tested permissions with different users to check IsOwnerOrReadOnly.

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
- Django testing
- More DRF concepts like Throttling and Versioning
- JWT customization for returning user info
- API documentation improvements

---

## Technologies Used

- Python
- Django 5.2
- Django REST Framework
- django-filter
- drf-yasg
- rest_framework_simplejwt
- SQLite
- Docker
- Docker Compose
- python-decouple
- Git
- GitHub
- Postman
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

### Without Docker 

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
