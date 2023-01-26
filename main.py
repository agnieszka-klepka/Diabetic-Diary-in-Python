import sys
from os import getenv

from database import Database

'''
    command to create database: python3 controller.py setupDB
'''
if len(sys.argv) == 2 and sys.argv[1] == "setupDB":
    print("Creating database")
    db = Database(getenv('DB_NAME'))
    db.createTable('''CREATE TABLE diabetes (id INTEGER PRIMARY KEY AUTOINCREMENT, sugarLevel INTEGER, measurementDay 
    TEXT) ''')
