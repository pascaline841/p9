<h1 align="center">DJANGO Project -  LIT REVIEW</h1>
  
## OVERVIEW
Beta version of a website made with Django. Allows you to post reviews to respond to the reviews of other user, to post your own review and to follow users and their posts.
<br>


## REQUISITORIES 
Python3<br>
Django3<br>
Flake8-html<br>

## INSTALLATION
Start by closing the repository :
```
git clone https://github.com/pascaline841/python_p09
```
Start access the project folder

## for Window
Create a virtual environment
```
python -m venv env
```
Enable the virtual environment
```
cd env/scripts
source activate
```

## for Linux or macOS
Create a virtual environment 
```
python3 -m venv env
```
Activate the virtual environment with 
```
source env/bin/activate 
```
## . . . 
Install the python dependencies to the virtual environment
```
pip install -r requirements.txt
```
- Create the database structure by using sqlite3 
```
python manage.py migrate
``` 
- Create an administrative account : <br>
You will be asked to select a username, provide an email address, and choose and confirm a password for the account.
```
winpty python manage.py createsuperuser
```
- Create and open a file named .env then paste :
```
DJANGO_SETTINGS_MODULE="litreview.settings.development"
DB_SECRET_KEY= 
```
Then complete DB_SECRET_KEY with the key you receive in private.
## LAUNCH 

Run the program
```
python manage.py runserver
```
Launch :

http://127.0.0.1:8000

To access to the admin account :

http://127.0.0.1:8000/admin 

## Use FLAKE8
In order to generate a flake8 report, run the following command :
```
flake8 --ignore=E501,W503 --format=html --htmldir=flake-report --exclude=venv,manage.py,db.sqlite3,litreview
```
Open the html file into the flake-report repertory to show the report.
## SCREENSHOT

![screenshot0](https://user-images.githubusercontent.com/55999192/119537783-439ec500-bd3f-11eb-84f0-e27279db755e.PNG)
<br>
![screenshot1](https://user-images.githubusercontent.com/55999192/119537708-2cf86e00-bd3f-11eb-977c-5252131a6b8e.PNG)
<br>
![screenshot2](https://user-images.githubusercontent.com/55999192/119537835-51544a80-bd3f-11eb-8580-aaf6fd6c9993.PNG)
<br>
![screenshot3](https://user-images.githubusercontent.com/55999192/120231186-bb6c6400-c205-11eb-848d-d3912bd5fe81.PNG)
