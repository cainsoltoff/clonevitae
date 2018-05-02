# Clonevitae
Invitae Full-Stack Variant Database Coding Assignment 

Deployed at https://obscure-garden-69041.herokuapp.com

Used Python/Django for the backend (as well as Django templates for barebones frontend rendering).  
Used two jQuery plugins: DataTables (https://datatables.net) and Autocomplete (https://jqueryui.com/autocomplete/)

# To Run
pipenv install
pipenv shell
python manage.py runserver

-- Deployed at http://127.0.0.1:8000 --

# To Update Database
pipenv shell
python manage.py shell
	from helper import load_variant_db
	load_variant_db()
	exit()

#To Run Tests
pipenv shell
python manage.py tests