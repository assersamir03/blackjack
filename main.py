# blackjack
import random

cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack():
    dealersCard = []
    dealersCard.append(random.choice(cards))
    dealersCard.append(random.choice(cards))

    playerCard = []
    playerCard.append(random.choice(cards))
    playerCard.append(random.choice(cards))

    print(f'ur cards are: {playerCard}')
    print(f"the dealers cards are: [?,{dealersCard[1]}]")


    userChoice = input('do u want to take ur chances or draw?y/n:').lower()

    if userChoice == 'y':
        playerCard.append(random.choice(cards))
        print(f'ur cards are: {playerCard} = {sum(playerCard)}')
        totalPlayer = sum(playerCard)
        if totalPlayer > 21:
            print(f'u exceeded the limit! so you lose')
        else:
            totalDealer = sum(dealersCard)
            print(f'the player cards are: {playerCard} = {totalPlayer}\nthe dealers cards are: {dealersCard} = {totalDealer}')
            if totalPlayer > totalDealer:
                print(f'you win')
            elif totalPlayer < totalDealer:
                print(f'you lose')
            else:
                print(f'its a tie')
    elif userChoice == 'n':
        totalPlayer = sum(playerCard)
        totalDealer = sum(dealersCard)
        print(f'the player cards are: {playerCard} = {totalPlayer}\nthe dealers cards are: {dealersCard} = {totalDealer}')
        if totalPlayer > totalDealer:
            print(f'you win')
        elif totalPlayer < totalDealer:
            print(f'you lose')
        else:
            print(f'its a tie')

    repeat =input("do you want to repeat y/n?").lower()
    if repeat == 'y':
        blackjack()
    if repeat == 'n':
        exit()
blackjack()