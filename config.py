import os
basedir = os.path.abspath(os.path.dirname(__file__))

#For POSTGRESQL INSTALLS
#SQLALCHEMY_DATABASE_URI = 'postgresql://<user>:<password>@<datbase location (localhost)>/<database name>

#FOR MYSQL INSTALLS
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:root@127.0.0.1:8889/test_db'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
