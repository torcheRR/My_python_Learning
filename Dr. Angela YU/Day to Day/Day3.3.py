print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? \n"))
if height>=120:
    age=int(input("What is your age? \n"))
    if age>18:
        print("Please pay $12")
    elif 12<age<=18:
        print("Please pay $7")
    else:
        print("Please pay $5")
else:
    print("You have to grow taller before you can ride.")