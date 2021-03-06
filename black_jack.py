"""
Black jack Black jack
"""
game = True
hitter = 0
com_game = main_game = True
winner: str = ' '
bet = 201


class Bet():
    def __init__(self, com_bankroll=10000000, human_bankroll=200, winner=' '):
        self.human_bankroll = human_bankroll
        self.com_bankroll = com_bankroll
        self.winner = winner

    def place_bet(self):
        global bet
        while True:
            try:
                print("\r>>>>>>>>>>>> how much bet you want to place :", end=" ")
                bet = int(input())
                if bet <= self.human_bankroll:
                    break
                else:
                    print("place a lower bet: ")
                    continue
            except:
                print(">>Enter The Amount of money you want to place as bet: ")
                continue

    def selecting_winner(self, winner):
        print(f"the bet is {bet}")
        try:
            if winner == 'com':
                self.human_bankroll = self.human_bankroll - bet
                print(f"money left : ${self.human_bankroll}")
            elif winner == 'human':
                self.human_bankroll = self.human_bankroll + (2 * bet)
                print(f"new balance : ${self.human_bankroll}")
        except:
            print("no clear winner,play again and bet, bank roll is the same")

    def bankroll_check(self):
        global main_game
        if self.human_bankroll <= 0:
            print("You can't Play anymore, You loose")
            print("Game Finished, Exiting Now")
            main_game = False
            # return main_game

    def __str__(self):
        return "your balance is : $"+str(self.human_bankroll)


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
    print(">Deck Created")
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
    try:
        print(">>shuffling cards..............")
        print(">>>card shuffled")
        random.shuffle(deck)
    except:
        print("restart the game")


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
    global hitter, game, com_game, human_card_value, winner
    hitter = 4
    while True:
        try:
            print("\r To hit type :y To stay type :n ", end=" ")
            response = input()
            if response.lower() == 'y':
                printing_card(non_repeat[hitter])
                if deck[non_repeat[hitter]][1] == 'ace':
                    print(
                        "\rYou have an ace, Enter \"y\" to make it 1 or \"n\" to let it be 11 :", end=" ")
                    ace_decider = input()
                    if ace_decider.lower() == 'y':
                        deck[non_repeat[hitter]][2] = 1
                    else:
                        pass
                card_value = card_value + deck[non_repeat[hitter]][2]
                human_card_value = card_value  # returning the human_card_value
                if card_value > 21:
                    print(f"Human card value : {card_value}")
                    print("Busted com won")
                    winner = 'com'
                    hitter += 1
                    game = False
                    com_game = False
                    break
                elif card_value == 21:
                    print(card_value)
                    print(f"Human card value : {card_value}")
                    hitter += 1
                    break
                elif card_value < 21:
                    print(f"Human card value : {card_value}")
                    hitter += 1
                    continue
            elif response.lower() == 'n':
                print("so you are staying and Now Computer's turn")
                break
        except:
            continue


lets_bet = Bet()
while main_game:
    while game:
        deck = deck_creation()
        shuffling()
        print(lets_bet)
        lets_bet.place_bet()
        for i in range(20):
            num_creator()
        print("Com Dealer's cards:")
        printing_card(non_repeat[1])
        # printing com card face down
        print('-----------------')
        print('|\t  \t|')
        print('|\t  \t|')
        print('|\t  \t|')
        print('-----------------')

        # not printing two cards but still counting the values to determine black jack, com card value and card will be revealed later
        com_card_value = deck[non_repeat[1]][2] + deck[non_repeat[3]][2]
        print("Human player cards:")
        printing_card(non_repeat[0])
        printing_card(non_repeat[2])
        human_card_value = deck[non_repeat[0]][2] + deck[non_repeat[2]][2]
        print(f'Human card value :{human_card_value}')
        if human_card_value == 21:  # here i need to change a thing when com will not show his cards #did the change
            if human_card_value == com_card_value == 21:
                print("both hit black jack,so draw")
                # when matter comes to decide black jack com card value will be revealed
                printing_card(non_repeat[1])
                printing_card(non_repeat[3])
                print(f"Com Card Value : {com_card_value}")
                game = False
                com_game = False
            else:
                print("Human has won the game")
                winner = 'human'
                com_game = False
                game = False
        else:
            hit_stay(human_card_value)
            print("Revealing com cards........................................")
            printing_card(non_repeat[1])
            printing_card(non_repeat[3])
            print(f"Com Card Value : {com_card_value}")
        if com_card_value == 21 and com_card_value >= human_card_value:
            print("black  jack, com won")
            winner = 'com'
            game = False
            continue

        while com_game:
            if com_card_value <= 21 and human_card_value < com_card_value:
                print("com Won")
                winner = 'com'
                game = False
                break
            elif com_card_value < 21:
                print(
                    "Now com will hit:.................................................")
                printing_card(non_repeat[hitter])
                com_card_value = com_card_value + deck[non_repeat[hitter]][2]
                print(f"Com card Value: {com_card_value}")
                hitter += 1
                continue
            elif com_card_value > 21 and human_card_value <= 21:
                print("com busted")
                print("Human player won")
                winner = 'human'
                game = False
                break
            elif com_card_value == human_card_value == 21:
                print("game drawed, Bank balance will be same")
                game = False
                break

    lets_bet.selecting_winner(winner)
    lets_bet.bankroll_check()
    if main_game == True:
        print("\r                  Wana play again ? type \"y\" to play again and type \"n\" to exit:", end=" ")
        response = input()
        if response.lower() == 'y':
            com_game = True
            game = True
            continue
        elif response.lower() == 'n':
            break
        else:
            print("No clear response you moron, exiting the game..........")
            break
    else:
        break
