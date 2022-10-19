import random
names_string=input("Give me everybody's name, seperated by a comma.\n")
names=names_string.split(", ")
num_items=len(names)
who_will_pay=random.choice(names) #
print(who_will_pay+" is going to buy the meal today!")