# Boilerplate for a Flask App

---
Make a virtualenv, create project foler

	mkvirtualenv -p [python version] [virtualenv name]
	mkdir flask-project
	cd flask-project

Pull down repo

	git clone https://github.com/Jonnyd55/flask-boilerplate.git

Install reqs (This includes SQL connectors for both MySQL and PostGreSQL)

	pip install -r requirements.txt

Adjust database info

Edit models.py to create tables

Run create_db.py to build tables in database

Run migrate_db.py to setup migration tables and migration histories

Turn on server

	python run.py

Visit localhost:5000 
