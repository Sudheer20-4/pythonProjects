data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plainText,key):
    cipher = ''
    for i in range(len(plainText)):
        if plainText[i] in data:
            cipher+=data[(data.index(plainText[i])+key)%26]
        else:
            cipher+=plainText[i]
    print("Encrypted Text\t--> ",cipher)

def decryption(cipherText,key):
    plainText = ''
    for i in range(len(cipherText)):
        if cipherText[i] in data:
            plainText+=data[(data.index(cipherText[i])-key)%26]
        else:
            plainText+=cipherText[i]
    print("Decrypted Text\t--> ",plainText)

userChoice = input("Do you want to encrypt or decrypt\t--> ").lower()
userInput = input("Enter the text\t--> ").lower()
key = int(input("Enter the key\t--> "))
con = True

while con:
    if userChoice == 'encrypt':
        encryption(userInput,key)
    elif userChoice == 'decrypt':
        decryption(userInput,key)
    else:
        print("Enter a valid  option !!!")
    opt = input("Wanna Stay [y/n]\t--> ")
    if opt == 'n':
        con = False
        print('Good Bye!!!')
    else:
        userChoice = input("Do you want to encrypt or decrypt\t--> ").lower()       
        userInput = input("Enter the text\t--> ")
        key = int(input("Enter the key\t--> "))