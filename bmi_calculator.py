import math
height = float(input("Enter your height(in Meters): "))
weight = float(input("Enter your weight(in kilograms): "))

def bmi_calculator():
    if height <= 0:
        raise ValueError("Height must be greater than 0.")

    bmi = weight / (height ** 2)
    return round(bmi, 2)


print(bmi_calculator())