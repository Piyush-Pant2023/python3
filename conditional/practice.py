# Python program demonstrating conditional statements

# Ask for user input
age = int(input("Enter your age: "))

# Conditional statements
if age < 0:
    print("Age cannot be negative!")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Additional example: Check if a number is even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Nested if example: Grading system
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")
