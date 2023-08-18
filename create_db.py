import sqlite3


connection = sqlite3.connect('my_data.db')

cursor = connection.cursor()

command = '''CREATE TABLE IF NOT EXISTS users
            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             full_name TEXT NOT NULL,
             username TEXT)'''

cursor.execute(command)
