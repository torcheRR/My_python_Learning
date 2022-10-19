print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? \n"))

if height>= 120:
    if int(input("What is your age? \n"))>=18:
        print("You can ride the rollercoaster!")
    else:
        print("Sorry, you have to grow up.")
else:
    print("Sorry, you have to grow taller before you can ride.")