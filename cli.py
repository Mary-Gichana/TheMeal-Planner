
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

def manage_categories():
    while True:
        print("\n==== Manage Meal Categories ====")
        print("1. Add Category")
        print("2. Delete Category")
        print("3. List Categories")
        print("4. Find Category by ID")
        print("5. Go Back")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter category name: ").strip()
            if name:
                MealCategory.add_category(name)
                print("Category added.")
            else:
                print("Category name cannot be empty.")
        elif choice == "2":
            name = input("Enter category name to delete: ").strip()
            MealCategory.delete_category(name)
            print("Category deleted.")
        elif choice == "3":
            categories = MealCategory.find_all()
            if categories:
                for category in categories:
                    print(category)
            else:
                print("No categories found.")
        elif choice == "4":
            category_id = input("Enter category ID: ").strip()
            if category_id.isdigit():
                category = MealCategory.find_by_id(int(category_id))
                if category:
                    print(category)
                else:
                    print("Category not found.")
            else:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
        