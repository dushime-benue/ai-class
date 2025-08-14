# program to check pionts
def check_point(points):
    if points > 36:
        return 'sorry, you have failed'
    else:
        return 'congratulation, you have passed'

user_points= int(input('enter your points'))
result_points= check_point(user_points)

print(result_points)Here’s a simple Python program to create a calculator using if, elif, and else statements. This program takes two numbers as input and performs basic arithmetic operations like addition, subtraction, multiplication, and division based on the user's choice.

Copy code
# Simple Calculator in Python

# Input: Two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Input: User's choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform the operation based on the user's choice
if choice == '1':
    print(f"The result is: {num1 + num2}")
elif choice == '2':
    print(f"The result is: {num1 - num2}")
elif choice == '3':
    print(f"The result is: {num1 * num2}")
elif choice == '4':
    if num2 != 0:  # Check for division by zero
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input! Please select a valid operation.")

How it works:
The program prompts the user to input two numbers.
It displays a menu of operations (add, subtract, multiply, divide).
Based on the user's choice, the corresponding operation is performed using if, elif, and else.
The program handles division by zero gracefully by checking if the second number is zero before performing division.

This is a simple and beginner-friendly implementation of a calculator in Python!Here’s a simple Python program to create a calculator using if, elif, and else statements. This program takes two numbers as input and performs basic arithmetic operations like addition, subtraction, multiplication, and division based on the user's choice.

Copy code
# Simple Calculator in Python

# Input: Two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Input: User's choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform the operation based on the user's choice
if choice == '1':
    print(f"The result is: {num1 + num2}")
elif choice == '2':
    print(f"The result is: {num1 - num2}")
elif choice == '3':
    print(f"The result is: {num1 * num2}")
elif choice == '4':
    if num2 != 0:  # Check for division by zero
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input! Please select a valid operation.")

How it works:
The program prompts the user to input two numbers.
It displays a menu of operations (add, subtract, multiply, divide).
Based on the user's choice, the corresponding operation is performed using if, elif, and else.
The program handles division by zero gracefully by checking if the second number is zero before performing division.

This is a simple and beginner-friendly implementation of a calculator in Python!Here’s a simple Python program to create a calculator using if, elif, and else statements. This program takes two numbers as input and performs basic arithmetic operations like addition, subtraction, multiplication, and division based on the user's choice.

Copy code
# Simple Calculator in Python

# Input: Two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Input: User's choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform the operation based on the user's choice
if choice == '1':
    print(f"The result is: {num1 + num2}")
elif choice == '2':
    print(f"The result is: {num1 - num2}")
elif choice == '3':
    print(f"The result is: {num1 * num2}")
elif choice == '4':
    if num2 != 0:  # Check for division by zero
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input! Please select a valid operation.")

How it works:
The program prompts the user to input two numbers.
It displays a menu of operations (add, subtract, multiply, divide).
Based on the user's choice, the corresponding operation is performed using if, elif, and else.
The program handles division by zero gracefully by checking if the second number is zero before performing division.

This is a simple and beginner-friendly implementation of a calculator in Python!