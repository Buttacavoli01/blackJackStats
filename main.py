import random

def create_standard_deck():
    #list that holds the suits
    suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
    # dictionary to hold the values of a deck
    place_holders = {
        "A": 1,
        2 : 2,
        3:3,
        4:4,
        5:5,
        6:6,
        7:7,
        8:8,
        9:9,
        10:10,
        'J':10,
        "Q": 10,
        'K': 10}

    standard_deck = {}
    #creating a card with each suit and creating a typical deck of cards
    for i in suits:
        for j, k in place_holders.items():
            str = f'{j}{i}'
            standard_deck[str] = k
    return standard_deck


def create_game_deck(num):
    game_deck = []
    deck = create_standard_deck()

    # for loop allows each card to be added "num" amount of times
    for i in deck.keys():
        game_deck += num * [i]
    random.shuffle(game_deck)
    print(len(game_deck))




if __name__ == '__main__':
    create_standard_deck()
    create_game_deck(3)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
