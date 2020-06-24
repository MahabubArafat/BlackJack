import random

marks=('diamond','spades','heart','club')
nums=('ace','two','three','four','five','six','seven','eight','nine','ten','king','queen','jack')
values={'ace':10,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'king':10,'queen':10,'jack':10}

def card(marks,nums,values):
    mark=random.choice(marks)
    num=random.choice(nums)
    value=values[num]
    print('-------------')
    print(f'|\t{mark}\t|')
    print(f'|\t{num} \t|')
    print(f'|\t{value}\t\t|')
    print('-------------')

for i in range(10):
    card(marks,nums,values)