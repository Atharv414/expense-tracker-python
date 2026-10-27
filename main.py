import json
from expense import Expense

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        return [Expense.from_dict(item) for item in data]

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    data = [expense.to_dict() for expense in expenses]

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def show_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Show Category Summary")
    print("5. Exit")


expenses = load_expenses()

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = Expense(date, category, description, amount)
        expenses.append(expense)

        save_expenses(expenses)

        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            print("\n===== ALL EXPENSES =====")

            for i, expense in enumerate(expenses, start=1):
                print(f"\nExpense {i}")
                expense.display()

    elif choice == "3":
        total = sum(expense.amount for expense in expenses)

        print(f"\nTotal Expense: ₹{total:.2f}")

    elif choice == "4":
        if not expenses:
            print("No expenses found.")
        else:
            categories = {}

            for expense in expenses:
                if expense.category in categories:
                    categories[expense.category] += expense.amount
                else:
                    categories[expense.category] = expense.amount

            print("\n===== CATEGORY SUMMARY =====")

            for category, amount in categories.items():
                print(f"{category}: ₹{amount:.2f}")

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")