### django_api - Django REST framework demo

This application demonstrates basic API functionality using the Django REST framework(DRF):

 - blogapi (deploys Swagger & ReDoc UI)

---
### Installation

 - `git clone https://github.com/kevinbowen777/django_api.git`
 - `cd django_api`
 - Local installation
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Open browser to http://127.0.0.1:8000

---
### URLs
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

### Live Demo on Heroku:
 - [django-api-blog](https://kbowen-django-api-blog.herokuapp.com/api/v1/)
 - [Swagger](https://kbowen-django-api-blog.herokuapp.com/swagger/)
 - [Redoc](https://kbowen-django-api-blog.herokuapp.com/redoc/)


---
### Screenshots
![Post list](https://github.com/kevinbowen777/django_api/blob/master/images/drf_post_list.png)

![User list](https://github.com/kevinbowen777/django_api/blob/master/images/drf_user_list.png)

![Swagger UI](https://github.com/kevinbowen777/django_api/blob/master/images/drf_swagger_ui.png)

![ReDoc UI](https://github.com/kevinbowen777/django_api/blob/master/images/drf_redoc_ui.png)

---
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/django_api/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django_api/issues)
      to view currently open bug reports or open a new issue.
