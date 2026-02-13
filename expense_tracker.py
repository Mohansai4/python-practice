expenses = []

while True:
    amount = input("Enter expense (or 'q' to quit): ")

    if amount == "q":
        break

    expenses.append(float(amount))

print("All expenses:", expenses)
print("Total spent:", sum(expenses))
