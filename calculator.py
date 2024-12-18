import os
import logos

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operators = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

def calculator():
    print(logos.calci)
    con = True
    num1 = float(input("Enter the number \t--> "))
    while con:
        op = input("Enter the operator\t--> ")
        num2 = float(input("Enter the number\t--> "))

        operation = operators[op]
        res = operation(num1,num2)

        print(f"{num1} {op} {num2} = {res}")

        tem = input("Do you want to continue [y] or [n] and wanna exit [x]\t--> ")
        if tem == 'y':
            num1=res
        elif tem =='n':
            os.system('cls')
            con = False
            calculator()
        else:
            con = False
            print("THE END")


calculator()