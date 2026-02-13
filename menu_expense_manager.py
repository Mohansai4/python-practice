expenses = []

def add_expense():
    amount = float(input("Enter expense amount: "))
    expenses.append(amount)
    print("Expense added.")

def view_expenses():
    print("All expenses:", expenses)
    print("Total spent:", sum(expenses))

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
