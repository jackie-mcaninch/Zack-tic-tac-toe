#Two player tic-tac-toe

import turtle
board = turtle.Pen()

#Start the game

def tic_tac_toe(board):

#Draw the board
    board.up()
    board.right(90)
    board.forward(100)
    board.left(90)
    board.down()
    board.forward(300)
    board.left(180)
    board.forward(600)
    board.right(180)
    board.forward(200)
    board.right(90)
    board.forward(200)
    board.left(180)
    board.forward(400)
    board.left(90)
    board.forward(200)
    board.left(180)
    board.forward(200)
    board.left(90)
    board.forward(200)
    board.right(180)
    board.forward(200)
    board.left(90)
    board.forward(400)
    board.right(180)
    board.forward(200)
    board.right(90)
    board.forward(200)
    board.right(180)
    board.forward(600)
    board.up()
    board.home()
    board.down()

    game_board = ['useless call for clarity',1,2,3,4,5,6,7,8,9]

#Making the x
    def x_motion(board):
        board.forward(100)
        board.right(180)
        board.forward(200)
        board.left(180)
        board.forward(100)
        board.right(90)
        board.forward(100)
        board.right(180)
        board.forward(200)
        board.up()
        board.home()
        board.down()

#Making the o
    def o_motion(board):
        board.up()
        board.right(90)
        board.forward(15)
        board.left(90)
        board.down()
        for loop in range(0,45):
            board.forward(12)
            board.left(8)
        
#Choose player one's space                        
    def player_one(game_board, board):
        print('Player 1, please pick a spot on the board.')
        player_x = int(input())

        for x in range(1,10):
            if(player_x > 9 or player_x < 1):
                print('Sorry, that space is not in the grid. Choose again.')
                player_x = int(input())
                continue
            else:
                board.pencolor('red')
                if(game_board[player_x] == 'O' or game_board[player_x] == 'X'):
                    print('Sorry, that space is taken. Choose again.')
                    player_x = int(input())
                else:
                    game_board[player_x] = 'X'
                    if(game_board[player_x] == 'X'):
                        x = player_x
                        if(x > 6 and x < 10):
                            board.up()
                            board.right(90)
                            board.forward(200)
                            board.down()
                            if(x == 7):
                                board.up()
                                board.right(90)
                                board.forward(200)
                                board.right(45)
                                board.down()
                                x_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            elif(x == 8):
                                board.right(135)
                                x_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            else:
                                board.up()
                                board.left(90)
                                board.forward(200)
                                board.left(135)
                                board.down()
                                x_motion(board)
                                board.up()
                                board.home()
                                board.down()
                        elif(x > 3 and x < 7):
                            if(x == 4):
                                board.up()
                                board.left(180)
                                board.forward(200)
                                board.right(45)
                                board.down()
                                x_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            elif(x == 5):
                                board.left(135)
                                x_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            elif(x == 6):
                                board.up()
                                board.forward(200)
                                board.down()
                                board.left(135)
                                x_motion(board)
                                board.up()
                                board.home()
                                board.down()
                        elif(x > 0 and x < 4):
                            board.up()
                            board.left(90)
                            board.forward(200)
                            board.down()
                            if(x == 1):
                                board.up()
                                board.left(90)
                                board.forward(200)
                                board.right(45)
                                board.down()
                                x_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            elif(x == 2):
                                board.left(45)
                                x_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            elif(x == 3):
                                board.up()
                                board.right(90)
                                board.forward(200)
                                board.left(135)
                                board.down()
                                x_motion(board)
                                board.up()
                                board.home()
                                board.down()
                        break
            print('Player 1, your turn is over.')

#Choose player two's space
    def player_two(game_board, board):
        print('Player 2, please pick a spot on the board.')
        player_o = int(input())

        for o in range(1,10):
            if(player_o > 9 or player_o < 1):
                print('Sorry, that space is not in the grid. Choose again.')
                player_o = int(input())
                continue
            else:
                board.pencolor('blue')
                if(game_board[player_o] == 'O' or game_board[player_o] == 'X'):
                    print('Sorry, that space is taken. Choose again.')
                    player_o = int(input())
                else:
                    game_board[player_o] = 'O'
                    if(game_board[player_o] == 'O'):
                        o = player_o
                        if(o > 6 and o < 10):
                            board.up()
                            board.right(90)
                            board.forward(200)
                            board.down()
                            if(o == 7):
                                board.up()
                                board.right(90)
                                board.forward(125)
                                board.right(90)
                                board.down()
                                o_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            elif(o == 8):
                                board.left(90)
                                board.up()
                                board.forward(75)
                                board.left(90)
                                board.down()
                                o_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            else:
                                board.up()
                                board.left(90)
                                board.forward(275)
                                board.down()
                                board.left(90)
                                o_motion(board)
                                board.up()
                                board.home()
                                board.down()
                        elif(o > 3 and o < 7):
                            if(o == 4):
                                board.up()
                                board.left(180)
                                board.forward(125)
                                board.right(90)
                                board.down()
                                o_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            elif(o == 5):
                                board.up()
                                board.forward(75)
                                board.down()
                                board.left(90)
                                o_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            elif(o == 6):
                                board.up()
                                board.forward(275)
                                board.down()
                                board.left(90)
                                o_motion(board)
                                board.up()
                                board.home()
                                board.down()
                        elif(o > 0 and o < 4):
                            board.up()
                            board.left(90)
                            board.forward(200)
                            board.down()
                            if(o == 1):
                                board.up()
                                board.left(90)
                                board.forward(125)
                                board.right(90)
                                board.down()
                                o_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            elif(o == 2):
                                board.right(90)
                                board.up()
                                board.forward(75)
                                board.down()
                                board.left(90)
                                o_motion(board)
                                board.up()
                                board.home()
                                board.down()
                            elif(o == 3):
                                board.up()
                                board.right(90)
                                board.forward(275)
                                board.left(90)
                                board.down()
                                o_motion(board)                      
                                board.up()
                                board.home()
                                board.down()
                        break
        print('Player 2, your turn is over.')

#Check for rows or ties
    for simulation in range(0,5):
        player_one(game_board,board)
        if(game_board[1] == 'X' and game_board[2] == 'X' and game_board[3] == 'X'):
            print('Congratulations! Player 1 is the winner!')
            break
        elif(game_board[1] == 'X' and game_board[4] == 'X' and game_board[7] == 'X'):
            print('Congratulations! Player 1 is the winner!')
            break
        elif(game_board[1] == 'X' and game_board[5] == 'X' and game_board[9] == 'X'):
            print('Congratulations! Player 1 is the winner!')
            break
        elif(game_board[2] == 'X' and game_board[5] == 'X' and game_board[8] == 'X'):
            print('Congratulations! Player 1 is the winner!')
            break
        elif(game_board[3] == 'X' and game_board[5] == 'X' and game_board[7] == 'X'):
            print('Congratulations! Player 1 is the winner!')
            break
        elif(game_board[3] == 'X' and game_board[6] == 'X' and game_board[9] == 'X'):
            print('Congratulations! Player 1 is the winner!')
            break
        elif(game_board[4] == 'X' and game_board[5] == 'X' and game_board[6] == 'X'):
            print('Congratulations! Player 1 is the winner!')
            break
        elif(game_board[7] == 'X' and game_board[8] == 'X' and game_board[9] == 'X'):
            print('Congratulations! Player 1 is the winner!')
            break

        if(game_board[1] != 1 and game_board[2] != 2 and game_board[3] != 3 and game_board[4] != 4 and game_board[5] != 5 and game_board[6] != 6 and game_board[7] != 7 and game_board[8] != 8 and game_board[9] != 9):
            print('Cat game!')
            break
        
        player_two(game_board,board)
        if(game_board[1] == 'O' and game_board[2] == 'O' and game_board[3] == 'O'):
            print('Congratulations! Player 2 is the winner!')
            break
        elif(game_board[1] == 'O' and game_board[4] == 'O' and game_board[7] == 'O'):
            print('Congratulations! Player 2 is the winner!')
            break
        elif(game_board[1] == 'O' and game_board[5] == 'O' and game_board[9] == 'O'):
            print('Congratulations! Player 2 is the winner!')
            break
        elif(game_board[2] == 'O' and game_board[5] == 'O' and game_board[8] == 'O'):
            print('Congratulations! Player 2 is the winner!')
            break
        elif(game_board[3] == 'O' and game_board[5] == 'O' and game_board[7] == 'O'):
            print('Congratulations! Player 2 is the winner!')
            break
        elif(game_board[3] == 'O' and game_board[6] == 'O' and game_board[9] == 'O'):
            print('Congratulations! Player 2 is the winner!')
            break
        elif(game_board[4] == 'O' and game_board[5] == 'O' and game_board[6] == 'O'):
            print('Congratulations! Player 2 is the winner!')
            break
        elif(game_board[7] == 'O' and game_board[8] == 'O' and game_board[9] == 'O'):
            print('Congratulations! Player 2 is the winner!')
            break

#Call the function
tic_tac_toe(board)
