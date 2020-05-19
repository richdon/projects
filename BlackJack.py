# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:00:48 2019

@author: richa
"""
import random
#where the dealer's cards will be stored
dealerHand = []

#where the player's cards will be stored
playerHand = []

#The dealer's cards are inserted into the list 'dealerHand'
while len(dealerHand) < 2:
    dealerHand.append(random.randint(1,11))
    if len(dealerHand) == 2:
        print("Dealer has: X &", dealerHand[0])
        
#The player's cards are inserted into the list 'playerHand'
while len(playerHand) < 2:
    playerHand.append(random.randint(1,11))
    if len(playerHand) == 2:
        print("Your cards are: ", playerHand)
    


playerTotal = sum(playerHand)
#dealerTotal = sum(dealerHand)

print("player total: ", playerTotal)

choice = input(str("would you like to HIT(h) or STAY(s)?: "))

if choice =='s' and playerTotal == 21:
    print('Blackjack! you have 21')
elif choice == 's' and playerTotal < 21:
    print('You have: ', playerTotal)

while choice == 'h' and playerTotal < 21:
    playerHand.append(random.randint(1,11))
    playerTotal = sum(playerHand)
    print('you have:',playerTotal)
    if playerTotal > 21:
        print("Bust",playerTotal)
    elif playerTotal < 21:
        choice = input(str("would you like to HIT(h) or STAY(s)?: "))
        if choice =='s':
            print('you have: ', playerTotal)
    elif playerTotal == 21:
        print(playerTotal,' blackjack! you win')
        
if sum(dealerHand) < playerTotal and playerTotal < 22:
    print('You win! you have: ', playerTotal, 'dealer has: ', sum(dealerHand))

elif sum(dealerHand) > playerTotal and sum(dealerHand)<22:
    print('dealer wins', sum(dealerHand))            
    
elif sum(dealerHand) == playerTotal:
    print('dealer has: ',sum(dealerHand), 'dealer wins the tie')
             




while choice == 'h' and sum(dealerHand) < 17:
    dealerHand.append(random.randint(1,11))
    if sum(dealerHand) == 21:
        print('dealer has blackjack you lose')
    elif sum(dealerHand)>21:
        print('dealer has bust')

