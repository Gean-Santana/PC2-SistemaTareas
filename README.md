mkdir gestor_tareas_api
cd gestor_tareas_api
python -m venv env
env\Scripts\activate
source env/bin/activate
pip install django djangorestframework
django-admin startproject gestor_tareas .
python manage.py startapp tareas
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
