'''
This is my attempt at a tic-tac-toe implementation

Possible future implimentations:
    .State who won at the end of each game (DONE)
    .Ask if the players want to play again
    .Ask if player wants to play against computer (impliment tictactoe AI engine)
    .
'''

import gameoverv2

#This is a representation of the tic-tac-toe board. Each {} bracket is an interchangable variable, used for the X's and O's on the board.        
board = '''
 
      |     |     
   {}  |  {}  |   {}  
 _____|_____|_____
      |     |     
   {}  |  {}  |   {}  
 _____|_____|_____
      |     |     
   {}  |  {}  |   {} 
      |     |     
'''


#A second identical board (board2) is crated to so that board can be a 'blank slate' board that doesn't get manipulated.
board2 = board
# print(board2)

placeholdstatement = False #This is used later on to prevent all variables on the board from being reset every time boardx is called

print("\n" * 50) #this puts things on the bottom of the screen so it flows better with the next makeshift screen clearing funciton

print("GAME START")
#%%                 <---- This is used in the spyder program to dictate the 'cells'
def boardx(player):
    '''#This function outputs the board for gameplay'''
    #declaring something as 'global' means it can be maniuplated outside of this varible. 
    global placeholdstatement
    global y
    global board2
    x = str(player)
    print("It is " + player + "'s turn!")
    if placeholdstatement == False:
        y = [1,2,3,4,5,6,7,8,9]
        board2 = board2.format(y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8])
        print(board2)
        placeholdstatement = True
    loc = int(input("please type the number you want")) - 1 
    y[loc] = x
    board2 = board.format(y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8])
    print("\n" * 50) #This is a very makeshift way of clearing the screen, needs to be reimplemented later... Only works in terminal, so comment out as needed.
    print(board2)
    print(y)

gameover = False

playerturn = True
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
closeout = True
while closeout==True:
    endthescreen = input("press enter to close out: ")
    closeout=False
    