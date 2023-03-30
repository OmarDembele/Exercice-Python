import random
print('Game of rock, paper, scissor')
player1=input('choisir entre les troix: ')
player2=random.choice(['rock', 'paper','scissor'])
print("player 2 selected: ",player2)
while player1 == player2:
    print("Tie")
    player1=input('select beetween this three : ')
    
if player1 == "rock" and player2 == "paper":
    print("Player 2 Won")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 Won")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 Won")
else:
    print("Player 1 Won")