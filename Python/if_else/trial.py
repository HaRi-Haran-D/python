weight = float(input("Enter your weight in Kg"))
height = float(input("Enter your height in mtr"))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18:
    print("UnderWeight")
elif bmi < 24:
    print("Normal")
else:
    print("Overweight")
