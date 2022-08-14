age=input("What is your current age?\n")
left_life_year=90-int(age)
life_left_month=90*12-int(age)*12
life_left_week=90*52-int(age)*52
life_left_days=90*365-int(age)*365

print(f"You have {left_life_year} years, {life_left_month} months, {life_left_week} weeks and {life_left_days} days left to live!")
