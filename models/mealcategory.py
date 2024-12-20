import sqlite3
from app import DATABASE_NAME

class MealCategory:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"MealCategory({self.id}, {self.name})"
    
    def add_category(name):
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO mealcategory (name) VALUES (?)', (name,))
            conn.commit()
