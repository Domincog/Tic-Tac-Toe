#This is a representation of the tic-tac-toe board. Each {} bracket is an interchangable variable, used for the X's and O's on the board.   
import gameoverv2
     
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
        board3 = board.format(y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8])
        print(board3)
        placeholdstatement = True
    loc = int(input("Choose your number: ")) - 1
    while gameoverv2.isplayed(y, loc) == True:
        print("You can't write over your opponents moves!")
        loc = int(input("Please choose another number: ")) - 1
    y[loc] = x
    board2 = board.format(y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8])
    print("\n" * 50) #This is a very makeshift way of clearing the screen, needs to be reimplemented later... Only works in terminal, so comment out as needed.
    print(board2)
    print(y)

