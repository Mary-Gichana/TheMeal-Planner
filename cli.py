
from datetime import datetime
from app import create_database
from models.meal import Meal
from models.mealcategory import MealCategory

create_database()

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return None
