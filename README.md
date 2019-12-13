# EECS 341 (Databases) Project

Django-based web app with sqlalchemy  

Note that `debug=True` as I ran into some issues with static/admin files in the admin view. This also results in 404/500 views appearing quite often as SQL queries and GET requests in URLS (?id=9) are extremely fragile and must be exact (not case sensitive)

## TODO
- [x] Pages for individual object views (`Instructor`, `Course`, `Profile`)
- [x] `Favorite` function for users
- [x] Login view + user_auth 1:1 with `Profile`
- [x] Patch up custom SQL queries
- [x] `Mod/Ins/Del` pages (stretch, they show up for admin views only for course)
- [x] Anchor objects to pages on the `courses` view


## Publishing Guidelines

Don't commit to master branch unless you have a bug-free product. Instead, start your own branch:
 ```
 # Clone this repo to your local machine:
 git clone https://github.com/asfakianos/DB-Web-App.git
 # Make your own branch
 git branch <BRANCH-NAME>
 git checkout <BRANCH-NAME>
 # When pushing to origin (here), don't use master. Use your branch name:
 git push origin <BRANCH-NAME>
 # If you want to update your local branch, pull from your own branch rather than master:
 git pull origin <BRANCH-NAME>
 ```
 
If what you push to **your** branch is working on your end, make a pull request to the master branch, so we can merge it in to our master branch and work with it.

## Getting Started

Django is pretty easy to use, but has some confusing architecture to get started with. If you want to see a quick tutorial of how to navigate through Django, use this [link](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) to quickstart your own app. We're working mainly in the /scraper/ directory. You can also just run our current app with `python manage.py runserver` which will run a server by default at localhost:8000. We also have a requirements.txt in the base directory, which you can install with pip: `pip install -r requirements.txt`.

## Quick Start
Requires python3.* to run.

* Clone the repository
* `pip install -r requirements.txt` to install required packages
* Navigate to the repo_destination/db_proj/ directory
* Run the server with `./manage.py runserver` (May need to adjust user permissions and/or header path for executing like this)
  * Alternatively, run `./manage.py dbshell` to directly access the sqlite3 DBMS (note that table names are of the form scraper_<NAME> rather than just <NAME> as a way to manage multiple apps). 
* Navigate to [http://localhost:8000/](http://localhost:8000/) to start searching the database
* Navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/) to manage objects as an administrator (for insert/modify/delete)


