# importing the random module
import random

def seeHumanWins(Board):
    humanWins=False
    if ((Board[0]*Board[1]*Board[2])==27):
        humanWins=True
    elif ((Board[3]*Board[4]*Board[5])==27):
        humanWins=True
    elif ((Board[6]*Board[7]*Board[8])==27):
        humanWins=True
    elif ((Board[0]*Board[3]*Board[6])==27):
        humanWins=True
    elif ((Board[1]*Board[4]*Board[7])==27):
        humanWins=True
    elif ((Board[2]*Board[5]*Board[8])==27):
        humanWins=True
    elif ((Board[0]*Board[4]*Board[8])==27):
        humanWins=True
    elif ((Board[2]*Board[4]*Board[6])==27):
        humanWins=True   
    return humanWins

def goForWinMove(Board):
    moveGiven=True
    if ((Board[0]*Board[1]*Board[2])==50):
        if (Board[0]==2):
            Board[0]=5
        elif (Board[1]==2):
            Board[1]=5
        elif Board[2]==2:
            Board[2]=5
    elif ((Board[3]*Board[4]*Board[5])==50):
        if (Board[3]==2):
            Board[3]=5
        elif (Board[5]==2):
            Board[5]=5
    elif ((Board[6]*Board[7]*Board[8])==50):
        if (Board[6]==2):
            Board[6]=5
        elif (Board[7]==2):
            Board[7]=5
        elif Board[8]==2:
            Board[8]=5
    elif ((Board[0]*Board[3]*Board[6])==50):
        if (Board[0]==2):
            Board[0]=5
        elif (Board[3]==2):
            Board[3]=5
        elif Board[6]==2:
            Board[6]=5
    elif ((Board[1]*Board[4]*Board[7])==50):
        if (Board[1]==2):
            Board[1]=5
        elif (Board[7]==2):
            Board[7]=5
    elif ((Board[2]*Board[5]*Board[8])==50):
        if (Board[2]==2):
            Board[2]=5
        elif (Board[5]==2):
            Board[5]=5
        elif Board[8]==2:
            Board[8]=5
    elif ((Board[0]*Board[4]*Board[8])==50):
        if (Board[0]==2):
            Board[0]=5
        elif (Board[8]==2):
            Board[8]=5
    elif ((Board[2]*Board[4]*Board[6])==50):
        if (Board[2]==2):
            Board[2]=5
        elif (Board[6]==2):
            Board[6]=5
    else:
        moveGiven=False   
    return moveGiven

def defendWinMove(Board):
    moveGiven=True
    if ((Board[0]*Board[1]*Board[2])==18):
        if (Board[0]==2):
            Board[0]=5
        elif (Board[1]==2):
            Board[1]=5
        elif Board[2]==2:
            Board[2]=5
    elif ((Board[3]*Board[4]*Board[5])==18):
        if (Board[3]==2):
            Board[3]=5
        elif (Board[5]==2):
            Board[5]=5
    elif ((Board[6]*Board[7]*Board[8])==18):
        if (Board[6]==2):
            Board[6]=5
        elif (Board[7]==2):
            Board[7]=5
        elif Board[8]==2:
            Board[8]=5
    elif ((Board[0]*Board[3]*Board[6])==18):
        if (Board[0]==2):
            Board[0]=5
        elif (Board[3]==2):
            Board[3]=5
        elif Board[6]==2:
            Board[6]=5
    elif ((Board[1]*Board[4]*Board[7])==18):
        if (Board[1]==2):
            Board[1]=5
        elif (Board[7]==2):
            Board[7]=5
    elif ((Board[2]*Board[5]*Board[8])==18):
        if (Board[2]==2):
            Board[2]=5
        elif (Board[5]==2):
            Board[5]=5
        elif Board[8]==2:
            Board[8]=5
    elif ((Board[2]*Board[4]*Board[6])==18):
        if (Board[2]==2):
            Board[2]=5
        elif (Board[6]==2):
            Board[6]=5
    else:
        moveGiven=False   
    return moveGiven

def createWinMove(Board):
    moveGiven=True
    if ((Board[0]*Board[1]*Board[2])==20):
        if (Board[0]==2):
            Board[0]=5
        elif (Board[1]==2):
            Board[1]=5
        elif Board[2]==2:
            Board[2]=5
    elif ((Board[3]*Board[4]*Board[5])==20):
        if (Board[3]==2):
            Board[3]=5
        elif (Board[5]==2):
            Board[5]=5
    elif ((Board[6]*Board[7]*Board[8])==20):
        if (Board[6]==2):
            Board[6]=5
        elif (Board[7]==2):
            Board[7]=5
        elif Board[8]==2:
            Board[8]=5
    elif ((Board[0]*Board[3]*Board[6])==20):
        if (Board[0]==2):
            Board[0]=5
        elif (Board[3]==2):
            Board[3]=5
        elif Board[6]==2:
            Board[6]=5
    elif ((Board[1]*Board[4]*Board[7])==20):
        if (Board[1]==2):
            Board[1]=5
        elif (Board[7]==2):
            Board[7]=5
    elif ((Board[2]*Board[5]*Board[8])==20):
        if (Board[2]==2):
            Board[2]=5
        elif (Board[5]==2):
            Board[5]=5
        elif Board[8]==2:
            Board[8]=5
    elif ((Board[0]*Board[4]*Board[8])==20):
        if (Board[0]==2):
            Board[0]=5
        elif (Board[8]==2):
            Board[8]=5
    elif ((Board[2]*Board[4]*Board[6])==20):
        if (Board[2]==2):
            Board[2]=5
        elif (Board[6]==2):
            Board[6]=5
    else:
        moveGiven=False   
    return moveGiven

def checkDangerousMove(Board):
    moveGiven=True
    if ((Board[4]==3) and (Board[8]==3)):
        Board[2]=5
    elif ((Board[5]==3) and (Board[7]==3)):
        Board[8]=5
    else:
        moveGiven=False 
    return moveGiven

def createForkMove(Board):
    moveGiven=True
    if ((Board[4]==5) and (Board[0]==3)):
        Board[8]=5
    elif ((Board[4]==5) and (Board[2]==3)):
        Board[6]=5
    elif ((Board[4]==5) and (Board[6]==3)):
        Board[2]=5
    elif ((Board[4]==5) and (Board[8]==3)):
        Board[0]=5
    else:
        moveGiven=False 
    return moveGiven

def createForkWinMove(Board):
    forkBoard=[0,0,0,0,0,0,0,0,0]
    moveGiven=False

    if ((Board[0]*Board[1]*Board[2])==20):
        if (Board[0]==2):
            forkBoard[0]=forkBoard[0]+1
        elif (Board[1]==2):
            forkBoard[1]=forkBoard[1]+1
        elif Board[2]==2:
            forkBoard[2]=forkBoard[2]+1

    if ((Board[3]*Board[4]*Board[5])==20):
        if (Board[3]==2):
            forkBoard[3]=forkBoard[3]+1
        elif (Board[5]==2):
            forkBoard[5]=forkBoard[5]+1

    if ((Board[6]*Board[7]*Board[8])==20):
        if (Board[6]==2):
            forkBoard[6]=forkBoard[6]+1
        elif (Board[7]==2):
            forkBoard[7]=forkBoard[7]+1
        elif Board[8]==2:
            forkBoard[8]=forkBoard[8]+1

    if ((Board[0]*Board[3]*Board[6])==20):
        if (Board[0]==2):
            forkBoard[0]=forkBoard[0]+1
        elif (Board[3]==2):
            forkBoard[3]=forkBoard[3]+1
        elif Board[6]==2:
            forkBoard[6]=forkBoard[6]+1
            
    if ((Board[1]*Board[4]*Board[7])==20):
        if (Board[1]==2):
            forkBoard[1]=forkBoard[1]+1
        elif (Board[7]==2):
            forkBoard[7]=forkBoard[7]+1
            
    if ((Board[2]*Board[5]*Board[8])==20):
        if (Board[2]==2):
            forkBoard[2]=forkBoard[2]+1
        elif (Board[5]==2):
            forkBoard[5]=forkBoard[5]+1
        elif Board[8]==2:
            forkBoard[8]=forkBoard[8]+1

    if ((Board[0]*Board[4]*Board[8])==20):
        if (Board[0]==2):
            forkBoard[0]=forkBoard[0]+1
        elif (Board[8]==2):
            forkBoard[8]=forkBoard[8]+1

    if ((Board[2]*Board[4]*Board[6])==20):
        if (Board[2]==2):
            forkBoard[2]=forkBoard[2]+1
        elif (Board[6]==2):
            forkBoard[6]=forkBoard[6]+1

    for i in range(9):
        if (forkBoard[i]==2):
            Board[i]=5
            moveGiven=True
            break
     
    return moveGiven

def calculateMove(Board,Turn):
    if Turn==2:
        if Board[4]==2:
            Board[4]=5
        else:
            Board[0]=5
    elif Turn==3:
        if (not(createForkMove(Board))):
            if (not(createWinMove(Board))):
                if Board[1]==2:
                    Board[1]=5
                elif Board[3]==2:
                    Board[3]=5
                elif Board[5]==2:
                    Board[5]=5
                elif Board[7]==2:
                    Board[7]=5
    elif (Turn==4):
        if (not(defendWinMove(Board))):
            if (not (checkDangerousMove(Board))):
                if (not(createWinMove(Board))):
                    if Board[1]==2:
                        Board[1]=5
                    elif Board[3]==2:
                        Board[3]=5
                    elif Board[5]==2:
                        Board[5]=5
                    elif Board[7]==2:
                        Board[7]=5
    elif (Turn==5):
        if (not(defendWinMove(Board))):
            if (not (createForkWinMove(Board))):
                if (not(createWinMove(Board))):
                    if Board[1]==2:
                        Board[1]=5
                    elif Board[3]==2:
                        Board[3]=5
                    elif Board[5]==2:
                        Board[5]=5
                    elif Board[7]==2:
                        Board[7]=5
    elif (Turn==6 or Turn==7 or Turn==8 or Turn==9):
        if (not(defendWinMove(Board))):
            if (not(createWinMove(Board))):
                if Board[0]==2:
                    Board[0]=5
                elif Board[1]==2:
                    Board[1]=5
                elif Board[2]==2:
                    Board[2]=5
                elif Board[3]==2:
                    Board[3]=5
                elif Board[5]==2:
                    Board[5]=5
                elif Board[6]==2:
                    Board[6]=5
                elif Board[7]==2:
                    Board[7]=5
                elif Board[8]==2:
                    Board[8]=5

# The board is drawn after each move is given

def displayBoard(Board):
    if Board[0]==2:
        Board0=' '
    elif Board[0]==3:
        Board0='X'
    else:
        Board0='O'

    if Board[1]==2:
        Board1=' '
    elif Board[1]==3:
        Board1='X'
    else:
        Board1='O'

    if Board[2]==2:
        Board2=' '
    elif Board[2]==3:
        Board2='X'
    else:
        Board2='O'

    if Board[3]==2:
        Board3=' '
    elif Board[3]==3:
        Board3='X'
    else:
        Board3='O'

    if Board[4]==2:
        Board4=' '
    elif Board[4]==3:
        Board4='X'
    else:
        Board4='O'

    if Board[5]==2:
        Board5=' '
    elif Board[5]==3:
        Board5='X'
    else:
        Board5='O'

    if Board[6]==2:
        Board6=' '
    elif Board[6]==3:
        Board6='X'
    else:
        Board6='O'

    if Board[7]==2:
        Board7=' '
    elif Board[7]==3:
        Board7='X'
    else:
        Board7='O'

    if Board[8]==2:
        Board8=' '
    elif Board[8]==3:
        Board8='X'
    else:
        Board8='O'
        
    print('\r\n   |   |')
    print(' ' + Board0 + ' | ' + Board1 + ' | ' + Board2)
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + Board3 + ' | ' + Board4 + ' | ' + Board5)
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + Board6 + ' | ' + Board7 + ' | ' + Board8)
    print('   |   |')

def TicTacToe():
    Board=[2,2,2,2,2,2,2,2,2]

    Turn=1

    # Random Selection of whether Computer or Human gives the first move

    if (random.randint(0,1)==0):
        print('*** Computer Plays First (Randomly Selected) ****')
        Board[4]=5
        Turn=Turn+1
    else:
        print('*** Human Plays First (Randomly Selected) ***')
    
    displayBoard(Board)

    while True:
        print('------------------------------')

        key = 1
        
        while True:
            num = int(input('Enter a number within 1 to 9: '))

            if ((num>=1) and (num<=9)):
                if (Board[num-1]==2):
                    Board[num-1]=3
                    displayBoard(Board)
                    print('------------------------------')
                    Turn=Turn+1
                    break
                else:
                    print('The Board Position is already occupied.')
            else:
                key=0
                break

        if (key==0):
            print('Hope, next time you will play the game properly.')
            break
            
        if (Turn>=5):
            if (seeHumanWins(Board)):
                print('Congratulations! You win the game.')
                break
            elif (goForWinMove(Board)):
                displayBoard(Board)
                print('Computer Wins.')
                break

        if (Turn==10):
            print('The game is draw. Better luck next time.')
            break
        
        calculateMove(Board,Turn)

        displayBoard(Board)

        Turn=Turn+1

        if (Turn==10):
            print('The game is draw. Better luck next time.')
            break

# Start of the TicTacToe Program

TicTacToe()

while True:    
    option = input('Play again?(y/n) ')

    if option == 'y':
        TicTacToe()
    else:
        exit()

