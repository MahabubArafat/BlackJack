'''
Black jack Black jack
'''
def deck_creation():
    marks = ('diamond', 'spades', 'heart', 'club')
    nums = ('ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'king', 'queen', 'jack')
    values = {'ace': 11, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
              'ten': 10, 'king': 10, 'queen': 10, 'jack': 10}
    deck = []

    for mark in marks:
        for num in nums:
            deck.append([mark, num, values[num]])

    return deck

def printing_card(num):
    # print(deck[num])
    print('-------------')
    print(f'|\t{deck[num][0]}\t|')
    print(f'|\t{deck[num][1]} \t|')
    print(f'|\t{deck[num][2]}\t\t|')
    print('-------------')

def shuffling():
    import random
    random.shuffle(deck)

non_repeat=[]
def num_creator():
    import random
    number=random.randint(0,51)
    if number not in non_repeat:
        non_repeat.append(number)
    return non_repeat

deck=deck_creation()
shuffling()
num_creator()
num_creator()
num_creator()
num_creator()
print("Com Dealer's cards:")
printing_card(non_repeat[1])
printing_card(non_repeat[3])
com_card_value=deck[non_repeat[1] ][2] + deck[non_repeat[3] ][2]
print(f'Com Card Value : {com_card_value}')
print("Human player cars:")
printing_card(non_repeat[0])
printing_card(non_repeat[2])
human_card_value=deck[non_repeat[0] ][2] + deck[non_repeat[2] ][2]
print(f'Human card value :{human_card_value}')
# if card_value==21:
#     print("congratulations you have hit the black jack")
#     continue#jokhon while loop e dimu

def hit_stay(card_value):
    global hitter
    hitter=4
    while True:
        print("\r To hit type :y To stay type :n ",end=" ")
        response=input()
        if response.lower()=='y':
            num_creator()
            printing_card(non_repeat[hitter])
            card_value=card_value+deck[non_repeat[hitter]][2]
            if card_value>21:
                print(card_value)
                print("Busted")
                hitter += 1  # noyle same card dui bar hit hobe
                break
            elif card_value==21:
                print(card_value)
                print("com's turn to hit")
                hitter += 1  # noyle same card dui bar hit hobe
                break
            elif card_value<21:
                print(card_value)
                hitter += 1  # noyle same card dui bar hit hobe
                continue
        else:
            print("so you are staying and Now Com's turn")
            hitter += 1  # noyle same card dui bar hit hobe
            break


hit_stay(human_card_value)

while True:
    if com_card_value==21:
        print("black  jack, com won")
        break
    elif com_card_value<21:
        num_creator()
        printing_card(non_repeat[hitter-1])
        com_card_value=com_card_value+deck[non_repeat[hitter-1]][2]
        print(com_card_value)
        hitter+=1
        continue
    elif com_card_value>21:
        print("com busted")
        break
