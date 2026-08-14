#Expense Tracker — Project
import json
import 

FILE_NAME = "expenses.json"

expenses = []
budget = 0


def load_data():
    global expenses, budget

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            expenses = data.get("expenses", [])
            budget = data.get("budget", 0)

        except:
            expenses = []
            budget = 0


def save_data():
    data = {
        "expenses": expenses,
        "budget": budget
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_expense():
    print("\n========== ADD EXPENSE ==========")

    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Invalid amount!")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_data()

    print("\nExpense added successfully!")


def view_expenses():
    print("\n========== ALL EXPENSES ==========")

    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. ₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )

    print("==================================")


def total_spending():
    print("\n========== TOTAL SPENDING ==========")

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total Spending: ₹{total:.2f}")

    if budget > 0:
        remaining = budget - total

        print(f"Budget: ₹{budget:.2f}")

        if remaining >= 0:
            print(f"Remaining: ₹{remaining:.2f}")
        else:
            print(f"⚠️ Budget exceeded by: ₹{abs(remaining):.2f}")

    print("====================================")


def category_summary():
    print("\n========== CATEGORY SUMMARY ==========")

    if not expenses:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] += expense["amount"]

    for category, amount in categories.items():
        print(f"{category:<15} : ₹{amount:.2f}")

    print("--------------------------------------")

    total = sum(categories.values())
    print(f"{'Total':<15} : ₹{total:.2f}")

    print("======================================")


def highest_expense():
    print("\n========== HIGHEST EXPENSE ==========")

    if not expenses:
        print("No expenses found.")
        return

    highest = max(expenses, key=lambda x: x["amount"])

    print(f"Amount      : ₹{highest['amount']:.2f}")
    print(f"Category    : {highest['category']}")
    print(f"Description : {highest['description']}")

    print("=====================================")


def delete_expense():
    print("\n========== DELETE EXPENSE ==========")

    if not expenses:
        print("No expenses found.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))
    except ValueError:
        print("Invalid number!")
        return

    if number < 1 or number > len(expenses):
        print("Invalid expense number!")
        return

    deleted = expenses.pop(number - 1)

    save_data()

    print(
        f"\nDeleted: ₹{deleted['amount']:.2f} | "
        f"{deleted['category']} | "
        f"{deleted['description']}"
    )


def search_expense():
    print("\n========== SEARCH EXPENSE ==========")

    if not expenses:
        print("No expenses found.")
        return

    category = input("Enter category to search: ").strip().lower()

    found = False

    for i, expense in enumerate(expenses, 1):
        if expense["category"].lower() == category:
            print(
                f"{i}. ₹{expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['description']}"
            )
            found = True

    if not found:
        print("No expenses found for this category.")

    print("====================================")


def set_budget():
    global budget

    print("\n========== SET BUDGET ==========")

    try:
        amount = float(input("Enter monthly budget: ₹"))
    except ValueError:
        print("Invalid amount!")
        return

    if amount < 0:
        print("Budget cannot be negative.")
        return

    budget = amount

    save_data()

    print(f"\nBudget set to ₹{budget:.2f}")


def budget_status():
    print("\n========== BUDGET STATUS ==========")

    if budget == 0:
        print("No budget has been set.")
        return

    total = sum(expense["amount"] for expense in expenses)
    remaining = budget - total

    print(f"Budget : ₹{budget:.2f}")
    print(f"Spent  : ₹{total:.2f}")

    if remaining >= 0:
        print(f"Left   : ₹{remaining:.2f}")
        print("Status : Within Budget")
    else:
        print(f"Extra  : ₹{abs(remaining):.2f}")
        print("Status : ⚠️ Budget Exceeded")

    print("==================================")


def clear_expenses():
    global expenses

    print("\n========== CLEAR EXPENSES ==========")

    if not expenses:
        print("No expenses to clear.")
        return

    confirmation = input(
        "Are you sure you want to delete ALL expenses? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        expenses = []
        save_data()
        print("All expenses deleted.")
    else:
        print("Operation cancelled.")


def show_menu():
    print("""
========================================
           💰 EXPENSE TRACKER
========================================

1. Add Expense
2. View Expenses
3. Total Spending
4. Category Summary
5. Highest Expense
6. Delete Expense
7. Search Expense
8. Set Budget
9. Budget Status
10. Clear All Expenses
11. Exit

========================================
""")


def main():
    load_data()

    print("""
========================================
       WELCOME TO EXPENSE TRACKER
========================================
""")

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_spending()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            highest_expense()

        elif choice == "6":
            delete_expense()

        elif choice == "7":
            search_expense()

        elif choice == "8":
            set_budget()

        elif choice == "9":
            budget_status()

        elif choice == "10":
            clear_expenses()

        elif choice == "11":
            save_data()
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
