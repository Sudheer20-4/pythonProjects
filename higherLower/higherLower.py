import random
import higherLowerInput
import logos
import os

def info(compare):
    name = compare['name'].upper()
    hero = compare['hero']
    year = compare['year']
    return f"{name} of {hero} in the year {year}"

def checkGuess(imdb1,imdb2,guess):
    if imdb1>imdb2:
        if guess == 1:
            return True
        else:
            return False
    else:
        if guess == 2:
            return True
        else:
            return False

score = 0
end = False

compare1 = random.choice(higherLowerInput.data)
while not end:
    compare2 = random.choice(higherLowerInput.data)
    while compare1 == compare2:
        compare2 = random.choice(higherLowerInput.data)    

    print(f"compare1\t--> {info(compare1)}")
    print(logos.versus)
    print(f"compare2\t--> {info(compare2)}")

    guess = int(input("\nwhich movie has high imdb [1 or 2]\t--> "))
    imdb1 = compare1['imdb']
    imdb2 = compare2['imdb']

    result = checkGuess(imdb1,imdb2,guess)

    os.system('cls')
    if result:
        score+=1
        print("\nYour Guess is Right!! Score --> ",score)
        compare1 = compare2
    else:
        print('\n\nYour Guess is Wrong!! Score --> ',score)
        end = True
