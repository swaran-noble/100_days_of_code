print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total_cost = 0

if size.lower()=='s':
    total_cost+=15
elif size.lower()=='m':
    total_cost+=20
elif size.lower()=='l':
    total_cost+=25
else:
    print("You have given wrong inputs")

if pepperoni.lower()=='y':
    if size.lower()=='s':
        total_cost+=2
    else:
        total_cost+=3

if extra_cheese.lower()=='y':
    total_cost+=1

print(f"Your final bill is ${total_cost}")                                