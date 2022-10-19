year=int(input("Which year do you want to check? \n"))
if year%4==0 | year%100==0 | year%400==0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")