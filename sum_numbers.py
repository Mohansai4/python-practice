total = 0

for i in range(1, 3):
    num = input("Enter number: ")

    if num == "":
        print("Please enter a valid number")
        continue

    total += int(num)

print("Total:", total)