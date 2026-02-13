filename = "expenses.txt"

def add_expense():
    amount = input("Enter expense: ")
    with open(filename, "a") as f:
        f.write(amount + "\n")
    print("Saved.")

def view_expenses():
    try:
        with open(filename, "r") as f:
            data = f.read()
            print("\nExpenses:\n", data)
    except FileNotFoundError:
        print("No expenses found.")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
