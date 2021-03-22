 ## Django REST API test for selection process (03/2021) - All the content is in english
 ### Cheff & Receip Backend
 ### Stack: Python + Django Rest Framework + Postgres + SwaggerUI
 #### Getting started

The purpose of this project is to present a simple solution for a Backend position in the company WORKALOVE. Feel Free to download & edit.

The Challenge was basically; as an admin(Cheff), CRUD receips. As an user, request for receips filtering by level of complexity or time consumed, and any other field. Well, as the position is for backend and I have few time; please make sure your user reads the documentation because his frontend is the Swagger itself, and the information he requests, will be in returned in JSON.



 1. Make sure python is installed (included env paths) 
 2. Initialize a new virtual environment: py -m venv env
 3. Activate your virtual env: source venv/bin/activate(Activate1)
 4. Intall dependencies: pip install -r requirements.txt
 5. Install postgres13, create a DB and replace the configurations in Django settings.
 6. Go to project main directory.
 7. Apply migrations: py manage.py migrate
 8. Create superuser : py3 manage.py createsuperuser
 9. Start the local server: py manage.py runserver



