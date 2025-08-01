from art import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print(logo)
    calculate = True
    num1 = int(input("Please enter the first numer:"))
    while calculate:
        for symbol in operations:
            print(symbol)
        operator = input("Please enter the operator you want to use from the above:")
        num2=int(input("Please enter the second number:"))
        answer = operations[operator](num1,num2)
        print(f"{num1} {operator} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice=="y":
            num1=answer
        else:
            calculate=False
            print("\n" * 20)
            calculator() 

calculator()            
