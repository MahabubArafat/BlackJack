"""
Black jack Black jack
"""
game = True
hitter = 0
com_game = True


def deck_creation():
    """
    it creates deck
    :return:
    """
    marks = ('diamond', 'spades', 'heart', 'club')
    numbers = ('ace', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine', 'ten', 'king', 'queen', 'jack')
    values = {'ace': 11, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
              'ten': 10, 'king': 10, 'queen': 10, 'jack': 10}
    card_deck = []

    for mark in marks:
        for num in numbers:
            card_deck.append([mark, num, values[num]])

    return card_deck


def printing_card(num):
    """
    prints the card for us
    """
    # print(deck[num])
    print('-----------------')
    print(f'|\t{deck[num][0]}\t|')
    print(f'|\t{deck[num][1]} \t|')
    print(f'|\t{deck[num][2]}\t|')
    print('-----------------')


def shuffling():
    """
    shuffles the created deck
    :return:
    """
    import random
    random.shuffle(deck)


non_repeat = []


def num_creator():
    """
    creates a random number
    :return:
    """
    import random
    number = random.randint(0, 51)
    if number not in non_repeat:
        non_repeat.append(number)
    return non_repeat


def hit_stay(card_value):
    """
    Human chooses to hit or stay
    :param card_value:
    :return:
    """
    global hitter, game, com_game, human_card_value
    hitter = 4
    while True:
        print("\r To hit type :y To stay type :n ", end=" ")
        response = input()
        if response.lower() == 'y':
            # num_creator()
            printing_card(non_repeat[hitter])
            card_value = card_value + deck[non_repeat[hitter]][2]
            human_card_value = card_value  # returning the human_card_value
            if card_value > 21:
                print(card_value)
                print("Busted com won")
                hitter += 1
                game = False
                com_game = False
                break
            elif card_value == 21:
                print(card_value)
                print("Computer\'s turn to hit")
                hitter += 1
                break
            elif card_value < 21:
                print(card_value)
                hitter += 1
                continue
        else:
            print("so you are staying and Now Computer's turn")
            break


while game:
    deck = deck_creation()
    shuffling()
    for i in range(20):
        num_creator()
    # num_creator()
    # num_creator()
    # num_creator()
    # num_creator()
    print("Com Dealer's cards:")
    printing_card(non_repeat[1])
    printing_card(non_repeat[3])
    com_card_value = deck[non_repeat[1]][2] + deck[non_repeat[3]][2]
    print(f"Com Card Value : {com_card_value}")
    print("Human player cars:")
    printing_card(non_repeat[0])
    printing_card(non_repeat[2])
    human_card_value = deck[non_repeat[0]][2] + deck[non_repeat[2]][2]
    print(f'Human card value :{human_card_value}')
    if human_card_value == 21:  # here i need to change a thing when com will not show his cards
        if human_card_value == com_card_value == 21:
            print("both hitted black jack,so draw")
            game = False
        else:
            print("Human has won the game")
            game = False
    else:
        hit_stay(human_card_value)
    if com_card_value == 21 and com_card_value >= human_card_value:
        print("black  jack, com won")
        game = False
        continue

    while com_game:
        if com_card_value <= 21 and human_card_value < com_card_value:
            print("com Won")
            game = False
            break
        elif com_card_value < 21:
            # num_creator()
            printing_card(non_repeat[hitter])
            com_card_value = com_card_value + deck[non_repeat[hitter]][2]
            print(com_card_value)
            hitter += 1
            continue
        elif com_card_value > 21 and human_card_value <= 21:
            print("com busted")
            print("Human player won")
            game = False
            break
