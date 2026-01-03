import random


cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

# 2 Cards For All Players At The Begining
def card_select():
    selected = random.sample(cards,2)
    for i in selected:
        cards.remove(i)
    return selected

dealer = card_select()
player = card_select()

#
while sum(player) < 21:
    print(f"Your Cards: {player}, and Your Total Points: {sum(player)}")
    print(f"Dealer First Card: {dealer[0]}")
    query = input("Do you want one card more?:(Yes/No) ")
    if query == "Yes":
        add_one = random.sample(cards,1)
        player = player + add_one
        cards.remove(add_one[0])
    else:
        print("Thank you for playing")
        break

while sum(dealer) <17:
    add_one = random.sample(cards,1)
    dealer = dealer + add_one
    cards.remove(add_one[0])

if sum(player) < sum(dealer):
    print("You won")
else:
    print("You lost")


