import json

filename = "users.json"

def load_users():
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(filename, "w") as f:
        json.dump(users, f)

users = load_users()

def register():
    username = input("Create username: ")
    password = input("Create password: ")

    if username in users:
        print("User already exists")
        return

    users[username] = password
    save_users(users)
    print("User registered.")

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid credentials")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
