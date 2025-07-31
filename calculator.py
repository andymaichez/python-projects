a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Choose an operation (+, -, *, /): ")

if op == '+':
    print(f"{a} + {b} = {a + b}")
elif op == '-':
    print(f"{a} - {b} = {a - b}")
elif op == '*':
    print(f"{a} * {b} = {a * b}")
elif op == '/':
    print("Error: Cannot divide by zero." if b == 0 else f"{a} / {b} = {a / b}")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
