# REST-API

__Description:__

  This is REST based postings app build upon Django REST Framework.
  
__Technology Stack:__

_Back-end:_ &nbsp;&nbsp;Django1.9 (Python 2.7) and Django REST

_Database:_ &nbsp;&nbsp;dbsqlite3

__Instructions:__

 
  1.Make a directory in your local machine and create a virtual environment by `python3 -p virtualenv .`

  2.Clone this repo in that directory and ensure to install the requirements by `pip install -r requirments.txt` 
  
  3.Make the migrations to create the database by `python3 manage.py makemigrations` followed by `python3 manage.py migrate`
  
  4.Create superuser by using the command `python3 manage.py createsuperuser`

  5.To run the application open terminal and change directory to the manage.py in the Blog-app/mysite folder.Now run the command `python3 mange.py runserver` and the app goes live in your machine.

