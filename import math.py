import random

print("===== Advanced Calculator =====")

# Take first number or generate random
num1 = input("Enter first number (or press Enter for random): ")
if num1 == "":
    num1 = random.randint(1, 1000)
    print(f"Randomly selected first number: {num1}")
else:
    num1 = float(num1)

# Take second number or generate random
num2 = input("Enter second number (or press Enter for random): ")
if num2 == "":
    num2 = random.randint(1, 100)
    print(f"Randomly selected second number: {num2}")
else:
    num2 = float(num2)

# Operation choice
print("\nChoose an operation 1 to 8 :")
print(" 1 : + : Addition")
print(" 2 : - : Subtraction")
print(" 3 : * : Multiplication")
print(" 4 : / : Division")
print(" 5 : ** : Power")
print(" 6 : % : Modulus")
print(" 7 : ^ : Exponentiation")
print(" 8 :&&: Logical AND")
operation = input("Enter operation: ")
operation =input("exit th program  and start the program ones again")
# Perform calculation
if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

elif operation == "**":
    result = num1 ** num2

elif operation == "%":
    result = num1 % num2

elif operation =="^":
    result =num1 ** num2

elif operation == "&&":
    result = num1 and num2 

elif operation == "//":
    if num2 != 0:
        result = num1 // num2
    else:
        result = "Error! Division by zero."
        


else:
    result = "Invalid operation!"

print("\n===== Result =====")
print(f"{num1} {operation} {num2} = {result}")
exit = input("Do you want to exit the program?( yes/no): ")
if exit.lower() =="yes":
    print( "exiting the program  and restart the program ones again")
    