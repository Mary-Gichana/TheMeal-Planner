import sqlite3

DATABASE_NAME = 'database.db'

def create_database():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mealcategory (
                id INTEGER PRIMARY KEY ,
                name TEXT UNIQUE NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS meals (
                id INTEGER PRIMARY KEY ,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                mealcategory_id INTEGER NOT NULL,
                FOREIGN KEY(mealcategory_id) REFERENCES mealcategory(id) 
            )
        ''')