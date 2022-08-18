print("Welcome to the Love Calculator!")
name1=str(input("What is your name? \n"))
name2=str(input("What is their name? \n"))
lower_1=name1.lower()
lower_2=name2.lower()
onlarbasamagi=int(lower_1.count("t") + lower_1.count("r") + lower_1.count("u") + lower_1.count("e") +lower_2.count("t") + lower_2.count("r") + lower_2.count("u") + lower_2.count("e") )*10
birlerbasamagi=int((lower_1.count("l")) + lower_1.count("o") + lower_1.count("v") + lower_1.count("e") + (lower_2.count("l")) + lower_2.count("o") + lower_2.count("v") + lower_2.count("e"))
sonsayi=onlarbasamagi+birlerbasamagi
if sonsayi<10 or sonsayi>90:
    print(f"Your score is {sonsayi}, you go together like coke and mentos.")
elif sonsayi<=50 and sonsayi>=40:
    print(f"Your score is {sonsayi}, you are alright together.")
else:
    print(f"Your score is {sonsayi}.")