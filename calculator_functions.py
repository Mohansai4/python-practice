def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (+ - * /): ")

if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", sub(a, b))
elif op == "*":
    print("Result:", mul(a, b))
elif op == "/":
    print("Result:", div(a, b))
else:
    print("Invalid operation")
