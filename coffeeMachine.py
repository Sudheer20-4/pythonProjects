import logos

print(logos.coffee)
menu = {
    'latte' : {
        'ingredients' : {
            'water' : 200,
            'milk'  : 150,
            'coffee': 24
        },
        'cost' : 150
    },
    'espresso' : {
        'ingredients' : {
            'water' : 50,
            'coffee': 18
        },
        'cost' : 100
    },
    'cappuccino' : {
        'ingredients' : {
            'water' : 250,
            'milk'  : 100,
            'coffee': 24
        },
        'cost' : 200
    }
}
resource = {
    'water' : 1000,
    'milk'  : 500,
    'coffee': 200
}
income = 0

def checkResource(ingredients):
    for item in ingredients:
        if ingredients[item] > resource[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True

def payment():
    print("!!Please insert the coins!!")
    total = 0
    coins20 = int(input("Enter no of Rs 20 coins --> "))
    coins10 = int(input("Enter no of Rs 10 coins --> "))
    coins5 = int(input("Enter no of Rs 5 coins --> "))
    total = 20*coins20 + 10*coins10 + 5*coins5
    return total

def paymentSuccessful(money,cost):
    if money>=cost:
        global income
        income+=cost
        change = money-cost
        print('Here is your change Rs',change)
        return True
    else:
        print('Sorry Please provide sufficient money!!')
        return False

def makeCoffee(choice,ingredients):
    for item in ingredients:
        resource[item] -= ingredients[item]
    print(f"Here is your {choice} Coffee --")

on = True

while on :
    userInput = input('What do you want? [latte/espresso/cappuccino] -->')
    if userInput == 'off':
        on = False
    elif userInput == 'report':
        print(f'Water = {resource["water"]}ml')
        print(f'Milk = {resource["milk"]}ml')
        print(f'Coffee = {resource["coffee"]}g')
        print(f'Money = Rs {income}')
    else:
        coffee = menu[userInput]
        if checkResource(coffee['ingredients']):
            amount = payment()
            if paymentSuccessful(amount,coffee['cost']):
                makeCoffee(userInput,coffee['ingredients'])