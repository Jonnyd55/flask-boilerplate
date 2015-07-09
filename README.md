# Boilerplate for a Flask App
=======

---
1. Make a virtualenv

	mkvirtualenv -p [python version] [virtualenv name]

2. Pull down repo

	git pull https://github.com/Jonnyd55/flask-boilerplate.git

3. Install reqs (This includes SQL connectors for both MySQL and PostGreSQL)

	pip install -r requirements.txt

4. Adjust database info

5. Edit models.py to create tables

6. Run create_db.py to build tables in database

7. Run migrate_db.py to setup migration tables and migration histories

8. Visit localhost:5000 
