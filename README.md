# Toolgether

Quick intro in how to setup your django and other information

<h1> SETUP GUIDE </h1>

( NOTICE - If you get error that you cannot run anything tell me and I will help sort ) - Loic

### Delete the ".venv" folder on your local clone
### Create venv
- `python -m venv .venv`

### Install packages
- `pip install -r requirements.txt`

### Activate Venv
- `.venv/Scripts/Activate.ps1`
Venv is the Virtual Environment

### Run Webserver
- `python manage.py runserver`
Go to the URL outputted into your terminal/cmd etc to see the Django web app locally

<h1> OTHER INFO </h1>

### Files within Project
- **`__init__`.py:** Files in folder are part of a Python package. Allows import of files from other directories
- **asgi.py:** Allows for optional Asynchronous Server Gateway Interface to be run
- **settings.py:** Controls project's overall settings
- **urls.py:** Tells Django which pages to build when responding to browser or URL requests
- **wsgi.py:** "*Web Server Gateway Interface*", Helps server web pages
- **manage.py:** Used to execute Django commands (e.g. Running local web server or creating a new app)

### Files within Apss
- **admin.py**, Config file for the built-in Django admin app
- **apps.py**, Config file for the app itself
- **migrations**, Keeps track of any changes to `models.py`, Ensure it stays in sync with the database
- **models.py**, Define database models, Django automatically translates to database tables
- *tests.py*, For app-specific tests
- *views.py*, Handles request/response logic for the web app



