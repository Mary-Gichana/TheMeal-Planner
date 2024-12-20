import sqlite3
from app import DATABASE_NAME

class Meal:
    def __init__(self, id=None, name=None, date=None, mealcategory_id=None):
        self.id = id
        self.name = name
        self.date = date
        self.mealcategory_id = mealcategory_id

   
    def __repr__(self):
        return f"Meal({self.id}, {self.name}), {self.date}, {self.mealcategory_id})"
    
    def add_meal(name, date, mealcategory_id):
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO meals (name, date, mealcategory_id) VALUES (?, ?, ?)', 
                           (name, date, mealcategory_id))
            conn.commit()

    def delete_meal(meal_id):
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM meals WHERE id = ?', (meal_id,))
            conn.commit()

    def find_all():
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM meals')
            return cursor.fetchall()
        
    def find_by_id(meal_id):
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM meals WHERE id = ?', (meal_id,))
            return cursor.fetchone()

