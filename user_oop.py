class UserSystem:
    def __init__(self):
        self.users = {}

    def register(self):
        username = input("Create username: ")
        password = input("Create password: ")
        self.users[username] = password
        print("User registered.")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        if username in self.users and self.users[username] == password:
            print("Login successful!")
        else:
            print("Invalid credentials")

app = UserSystem()

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        app.register()
    elif choice == "2":
        app.login()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
