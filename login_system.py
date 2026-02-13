users = {
    "mohan": "1234",
    "admin": "admin"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid credentials")
