from rps import your_choice
from rps import computer_choice
from rps import check_win
from rps import clear
from rps import final_win_check
from rps import game_display

# LETS START

# CONTROL VARIABLE
playing = False

# ROUNDS
round = 0

# SCORE 
your_score = 0
computer_score = 0

# PLAY OR NOT
print("WELCOME TO THE GAME")
play_or_not = input("DO YOU WANT TO PLAY: y/n  ")
if play_or_not[0].lower() == 'y':
    playing = True
elif play_or_not[0].lower() == 'n':
    print("THANKS")
    exit()

# GAME LOGIC
# WHILE LOOP
while playing:
    yc = your_choice()
    cc = computer_choice()
    res = check_win(yc,cc)
    if res == 'win':
        your_score += 1
    elif res == 'lose':
        computer_score += 1
    else:
        pass

    round += 1
    
    game_display(yc,cc,res,your_score,computer_score,round)

    if round == 10:
        playing = False

final_res = final_win_check(your_score,computer_score)
clear()
if final_res == 'win':
    print("CONGRATULATIONS! YOU WON")
elif final_res == 'lose':
    print("NOOB! YOU LOSE")
else:
    print("LOL TIE")










