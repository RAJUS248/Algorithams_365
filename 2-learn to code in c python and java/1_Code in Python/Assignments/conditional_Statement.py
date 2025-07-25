""" Python – Conditional Statements Assignment Questions """
# --------------------------------------------------------------------------------------------------------------------
# 1.	Write a Python program to check if a number is positive, negative, or zero.

number = 0

if (number > 0):
    print("Number is positive")

elif (number < 0):
    print("Number is negative")

else:
    print("The number is Zero")
# --------------------------------------------------------------------------------------------------------------------

# 2.Given a student’s score, write a program to print “Pass” if score ≥ 40, otherwise print “Fail”.

Score = 40

if(Score >= 40):
    print("Pass")

else:
    print("Fail")
# --------------------------------------------------------------------------------------------------------------------

# 3.Write a program that checks if a given year is a leap year.
#ChatGPT

year = 2025

if year % 400 == 0:
    print(f"{year} is leap year")

elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is leap year")

else:
    print(f"{year} is not a leap year")
# --------------------------------------------------------------------------------------------------------------------

# 4.Given 3 integers, write a program to find the largest number using if-elif-else.

def largest_number(num1,num2,num3):

    if num1 >= num2 and num1 >= num3:
        print(f"The largest number is {num1}")

    elif num2 >= num1 and num2 >= num3:
        print(f"The largest number is {num2}")

    else:
        print(f"The largest number is {num3}")
largest_number(50,20,40)
# --------------------------------------------------------------------------------------------------------------------

# 5.Evaluate if a candidate passes technical round using:
# o	coding_skill ≥ 4
# o	problem_solving ≥ 4
# o	cs_fundamentals ≥ 4
# (Use and operator)

def technical_round(coding_skill,problem_solving,cs_fundamentals):

    if coding_skill >= 4 and problem_solving >= 4 and cs_fundamentals >= 4:
        print("you Pass the technical round")

    else:
        print("you fail better luck next time ")

technical_round(3,4,5)
# --------------------------------------------------------------------------------------------------------------------

# 6.Check if a candidate meets communication and CGPA criteria:
# o	CGPA ≥ 7.0
# o	communication ≥ 3

def criteria(CGPA:float,communication:float):

    if CGPA >= 7.0 and communication >= 3 :
        print("meet the criteria")

    else:
        print("not meet the criteria")

criteria(8.7,3)
# --------------------------------------------------------------------------------------------------------------------

# 7.Based on inputs, decide hiring decision using nested if:
# o	Check technical first, then CGPA & communication

def hiring_decision(technical:int,CGPA:float,communication:int):

    if technical >= 4:
        
        if CGPA >= 5.0:
           
            if communication >= 5:
               
               print("Pass")

            else:
                print("fail due to communiction score")

        else:
            print("fail due to CGPA score")

    else:
        print("fail due to technical score")
        
hiring_decision(4,7,5)
# --------------------------------------------------------------------------------------------------------------------

# 8.Write a program to check if a number is divisible by both 3 and 5 using and.

def number_divisible(number):

    if number % 3 == 0 and number % 5 == 0:
        print("the number is divisible by 3 and 5 \n")

    else:
        print("the nuber is not divisible by both \n")

number_divisible(10)
# --------------------------------------------------------------------------------------------------------------------
# 9.Given a list of candidates with CGPAs, print “Fast-Track” if CGPA > 9 or communication ≥ 4
"""ChatGPT"""

def list_of_candidates(CGPA:list,communication:list) -> list:
    for i in range(len(CGPA)):
        if CGPA[i] > 9 or communication[i] >= 4:
            print(f"Fast-Track {i+1}")

    else:
        print(f"do good {i+1}")

list_of_candidates([9,5,6],[4,5,3])
# OR 
candidates = [
    {"name": "Alice", "cgpa": 9.2, "communication": 3},
    {"name": "Bob", "cgpa": 8.5, "communication": 4},
    {"name": "Charlie", "cgpa": 7.8, "communication": 3},
    {"name": "David", "cgpa": 9.5, "communication": 5},
]

for candidate in candidates:
    if candidate["cgpa"] > 9 or candidate["communication"] >= 4:
        print(f"{candidate['name']} -> Fast-Track")
    else:
        print(f"{candidate['name']} -> Regular Process")
# --------------------------------------------------------------------------------------------------------------------

# 10.Write a program using not to check if a person is not eligible for a scholarship (i.e., CGPA < 6).

def scholarship_eligibility(CGPA:float):
    if CGPA  < 6:
        print("\nNot Eligible for scholarship ")
    else:
        print("\nEligible for scholarship")

scholarship_eligibility(5.9)