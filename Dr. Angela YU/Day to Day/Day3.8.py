print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? \n"))
if height>=120:
    print("You can ride the rollercoaster!")
    bill=0
    age=int(input("What is your age? \n"))
    if age<12:
        print("Child tickets are $5.")
        bill=5
    elif age<=18:
        print("Youth tickets are $7.")
        bill=7
    elif age>18 and age<45:
        print("Adult tickects are $12.")
        bill=12
    elif age>=45 and age<=55:
        print("You have a free ride on us!!")
    wants_photo=(input("Do you want a photo taken? Y or N. \n"))
    if wants_photo=="Y" :
        bill+=3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")