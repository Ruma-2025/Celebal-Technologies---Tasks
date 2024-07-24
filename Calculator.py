def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = int(input("Choose an operation (1/2/3/4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == 1:
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == 2:
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == 3:
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == 4:
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")
