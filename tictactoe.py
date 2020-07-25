from IPython.display import clear_output

def display_board(board):
    print(board[1]+'|'+ board[2]+'|'+board[3])
    print(board[4]+'|'+ board[5]+'|'+board[6])
    print(board[7]+'|'+ board[8]+'|'+board[9])
def player_input():
    
    word = ''
    
    while word != 'X' and word != 'O':
        word = input("Player One: Do you want to be X or O?: ")
        if word != 'X' and word != 'O' :
            print("Invalid entry, try again.")
            
    marker1 = word
    
    if word == 'X':
        marker2 = 'O'
    if word == 'O':
        marker2 = 'X'
 
    print("Player One is " + marker1 + ', ' + 'Player Two is ' + marker2)
def place_marker(board, marker, position):
    
    while marker1 == 'X':
        marker2 = 'O'
        break
    while marker1 == 'O':
        marker2 = 'X'
        break
    
    position = input("Where would you like to place your marker? ")

    ## IF THE POSITION IS NOT EMPTY, ALLOW FOR NEW POSITION TO BE INPUTTED, AND THEN CHECK IF THAT IS EMPTY
    
    while board[int(position)]!='':
        print("This spot is taken. Please try again")
        position = input("Please select another spot: ")
       
    ## IF THE POSITION IS EMPTY, REPLACE THE EMPTY SLOT WITH THE MARKER
    
    while board[int(position)] == '':
        board[int(position)] = marker
        display_board(board)
    
    tie_check(board)
def replay():
    
    response = ''
    
    while response != 'Y' and response != 'N':
        response = input("Do you want to play again (Y/N)? ")
        print(response)
    
    if response == 'Y' or response == 'N':
        if response == 'Y':
            board = ['#','','','','','','','','','']
            

            while marker1 == 'X':
                marker2 = 'O'
                break
            while marker1 == 'O':
                marker2 = 'X'
                break

            tie_check(board)

            display_board(board)
            position = input("Where would you like to place your marker? ")

            while board[int(position)]!='':
                    print("This spot is taken. Please try again")
                    position = input("Please select another spot: ")

                ## IF THE POSITION IS EMPTY, REPLACE THE EMPTY SLOT WITH THE MARKER

            while board[int(position)] == '':
                board[int(position)] = marker1
                display_board(board)
                tie_check(board)
                win_check(board, int(position), marker1)

        else:
            print("Thanks for playing!")
def replay2():
    replay()
def win_check(board, position, marker1): 

    while position == 1:
        if board[2] == marker1 and board[3] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[4] == marker1 and board[7] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[5] == marker1 and board[9] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player2(board)
            break
    while position == 2:
        if board[1] == marker1 and board[3] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[5] == marker1 and board[8] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player2(board)
            break
    while position == 3:
        if board[1] == marker1 and board[2] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[6] == marker1 and board[9] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[5] == marker1 and board[7] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player2(board)
            break
    while position == 4:
        if board[1] == marker1 and board[7] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[5] == marker1 and board[6] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player2(board)
            break
    while position == 5:
        if board[2] == marker1 and board[8] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[4] == marker1 and board[6] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[1] == marker1 and board[9] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[3] == marker1 and board[7] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player2(board)
            break
    while position == 6:
        if board[4] == marker1 and board[5] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[3] == marker1 and board[9] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player2(board)
            break
    while position == 7:
        if board[8] == marker1 and board[9] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[1] == marker1 and board[4] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[3] == marker1 and board[5] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player2(board)
            break
    while position == 8:
        if board[2] == marker1 and board[5] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[7] == marker1 and board[9] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player2(board)
            break
    while position == 9:
        if board[7] == marker1 and board[8] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[3] == marker1 and board[6] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[1] == marker1 and board[5] == marker1:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player2(board)
            break
def win_check2(board, position, marker2):
    if marker1 == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'

    while position == 1:
        if board[2] == marker2 and board[3] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[4] == marker2 and board[7] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[5] == marker2 and board[9] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player1(board, marker1)
            break
    while position == 2:
        if board[1] == marker2 and board[3] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[5] == marker2 and board[8] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player1(board, marker1)
            break
    while position == 3:
        if board[1] == marker2 and board[2] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[6] == marker2 and board[9] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[5] == marker2 and board[7] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player1(board, marker1)
            break
    while position == 4:
        if board[1] == marker2 and board[7] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[5] == marker2 and board[6] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player1(board, marker1)
            break
    while position == 5:
        if board[2] == marker2 and board[8] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[4] == marker2 and board[6] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[1] == marker2 and board[9] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[3] == marker2 and board[7] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player1(board, marker1)
            break
    while position == 6:
        if board[4] == marker2 and board[5] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[3] == marker2 and board[9] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player1(board, marker1)
            break
    while position == 7:
        if board[8] == marker2 and board[9] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[1] == marker2 and board[4] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[3] == marker2 and board[5] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player1(board, marker1)
            break
    while position == 8:
        if board[2] == marker2 and board[5] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[7] == marker2 and board[9] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player1(board, marker1)
            break
    while position == 9:
        if board[7] == marker2 and board[8] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[3] == marker2 and board[6] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        elif board[1] == marker2 and board[5] == marker2:
            display_board(board)
            print("You Won!")
            replay()
            break
        else:
            player1(board, marker1)
            break
def player2(board):
    if marker1 == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'
    tie_check(board)
    
    display_board(board)
    position = input("Player 2, where would you like to place your marker? ")

    while board[int(position)]!='':
            print("This spot is taken. Please try again")
            position = input("Please select another spot: ")

    ## IF THE POSITION IS EMPTY, REPLACE THE EMPTY SLOT WITH THE MARKER

    while board[int(position)] == '':
        board[int(position)] = marker2
        win_check2(board, int(position), marker2)
        break    
def player1(board, marker1):
    if marker1 == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'

    tie_check(board)
    display_board(board)
    position = input("Player 1, where would you like to place your marker? ")

    while board[int(position)]!='':
            print("This spot is taken. Please try again")
            position = input("Please select another spot: ")
    ## IF THE POSITION IS EMPTY, REPLACE THE EMPTY SLOT WITH THE MARKER

    while board[int(position)] == '':
        board[int(position)] = marker1
        #display_board(board)
        win_check(board, int(position), marker1)
        break
def tie_check(board):

    while board[1] != '' and board[2] != '' and board[3] != '' and board[4] != '' and board[5] != '' and board[6] != '' and board[7] != '' and board[8] != '' and board[9] != '':
        display_board(board)
        print("Game Over. TIE")
        replay() 
        board = ['#','','','','','','','','','']
        break

print('Welcome to Tic Tac Toe!')


board = ['#','','','','','','','','','']
display_board(board)

word = '' 
    
while word != 'X' and word != 'O':
    word = input("Player One: Do you want to be X or O?: ")
    if word != 'X' and word != 'O' :
        print("Invalid entry, try again.")
            
marker1 = word
    
if marker1 == 'X':
    marker2 = 'O'
else:
    marker1 = 'O'
    marker2 = 'X'

print("Player One is " + marker1 + ', ' + 'Player Two is ' + marker2)

tie_check(board)

display_board(board)
position = input("Where would you like to place your marker? ")

while board[int(position)]!='':
        print("This spot is taken. Please try again")
        position = input("Please select another spot: ")
       
    ## IF THE POSITION IS EMPTY, REPLACE THE EMPTY SLOT WITH THE MARKER
    
while board[int(position)] == '':
    board[int(position)] = marker1
    display_board(board)
    win_check(board, int(position), marker1)