from random import shuffle
from time import sleep

play_again = "да"
balance = 100


while play_again == "да":

    koloda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4
    shuffle(koloda)
    your_points = 0
    dealer_points = 0
    min_dealer_points = 17
    move = 1
    choice = 'да'
    bet = input("Введите ставку ")

    while choice == "да":
       
        if move == 1:
            dealer_card = koloda.pop()
            dealer_points += dealer_card

            cards = []
            for i in range(2):
                your_card = koloda.pop()
                your_points += your_card
                cards.append(your_card)
        else:
            your_card = koloda.pop()
            your_points += your_card

        print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
        if move == 1:
            print(f"    Вам выпали карты номиналом {cards[0]} и {cards[1]}")
        else:
            print(f"Вам выпала карта номиналом {your_card}")

        if your_points > 21:
            print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
            print("Вы проиграли")
            balance-=bet
            print(f"Ваш баланс: {balance}$")
            break

        elif your_points == 21:
            choice = "нет"
        else:
            choice = input("Ещё? (да/нет)\n")
            while choice not in ["да", "нет"]:
                choice  = input("Введи да или нет\n")

        move+=1
        
    else:
        while dealer_points <= 17:
            dealer_card = koloda.pop()
            dealer_points += dealer_card
            print(f"Крупье вытянул карту номиналом {dealer_card}")
            sleep(2)

        if your_points == dealer_points:
            print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
            print("Ничья")
            print(f"Ваш баланс: {balance}$")
        elif dealer_points > 21:
            print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
            print("Вы выиграли")
            balance+=bet
            print(f"Ваш баланс: {balance}$")
        else:
            if your_points > dealer_points:
                print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
                print("Вы выиграли")
                balance+=bet
                print(f"Ваш баланс: {balance}$")
            else:
                print(f"""
        =============
        ОЧКИ:
        Крупье: {dealer_points}
        Вы: {your_points}
        =============    
            """)
                print("Вы проиграли")
                balance-=bet
                print(f"Ваш баланс: {balance}$")
    play_again = input("Сыграем еще? Да/нет\n")