import os

bidDetails = {}
flag = True

def bidWinner(bidData):
    maxBid = 0
    for bid in bidData:
        tem = bidData[bid]
        if tem > maxBid:
            maxBid = tem
            winner = bid
    print('The Bid Winner is\t--> ',winner)
    
while flag:
    name = input('Enter the bidder name\t--> ')
    value = int(input('Enter the bidValue\t--> '))
    bidDetails[name] = value
    con = input('Do you want to continue[y/n]\t--> ')
    if con=='n':
        bidWinner(bidDetails)
        print(bidDetails)
        flag = False
    elif con=='y':
        os.system('cls')