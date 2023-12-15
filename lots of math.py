# Lots Of math
# Brayden Towner
# 10/23/2023

import math

print((100 - 5**3)/5)


print(math.sqrt(15/4 + 6))

print(24/4 + (2 ** 2))


cube_side = 4

print(f"The area of cube with a side length of {cube_side} is {6*cube_side**2}, while the volume of the cube is {cube_side**3}")


temperature = float(input("What Temperature (F) do you want to convert to Celsius? >  "))

print(f"{temperature}°F is {(temperature-32)*5/9}°C")


degrees = float(input("What angle in degrees do you want to convert to radians? >  "))

print(f"{degrees}° is {(degrees*math.pi/180)}rad")

problem_4_num1 = float(input("What is your 1st number? >  "))
problem_4_num2 = float(input("What is your 2nd number? >  "))

print(f"""
Addition = {problem_4_num1} + {problem_4_num2} = {problem_4_num1+problem_4_num2}
Subtraction = {problem_4_num1} - {problem_4_num2} = {problem_4_num1-problem_4_num2}
Product = {problem_4_num1} * {problem_4_num2} = {problem_4_num1*problem_4_num2}
Division = {problem_4_num1} / {problem_4_num2} = {problem_4_num1/problem_4_num2}
Exponential = {problem_4_num1}**{problem_4_num2} = {problem_4_num1**problem_4_num2}
Floor division = {problem_4_num1} // {problem_4_num2} = {problem_4_num1//problem_4_num2}
Modulus = {problem_4_num1} % {problem_4_num2} = {problem_4_num1%problem_4_num2}
""")