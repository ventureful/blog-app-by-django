### django_api - Django REST framework demo

This application demonstrates basic API functionality using the Django REST framework(DRF):

 - blogapi (deploys Swagger & ReDoc UI)

---
### Installation

 - `git clone https://github.com/kevinbowen777/django_api.git`
 - `cd django_api`
 - `docker-compose up --build`
     - `docker-compose exec blog_api-web python manage.py migrate`
     - `docker-compose exec blog_api-web createsuperuser`
 - URLs:
     - http://127.0.0.1:8000/api/v1
     - http://127.0.0.1:8000/swagger
     - http://127.0.0.1:8000/redoc

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
