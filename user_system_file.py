filename = "users.txt"

def load_users():
    users = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                users[u] = p
    except FileNotFoundError:
        pass
    return users

def save_user(username, password):
    with open(filename, "a") as f:
        f.write(username + "," + password + "\n")

users = load_users()

def register():
    username = input("Create username: ")
    password = input("Create password: ")

    if username in users:
        print("User already exists")
        return

    users[username] = password
    save_user(username, password)
    print("User registered and saved.")

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

    choice = input("Choose option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
