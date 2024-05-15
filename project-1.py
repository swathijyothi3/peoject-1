print('welcome to rps')
your_score = 0
cpu_score = 0
while True:
    user_choice = input('rock,paper and scissor?').lower()
    while user_choice!= 'rock' and user_choice!='paper'and user_choice!='scissor':
        user_choice= input('inavalid input, please try again:').lower()
    
    
    choices = ('rock','paper','scissor')
    import random
    computer_choice = random.choice(choices)
    print()
    print('your choice is',user_choice)
    print("computer's choice is",computer_choice)
    print()
    if user_choice == 'rock':
        if computer_choice == 'rock':
                print('its a tie')
        elif computer_choice == 'paper':
                print('you lost')
                cpu_score+=1
        elif computer_choice =='scissor':
                print('you win')
                your_score+=1
    elif user_choice =='paper':
        if computer_choice =='paper':
                print('its a tie')
        elif computer_choice =='rock':
                print('you win')
                your_score+=1
        elif computer_choice == 'scissor':
                print('you lost')
                cpu_score+=1
    elif user_choice == 'scissor':
        if computer_choice == 'scissor':
                print('its a tie')
        elif computer_choice == 'rock':
                print('you lost')
                cpu_score+=1
        elif computer_choice == 'paper':
                print('you win')
                your_score+=1
    print('your_score',your_score)
    print('computer_score',cpu_score)
    print()
    repeat = input("play again?: (Y/N):").lower()
    while repeat != 'n' and repeat != 'y':
            repeat = input('invalid input! try again!').lower()
    if repeat == 'n':
                print ('thank you')
                break
    print('\n------------\n')
