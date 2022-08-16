print("Let's calculate your body mass index!!\n")
height = input("Enter your height in m: \n")
weight = input("Enter your weight in kg: \n")
bmi = int(weight)/float(height)**2
bmi_as_int = int(bmi)
if bmi_as_int<18.5:
    print(f"Your BMI is {bmi_as_int}, you have an underweight.")
elif bmi_as_int<25:
    print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
elif bmi_as_int<30:
    print(f"Your BMI is {bmi_as_int}, you have an overweight.")
elif bmi_as_int<35:
    print(f"Your BMI is {bmi_as_int}, you have an obese")
else:
    print(f"Your BMI is {bmi_as_int}, you have a clinically obese.")