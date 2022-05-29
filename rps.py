import random
import os
# your_choice
def your_choice():
    choice = input('Your choice: ')
    return choice

# computer_choice
def computer_choice():
    choice_dict = {'1':"rock",'2':"paper",'3':"scissor"}
    choice = random.randint(1,3)
    return choice_dict[str(choice)]

# check_win
def check_win(your_choice,computer_choice):
    win_condition = {'rock':'scissor','paper':'rock','scissor':'paper'}
    lose_condition = {'scissor':'rock','rock':'paper','paper':'scissor'}
    # check tie
    res = ''
    if your_choice == computer_choice:
        res = "Tie"
    else:

    # check win or lose
        if win_condition[your_choice] == computer_choice:
            res =  "win"
        elif  lose_condition[your_choice] == computer_choice:
            res +=  "lose"

    return res

# clear screen
def clear():
    os.system('cls')

# final win check
def final_win_check(your_score,computer_score):
    if your_score > computer_score:
        res = 'win'
    elif computer_score > your_score:
        res= 'lose'
    else:
        res = 'tie'
    
    return res

# display func
def game_display(your_choice,computer_choice,check_win,your_score,computer_score,round):

    print(f"         ROUND: {round}          ")
    print(f"\nYOU CHOSE: {your_choice}      ")
    print(f"\nCOMPUTER CHOSE: {computer_choice}")
    print(f"\n\nRESULT: {check_win}         ")
    print(f"\nYOUR SCORE:{your_score} \nCOMPUTER SCORE:{computer_score}")





    




