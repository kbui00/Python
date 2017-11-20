from random import randint

board = []
x_axis = []
y_axis = []



for x in range(0,size):
  board.append(["O"] * size)

def print_board(board):
  for row in board:
    print (" ".join(row))
    
print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#Debugging
print (ship_row)
print (ship_col)

for turn in range(4):
  print ("Turn", turn + 1)
  #guess_row = int(raw_input("Guess Row: "))        #Python 2
  #guess_col = int(raw_input("Guess Col: "))        #Python 2
  guess_row = eval(input("Guess Row: "))            #Python 3
  guess_col = eval(input("Guess Col: "))            #Python 3

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
    if turn == 3:
      print ('Game Over')
