import random
data = ['ROCK','PAPER','SCISSOR']
userChoice = input('---DO YOU WANT TO PLAY[y/n]---\t->')
while userChoice == 'y':
    userInput = input("---ENTER YOUR CHOICE---\t->").upper()
    if userInput in data:
        botChoice = random.choice(data)
        print("Bot choice : ",botChoice)
        if userInput == botChoice:
            print('\t\t\t---DRAW---')
        else: 
            if userInput == data[0]:
                if botChoice == data[1]:
                    print('\t\t\t---BOT WON---')
                else:
                    print('\t\t\t---YOU WON---')
            elif userInput == data[1]:
                if botChoice == data[0]:
                    print('\t\t\t---YOU WON---')
                else:
                    print('\t\t\t---BOT WON---')
            else:
                if botChoice == data[0]:
                    print('\t\t\t---BOT WON---')
                else:
                    print('\t\t\t---YOU WON---')
    else:
        print('\t\t\t---ENTER VALID CHOICE---')
    userChoice = input('---DO YOU WANT TO CONTINUE[y/n]---\t->')