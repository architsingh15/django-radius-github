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

DB schema in issue_tracker/models.py 

Application Logic:
1) The Add to Registry page will accept a valid GitHub Public URL
2) On clicking submit the URL will be attached as payload to a POST request to an API named validate_url
3) The API will validate the URL, parse for the username and repository_name, call the GitHub '/issues' API for the issues_data, process the data and save it in the DataBase
4) Will redirect to the Issues Registry where all the data that has been stored in the DB is displayed 

  