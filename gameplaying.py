import gameoverv2
from boardmechanics import board2

def playgame():
    global placeholdstatement
    gameover = False
    playerturn = True
    placeholdstatement = False
    while gameover == False:
        if playerturn==True:
            boardx('x')
            playerturn=False
            if gameoverv2.fullboard2(y)==True:
                print("THE GAME IS OVER \n        DRAW!!!")
                gameover=True
            elif gameoverv2.gameover(y)==True:
                print("THE GAME IS OVER \n        X WINS")
                gameover = True
        elif playerturn==False:
            boardx('o')
            playerturn=True    
            if gameoverv2.fullboard2(y)==True:
                print("THE GAME IS OVER \n        DRAW!!!")
                gameover=True
            elif gameoverv2.gameover(y)==True:
                print("THE GAME IS OVER \n        O WINS")
                gameover = True

#This is another makeshift bit of code that only makes sense when used in the command line... 
playagain = True
while playagain==True:
    playgame()
    question = input("press enter to exit or type 'yes' to play again: ")
    if question != 'yes':
        playagain = False
    
