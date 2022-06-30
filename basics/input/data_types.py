name = input("What is your name human ?")
age = int(input("How old are u in years ?"))
height = float(input("How tall are you ?"))
weight = float(input("How much do u wait in kg ?"))

bmi = weight / (height**2)

print(f"{name}, you are {age} years old and your bmi is {bmi:.2f}")

