import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses():
    """Load saved expenses from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved data. Starting with an empty list.")
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4, ensure_ascii=False)
    except OSError as error:
        print(f"Error saving expenses: {error}")


def get_positive_amount():
    """Ask the user for a positive expense amount."""
    while True:
        try:
            amount = float(input("Enter amount: ₹").strip())
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Please enter a valid number.")


def get_category():
    """Ask for and normalize an expense category."""
    while True:
        category = input("Enter category: ").strip()
        if category:
            return category.title()
        print("Category cannot be empty.")


def add_expense(expenses):
    """Add a new expense."""
    print("\n--- Add Expense ---")

    name = input("Enter expense name: ").strip()
    if not name:
        print("Expense name cannot be empty.")
        return

    amount = get_positive_amount()
    category = get_category()

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    """Display all recorded expenses."""
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:>2}. {expense['date']} | "
            f"{expense['name']:<20} | "
            f"₹{expense['amount']:>8.2f} | "
            f"{expense['category']}"
        )


def show_total(expenses):
    """Display total spending."""
    total = sum(expense["amount"] for expense in expenses)
    print("\n--- Total Spending ---")
    print(f"Total spent: ₹{total:.2f}")


def category_summary(expenses):
    """Display spending totals grouped by category."""
    print("\n--- Spending by Category ---")

    if not expenses:
        print("No expenses found.")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    for category, total in sorted(totals.items()):
        print(f"{category:<20} ₹{total:.2f}")


def search_category(expenses):
    """Show expenses matching a category."""
    if not expenses:
        print("\nNo expenses found.")
        return

    category = input("\nEnter category to search: ").strip().lower()
    if not category:
        print("Category cannot be empty.")
        return

    matches = [
        expense
        for expense in expenses
        if expense["category"].lower() == category
    ]

    if not matches:
        print("No expenses found in that category.")
        return

    print(f"\n--- Expenses in '{category.title()}' ---")
    for expense in matches:
        print(
            f"{expense['date']} | {expense['name']} | "
            f"₹{expense['amount']:.2f}"
        )


def delete_expense(expenses):
    """Delete an expense by its displayed number."""
    if not expenses:
        print("\nNo expenses to delete.")
        return

    view_expenses(expenses)

    while True:
        choice = input("\nEnter expense number to delete (0 to cancel): ").strip()
        try:
            number = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if number == 0:
            print("Delete cancelled.")
            return

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)
            print(
                f"Deleted: {removed['name']} "
                f"(₹{removed['amount']:.2f})"
            )
            return

        print("Invalid expense number.")


def display_menu():
    """Display the application menu."""
    print("\n" + "=" * 42)
    print("           EXPENSE TRACKER")
    print("=" * 42)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Search by Category")
    print("5. Spending by Category")
    print("6. Delete Expense")
    print("7. Exit")
    print("=" * 42)


def main():
    """Run the Expense Tracker."""
    expenses = load_expenses()

    print("Welcome to Expense Tracker!")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            search_category(expenses)
        elif choice == "5":
            category_summary(expenses)
        elif choice == "6":
            delete_expense(expenses)
        elif choice == "7":
            print("Thanks for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
