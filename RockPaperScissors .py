import random
choices=['r','p','s']
choice_meaining={
    'r':'Rock',
    'p':'Paper',
    's':'scissors'
}
user_score = 0
AI_score=0
i=0
while i<5:
    user_choice = input('select from Rock, Paper, Scissors:(r , p ,s)')
    ai_choice = random.choice(choices)
    if user_choice in choices:
        print(f'your choices is {choice_meaining[user_choice]}. AI choice is {choice_meaining[ai_choice]}.')
        if user_choice == AI_score:
            print('Tie')
        elif user_choice == 'r' and AI_score == 's':
            user_score+=1
            print('user + 1!')
        elif user_choice == 'p' and ai_choice == 'r':
            user_score+=1
            print('user + 1!')
        elif user_choice == 's' and ai_choice == 'p':
            print('user + 1!')
            user_score+=1
        else:
            print('ai + 1!')
            AI_score+=1
    else:
        print('invalid')
        i-=1
    print(f'user_score: {user_score} / ai_score: {AI_score}')
    print('_'*15,) 
    i+=1
if user_score > AI_score:  
    print (f'user won with score: {user_score}')    
elif user_score < AI_score:
    print(f'ai won with score: {AI_score}')
else:
    print(f'It\'s a Tie. score:{user_score}')
    
