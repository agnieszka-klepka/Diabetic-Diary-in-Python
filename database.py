import sqlite3
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def createTable(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, table, *values):
        self.cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?' for _ in values])})", values)
        self.connection.commit()

    def printData(self):
        self.cursor.execute('SELECT * from diabetes')
        return self.cursor.fetchall()
