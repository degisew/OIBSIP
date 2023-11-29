height = float(input("Enter your height(in Meters): "))
weight = float(input("Enter your weight(in kilograms): "))

def calculate_bmi(height, weight):
    if height <= 0:
        raise ValueError("Height must be greater than 0.")

    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    """
    Underweight: BMI less than 18.5
    Normal weight: BMI 18.5 to 24.9
    Overweight: BMI 25 to 29.9
    Obese: BMI 30 or greater

    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


bmi = calculate_bmi(height, weight)
bmi_category = classify_bmi(bmi)

print(f"BMI: {bmi}")
print(f"Category: {bmi_category}")