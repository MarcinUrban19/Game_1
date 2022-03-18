import random
from random import randint
tools = ["rock","paper","scissors"]
results = {("paper", "scissors"): "scissors",
           ("paper", "rock"): "paper",
           ("rock","scissors"): "rock"

}
game = True
user_wins = 0
comp_wins = 0
draws = 0
while game == True:

    user_choice = input('Choose one! rock, paper or scissors: ')
    user_choice.lower()
    while user_choice not in tools:
    #     raise Exception("Unknown tool")
        print('Unknown tool')
        user_choice = input('Choose one! rock, paper or scissors: ')
        user_choice.lower()

    comp_choice =random.choice(tools)
    print('Computer choice: ',comp_choice)

    if user_choice == comp_choice:
        print("Draw")
        draws =+ 1
    else:
       for result in results:
           if user_choice in result and comp_choice in result:
                winner = results[result]
                if user_choice  == winner:
                    print('You win!!')
                    user_wins += 1
                else:
                    print('Computer win!!')
                    comp_wins =+ 1
                break
    decision = input('Do you want to play again? yes/no')
    decision.lower()
    if decision != 'yes':
        game = False
print('Thanks for your game!')
print('You wins: ', user_wins)
print('Computer wins: ',comp_wins)
if draws > 0 :
    print('Draws: ', draws)