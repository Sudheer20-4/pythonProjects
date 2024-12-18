import random

print('\t\t\t---PASSWORD GENERATOR---\n\n\n')

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['~','!','@','#','$','%','^','&','*','(',')','_','-','+']

passwordList = []
l=int(input('How many letters you require?\t'))
n=int(input('How many numbers you require?\t'))
s=int(input('How many symbols you require?\t'))

for i in range(l):
    char = random.choice(letters)
    passwordList += char
for i in range(n):
    char = random.choice(numbers)
    passwordList += char
for i in range(s):
    char = random.choice(symbols)
    passwordList += char

random.shuffle(passwordList)
password = ''.join(passwordList)
print('YOUR PASSWORD IS --\t >',password)