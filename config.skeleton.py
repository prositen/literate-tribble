import os

basedir = os.path.dirname(__file__)

DB_USER = ''
DB_PASSWORD = ''
DB_HOST = '127.0.0.1'
DB_NAME = 'tribble'
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{user}:{password}@{host}/{database}".format(user=DB_USER,
                                                                                              password=DB_PASSWORD,
                                                                                              host=DB_HOST,
                                                                                              database=DB_NAME)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'salt'

SECRET_KEY = 'ADD A SECRET KEY HERE'
ACCESS_LOG = "logs/access.log"

TRIBBLE_HOST = '0.0.0.0'
TRIBLE_PORT = 5060
DEBUG = True
