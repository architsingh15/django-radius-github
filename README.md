# django-radius-github
A simple application serving as a issue tracker for public repositories on github using github API

Production Version of the Application:
`https://github-issue-trackerrr.herokuapp.com`
Admin Access of the Application:
`https://github-issue-trackerrr.herokuapp.com/admin`
username: admin
password: admin

Deployed on Heroku
, with POSTGRES add on as the DB
, runtime python 3.5.2
, served via Gunicorn 
, static files serving using Whitenoise
, Server side language Django
, Front End Bootstrap, JQuery

Application name: Issue Tracker

Options:
Add Repository: Receives a valid GitHub URL and gets the issues count via the GitHub API and stores it in the DataBase(Issue Registry)
Issue Registry: Displays the data that has been stored in the DataBase in a simple filterable way. 

Add Repository Specifics:
The input box only accepts valid GitHub URLs. 
Valid GitHub URLs format: 
`https://github.com/username/repository_name`

Error Pages in Add Repository:
400 Bad Request
403 Permission Denied
404 Page Not Found
Invalid Domain type: https://facebook.com/....
Private Repository URL input error
We cannot access the data of the Private GitHub Repositories

Issue Registry Specifics:
Pagination Implemented
Row Limit Implemented  
Search method across the table implemented 
Sort according to columns alphabetically or numerically implemented
 
Steps to set it up locally
1) git clone https://github.com/architsingh15/django-radius-github.git
2) cd django-radius-github
3) virtualenv venv -p /usr/bin/python3
4) source venv/bin/activate
5) pip3.5 install -r requirements.txt
6) ./manage.py makemigrations
7) ./manage.py migrate
8) ./manage.py runserver 
9) ./manage.py run_selenium_test to run test

