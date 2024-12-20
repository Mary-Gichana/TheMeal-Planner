import sqlite3
from app import DATABASE_NAME

class MealCategory:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"MealCategory({self.id}, {self.name})"
