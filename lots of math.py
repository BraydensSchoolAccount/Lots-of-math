# Lots Of math
# Brayden Towner
# 10/23/2023

import math, os


PROBLEM_1={
    "TO_SUBTRACT_CUBED" : 5,
    "TO_SUBTRACT_FROM" : 100,
    "FINAL_DIVIDING_NUM" : 5
}

print((PROBLEM_1["TO_SUBTRACT_FROM"] -PROBLEM_1["TO_SUBTRACT_CUBED"]**3)/PROBLEM_1["FINAL_DIVIDING_NUM"])

os.system("pause")

PROBLEM_2={
    "TO_ADD_POST_DIV" : 6,
    "TO_DIVIDE" : 15,
    "DIVIDE_BY" : 4
}

print(math.sqrt(PROBLEM_2["TO_DIVIDE"]/PROBLEM_2["DIVIDE_BY"] + PROBLEM_2["TO_ADD_POST_DIV"]))

os.system("pause")

PROBLEM_3={
    "ADD_AS_SQUARED" : 2,
    "TO_DIVIDE" : 24,
    "DIVIDE_BY" : 4
}

print(int(PROBLEM_3["TO_DIVIDE"]/PROBLEM_3["DIVIDE_BY"]) + (PROBLEM_3["ADD_AS_SQUARED"] ** 2))

os.system("pause")

cube_side = 4

print(f"The area of cube with a side length of {cube_side} is {6*cube_side**2}, while the volume of the cube is {cube_side**3}")

os.system("pause")

temperature = float(input("What Temperature (F) do you want to convert to Celsius? >  "))

print(f"{temperature}°F is {(temperature-32)*5/9}°C")

os.system("pause")

degrees = float(input("What angle in degrees do you want to convert to radians? >  "))

print(f"{degrees}° is {(degrees*math.pi/180)}rad")