# Palindrome Game Django

This repository contains API to 
- create/update/delete a user
- login user
- start a game
- get gameString
- update the gameString
- check whether the gameString is palindrome or not, when string length equals 6
- get a list of all games played
- logout user

<br />

## Test this API on your local machine:
### 1. Creating a Python Virtual Environment
```sh
python -m venv <virtual_environment_name>
```

### 2. Activating the Virtual Environment
```sh
cd <virtual_environment_name>
Scripts\activate (on Windows)
source bin/activate (on MacOS)
```

### 3. Installing Django
```sh
pip install django
```
### 4. Clone this repo into your local machine
```sh
git clone https://github.com/laminarss/palindrome-game-django.git
```

### 5. Run Development Server
```sh
cd palindrome-game-django
python manage.py runserver
```

### 6. Test the API
> To test the API, a web browser or a tool like Postman can be used.

<br />
<br />

## Steps to Create & Run Django Project:
### 1. Creating a Python Virtual Environment
```sh
python -m venv <virtual_environment_name>
```

### 2. Activating the Virtual Environment
```sh
cd <virtual_environment_name>
Scripts\activate (on Windows)
source bin/activate (on MacOS)
```

### 3. Installing Django
```sh
pip install django
```

### 4. Creating a Django Project
```sh
django-admin startproject <project_name>
```

### 5. Creating an App in the Project
```sh
cd <project_name>
python manage.py startapp <app_name>
```
> Make sure to add the `<app_name>` to `INSTALLED_APPS` in `settings.py`

### 6. Creation of Models, Views, and Routing with URLs
 1. `models.py`, `views.py`, `urls.py` contain models, views, url paths respectively.

### 7. Running the Development Server
```sh
python manage.py runserver
```
> Default host would be http://127.0.0.1:8000

### 8. Test the API
> To test the API, a web browser or a tool like Postman can be used.
