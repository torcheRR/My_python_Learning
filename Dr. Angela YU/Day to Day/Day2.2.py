print("Let's calculate your body mass index!!\n")
height = input("Enter your height in m: \n")
weight = input("Enter your weight in kg: \n")
bmi = int(weight)/float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)