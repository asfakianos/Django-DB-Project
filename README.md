# EECS 341 (Databases) Project

## TODO
- [ ] Pages for individual object views (`Instructor`, `Course`, `Profile`)
- [ ] `Favorite` function for users
- [ ] Login view + user_auth 1:1 with `Profile`
- [ ] Patch up custom SQL queries
- [ ] `Mod/Ins/Del` pages (stretch, they show up for admin views only for course)

Django-based web app with sqlalchemy
Our goal is to maintain a relational database with the following tables:
Course(course_id, prereqs, dept, units, name), Instructor(name, dept), Department(name, address, school), School(name), and some sort of user model that is TBD.

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

