print("Welcome to the tip calculator!\n")

total_bill = float(input("What is the total bill? $"))

tip = int(input("How much tip would you like to give?10,12 or 15?"))

final_bill = total_bill * (1 + tip/100)

people = int(input("How many people to split the bill?"))

print(f"Each person should pay:{round(final_bill/people,2)}")