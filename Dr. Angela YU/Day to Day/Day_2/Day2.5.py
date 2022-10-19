print("Welcome to tip calculator.")
totalbill=float(input("What was the total bill? $"))
percentage=int(input("What percenbtage tip would you like to give? 10 ,12 or 15?"))
split=int(input("How many people to split the bill?"))
billwithtip=totalbill*percentage/100+totalbill
splitedbill=round(billwithtip/split, 2)
print(f"Each person should pay: ${splitedbill}")