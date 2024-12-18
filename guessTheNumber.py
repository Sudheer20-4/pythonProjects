import random
import logos

def checkNum(bot,user,attempts):
    if user > bot:
        print("Too high")
        return attempts-1
    elif user < bot:
        print("Too low")
        return attempts-1
    else:
        print("Your Guess was right")
        return

print(logos.guess)

level = input("select a level [easy/hard]\t--> ").lower()
print("\n<---Let me guess a number--->")
if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5
else:
    print("select a valid level")
botGuess = random.randint(1,50)

while True:
    userGuess = int(input("\nGuess a number\t--> "))
    attempts= checkNum(botGuess,userGuess,attempts)
    if attempts == 0:
        print("You have ran out off attempts")
        print("The number is ",botGuess)
        break
    elif attempts == None:
        break
    print(f"You have {attempts} attempts remaining")