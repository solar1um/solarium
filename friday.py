import random
#data
inp = ''
a = 'rock'
b = 'scissors'
c = 'paper'
pc_score = []
user_score = []
lst = [a, b, c]

#functions:

def winner():
    if len(pc_score) > len(user_score):
        print('comp won')
    elif len(pc_score) < len(user_score):
        print('user won')
    else:
        print('tie')
    return winner



def func(usr, pc):
    if usr == 'rock' and pc == 'scissors':
        user_score.append('win')
    elif usr == 'rock' and pc == 'paper':
        pc_score.append('win')
    elif usr == 'scissors' and pc == 'rock':
        pc_score.append('win')
    elif usr == 'scissors' and pc == 'paper':
        user_score.append('win')
    elif usr == 'paper' and pc == 'scissors':
        pc_score.append('win')
    elif usr == 'paper' and pc == 'rock':
        user_score.append('win')

    print(f'comp chose {pc_choice}')
    print(f'user {len(user_score)}:{len(pc_score)} comp')

#main logic

while (inp != 'finish' ):
    pc_choice = random.choice(lst)
    inp = input('\n')
    if inp == 'finish':
        print(f'final score is  {len(user_score)}:{len(pc_score)}')
        if len(pc_score) > len(user_score):
            print('pc won')
        elif len(pc_score) < len(user_score):
            print('user won')
        else:
            print('tie')
    else:
        func(inp.lower().strip(), pc_choice)
