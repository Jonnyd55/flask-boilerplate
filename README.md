# Boilerplate for a Flask App

---
Make a virtualenv

	mkvirtualenv -p [python version] [virtualenv name]

Pull down repo

	git pull https://github.com/Jonnyd55/flask-boilerplate.git

Install reqs (This includes SQL connectors for both MySQL and PostGreSQL)

	pip install -r requirements.txt

Adjust database info

Edit models.py to create tables

Run create_db.py to build tables in database

Run migrate_db.py to setup migration tables and migration histories

Visit localhost:5000 
