import sqlite3
from app import DATABASE_NAME

class Meal:
    def __init__(self, id=None, name=None, date=None, mealcategory_id=None):
        self.id = id
        self.name = name
        self.date = date
        self.mealcategory_id = mealcategory_id
