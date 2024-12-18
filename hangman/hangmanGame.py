import random
import hangmanStages as Stages
import hangmanWords as Words

chosenWord = random.choice(Words.words)
lives = 6
display = []
gameOver = False

#print(chosenWord)

for i in range(len(chosenWord)):
    display +='_'
print(display)
    
while not gameOver:
    guessedLetter = input('Guess a letter \t -->').lower()
    for i in range(len(chosenWord)):
        if chosenWord[i] == guessedLetter:
            display[i] = chosenWord[i]
    print(display)
    if guessedLetter not in chosenWord:
        lives-=1
        if lives == 0:
            gameOver = True
            print('You Lose')
            print('ANSWER IS \t--> ',chosenWord)
    if '_' not in display:
        gameOver = True
        print('You Win')
    print(Stages.stages[lives])
    print('\n\n')