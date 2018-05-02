# Clonevitae
Invitae Full-Stack Variant Database Coding Assignment 

Deployed at https://obscure-garden-69041.herokuapp.com

Used Python/Django for the backend (as well as Django templates for barebones frontend rendering).  
Used two jQuery plugins: DataTables (https://datatables.net) and Autocomplete (https://jqueryui.com/autocomplete/)

# To Run
pipenv install <br />
pipenv shell <br />
python manage.py runserver <br />

-- Deployed at http://127.0.0.1:8000 --

# To Update Database
pipenv shell <br />
python manage.py shell <br />
from helper import load_variant_db <br />
load_variant_db() <br />
exit() <br />

#To Run Tests
pipenv shell <br />
python manage.py tests <br />