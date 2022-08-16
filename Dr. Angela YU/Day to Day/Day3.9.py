print("Welcome to the Love Calculator!")
name1=input("What is your name? \n")
name2=input("What is their name? \n")
lower_1=name1.lower
onlarbasamagi=lower_1.count("t") + lower_1.count("r") + lower_1.count("u") + lower_1.count("e")
lower_2=name2.lower
birlerbasamagi=int(lower_2.count("l")) + int(lower_2.count("o")) + int(lower_2.count("v")) + int(lower_2.count("e"))
sonsayi=onlarbasamagi+birlerbasamagi
if sonsayi<10 and sonsayi>90:
    print(f"Your score is {sonsayi}, you go together like coke and mentos.")
elif sonsayi<=50 and sonsayi>=40:
    print(f"Your score is {sonsayi}, you are alright together.")
else:
    print(f"Your score is {sonsayi}.")