### django-api-blog

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/django-api-blog.svg)](https://github.com/kevinbowen777/django-api-blog/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

 - A basic blogging website & API built with Django 4.1 & Django REST Framework (DRF) 3.13

##### Table of Contents
 - [Features](#features)
 - [Installation](#installation)
 - [Testing](#testing)
 - [API URLs](#api-urls)
 - [Application Demo](#application-demo)
 - [Screenshots](#screenshots)
 - [Reporting Bugs](#reporting-bugs)

---

### Features
 - Application
     - Browseable Web API
     - SwaggerUI & ReDoc API documentation
     - User registration with email verification & social(GitHub) login
     - Bootstrap4 & crispy-forms decorations
     - Customizable user profile pages with bio, profile pic, & country flags
 - Dev/testing
     - Basic module testing templates
     - Coverage reports
     - Debug-toolbar available
     - Examples of using Factories & pytest fixtures in account app testing
     - `shell_plus` with IPython via `django-extensions` package
     - Nox testing sessions for latest Python 3.9, 3.10, and 3.11
         - black
         - Sphinx documentaion generation
         - linting
             - flake8
             - flake8-bugbear
             - flake8-docstrings
             - flake8-import-order
         - safety(python package vulnerability testing)
         - pytest sessions with coverage
     - For additional links to package resources used in this repository, see the [Package Index](docs/package_index.md)

---
### Installation

 - `git clone https://github.com/kevinbowen777/django-api-blog.git`
 - `cd django-api-blog`
 - Local installation
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation
     - `docker compose up --build`
     - `docker compose exec web python manage.py migrate`
     - `docker compose exec web python manage.py createsuperuser`
     Additional commands:
       - `docker compose exec web python manage.py shell_plus`
         (loads Django shell autoloading project models & classes)
       - `docker run -it django-start-web bash`
         (CLI access to container)
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---

### Testing
 - `docker-compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`


---

### API URLs
 - Log In endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/login/
 - Log Out endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/
 - Password reset:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset
 - Password reset confirmation:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset/confirm
 - User registration endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/
 - User list:
    http://127.0.0.1:8000/api/v1/users/
 - User detail:
    http://127.0.0.1:8000/api/v1/users/1/
 - API schema download:
    http://127.0.0.1:8000/api/schema/
 - Redoc API browser:
    http://127.0.0.1:8000/api/schema/redoc/
 - Swagger-UI:
    http://127.0.0.1:8000/api/schema/swagger-ui/

---

### Application Demo
A live application demonstration hosted at Heroku
 - [django-api-blog](https://kbowen-django-api-blog.herokuapp.com/api/v1/)

---

### Screenshots
![Post list](https://github.com/kevinbowen777/django-api-blog/blob/master/images/drf_post_list.png)

![User list](https://github.com/kevinbowen777/django-api-blog/blob/master/images/drf_user_list.png)

![Swagger UI](https://github.com/kevinbowen777/django-api-blog/blob/master/images/drf_swagger_ui.png)

![ReDoc UI](https://github.com/kevinbowen777/django-api-blog/blob/master/images/drf_redoc_ui.png)

---

### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django-api-blog/issues)
      to view currently open bug reports or open a new issue.
