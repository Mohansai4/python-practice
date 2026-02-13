import json

users_file = "users.json"
expenses_file = "expenses.json"

def load_file(name):
    try:
        with open(name, "r") as f:
            return json.load(f)
    except:
        return {}

def save_file(name, data):
    with open(name, "w") as f:
        json.dump(data, f)

users = load_file(users_file)
expenses = load_file(expenses_file)

def register():
    u = input("Username: ")
    p = input("Password: ")

    if u in users:
        print("User exists")
        return

    users[u] = p
    expenses[u] = []
    save_file(users_file, users)
    save_file(expenses_file, expenses)
    print("Registered.")

def login():
    u = input("Username: ")
    p = input("Password: ")

    if u in users and users[u] == p:
        print("Login successful")
        user_menu(u)
    else:
        print("Invalid credentials")

def user_menu(user):
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Logout")

        c = input("Choose: ")

        if c == "1":
            amt = float(input("Enter amount: "))
            expenses[user].append(amt)
            save_file(expenses_file, expenses)
            print("Saved.")
        elif c == "2":
            print("Expenses:", expenses[user])
            print("Total:", sum(expenses[user]))
        elif c == "3":
            break
        else:
            print("Invalid")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    ch = input("Choose: ")

    if ch == "1":
        register()
    elif ch == "2":
        login()
    elif ch == "3":
        break
    else:
        print("Invalid")
