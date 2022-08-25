# Django-Starter-Template
This repository contains template for Django Starter Project. It includes Django Authentication System Implemented (Sign Up, Sign In &amp; Logout), Check if username or email already exists in database during sign up &amp; Django Messages Framework Implemented.

# How to Use it ?
1. Clone this repo using:
```bash
git clone https://github.com/hussnainahmad25/Django-Starter-Template.git
```

2. Now install django-rename-app module:
```bash
pip install django-rename-app
```

3. Add to your Django settings.py 
```python
INSTALLED_APPS = [
    ...
    'django_rename_app',
    ...
]
```

4. Finally run:
```bash
python manage.py rename_app <old_app_name> <new_app_name>
```
