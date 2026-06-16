import random

Cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


random.shuffle(Cards)


p1 = [Cards.pop(), Cards.pop()]
p2 = [Cards.pop(), Cards.pop()]

print("Player 1:", p1)
print("Player 2:", "*" ,p2[1])
a=0
b=0
def p1():
    if b==1:
        return
    else:
        action = input("Player 1, do you want to hit or stay? (h/s): ")
        if action.lower() == 'h':
            p1.append(Cards.pop())
            print("Player 1 draws a card:", p1[-1])
            a=0
            
        else:
            print("Player 1 stays with total:", p1_total)
        a=1

def p2():
    if a==1:
        if p2_total < 17:
            p2.append(Cards.pop())
            print("Player 2 draws a card:", p2[-1])
            return
        else:
            print("Player 2 stays with total:", p2_total)
            b=1
            return
    elif p2_total <= 17:
        p2.append(Cards.pop())
        print("Player 2 draws a card:", p2[-1])
        return
    else:
        print("Player 2 stays with total:", p2_total)
        return

while True:
    p1_total = sum(p1)
    p2_total = sum(p2)

    if p1_total > 21:
        print("Player 1 busts! Player 2 wins!")
        break
    elif p2_total > 21:
        print("Player 2 busts! Player 1 wins!")
        break

    if p1_total == 21:
        print("Player 1 has Blackjack! Player 1 wins!")
        break
    elif p2_total == 21:
        print("Player 2 has Blackjack! Player 2 wins!")
        break

    p2()


    if action.lower() == 's' and action.lower() == 's':
        if p1_total > p2_total:
            print("Player 1 wins with total:", p1_total)
        elif p2_total > p1_total:
            print("Player 2 wins with total:", p2_total)
        else:
            print("It's a tie!")
        break
