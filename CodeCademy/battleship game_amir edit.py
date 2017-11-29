from random import randint
import sys,time,random

board = []
axis = []

#Human typing simulation
typing_speed = 70 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')

#slow_type("Welcome Commander, I am happy to have you with us today. Getting right to the point, we are facing a hidden enemy battleship within our territory. The enemy's presence has severely undermined our effort to supply the front line. It is up to you to lead us one step closer to victory by destroying the enemy's battleship.")
print ("")
#size = int(raw_input('Enter board size: ')

valid = 11
#while valid < 10:
 # size = eval(input('Please enter your desired board size (smaller than 11): '))
  #valid = size
#print ("")
size = eval(input('enter board size: '))

for x in range(0,size):
  board.append([str(x)] + ["O"] * size)

#def print_board(board):
#  z = 0
#  for row in board:
#    while z < size:
#      print (z,  " ".join(row))
#      z = z + 1
      
def print_board(board):
  s=''
  for row in board:
    for i in range(len(row)):
      if (i == 2) and row[2]== " ":
        s=s+" "
      s = s+ row[i] + " "
    s=s+'\n'
  print(s)
    
axis.append([str(x) for x in range(0,size)])
def print_xaxis(axis):
  for x in axis:
    print (" ", " ".join(x))

print_xaxis(axis)
print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#Debugging
#print (ship_row)
#print (ship_col)

for turn in range(size-1):
  print ("")
  print ("Turn", turn + 1)
  print ("")
  #guess_row = int(raw_input("Guess Row: "))        #Python 2
  #guess_col = int(raw_input("Guess Col: "))        #Python 2
  guess_row = eval(input("Guess X coordinate: "))            #Python 3
  guess_col = eval(input("Guess Y coordinate: "))            #Python 3
  guess_col_1 = guess_col + 1
  if guess_row == ship_row and guess_col_1 == ship_col:
    print ("")
    print ("You are victorious!")
    break
  else:
    if guess_row not in range(size) or guess_col_1 not in range(size+1):
      print ("")
      print ("Oops, that's not even in the ocean.")
      print ("")
    elif board[guess_row][guess_col_1] == "X":
      print ("")
      print( "You guessed that one already." )
      print ("")
    else:
      print ("")
      print ("You missed their battleship!")
      print ("")
      board[guess_row][guess_col_1] = "X"
    print_xaxis(axis)
    print_board(board)
    if turn == size - 2:
      print ('Game Over')
