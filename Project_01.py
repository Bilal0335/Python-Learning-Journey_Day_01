# ! Assignment

'''

Write a Python program where you:
Declare multiple variables using your own name.
Assign different values to those variables, ensuring that you include various data types such as string, integer, float.
Use comments to explain each variable and its data type.
Print all variables using the print() function.

'''

# Declare variables
name = "Bilal"

age=20

height = 5.0

is_student = True

# Print variables

# print("Name: ", name)

# print("Age: ", age)

# print("Height: ", height)

# print("Is Student: ", is_student)



# ! Project 

'''
📌 Project Description:
Create a Python program that collects a student's basic information, performs some calculations, and displays the results using the concepts learned in Week 1.

📌 Project Requirements:

1: Input and Variables:
Ask the user for their name, age, and marks in three subjects.
Store these values in appropriate variables.


2: Typecasting:
Convert the marks (string input) to integers for calculations.


3: Operators:
Calculate the total marks and average marks using arithmetic operators.


4:String Operations:
Print a formatted output that includes the student’s name, total marks, and average.
Use string concatenation or f-strings for a clean output.

'''

#! Q1:
'''Input and Variables:
Ask the user for their name, age, and marks in three subjects.
Store these values in appropriate variables.
'''
# name =str(input("Enter Your Name: "))
# age=int(input("Enter Your Age: "))
# eng = input("Enter Your English Marks: ")
# urdu = input("Enter Your Urdu Marks: ")
# computer = input("Enter Your Computer Marks: ")

#! Q2: 
'''
Typecasting:
Convert the marks (string input) to integers for calculations.
'''

name =str(input("Enter Your Name: "))
age=int(input("Enter Your Age: "))
eng = int(input("Enter Your English Marks: "))
urdu = int(input("Enter Your Urdu Marks: "))
computer = int(input("Enter Your Computer Marks: "))

#! Q3:
'''
Operators:
Calculate the total marks and average marks using arithmetic operators.

'''

total_num = eng + computer + urdu
avg = total_num / 3

#! Q4:

'''
String Operations:
Print a formatted output that includes the student’s name, total marks, and average.
Use string concatenation or f-strings for a clean output.

'''

print(f"Your Name: {name.title()}\nYour Age: {age}\nYour Marks Three Subjects: {avg:.2f}")