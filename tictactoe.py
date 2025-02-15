from random import randrange

def print_horizontal_border():
  print(3*"+-------", "+", sep="")

def print_padding():
  print("|", "|", "|", "|", sep=7*" ")

def display_board(board):
  for i in range(3):
    print_horizontal_border()
    print_padding()
    print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|", sep=3*" ")
    print_padding()
  print_horizontal_border()

def make_list_of_free_fields(board):
  free_fields = []
  for i in range(3):
    for j in range(3):
      if board[i][j] not in ("X", "O"):
        free_fields.append((i, j))
  return free_fields

def enter_move(board):
  free_fields = make_list_of_free_fields(board)
  while True:
    try:
      field = int(input("Enter your move: "))
    except ValueError:
      print("Invalid input")
      continue
    row, col = (field-1) // 3, (field-1) % 3
    if field > 0 and field < 10 and (row, col) in free_fields:
      board[row][col] = "O"
      break
    else:
      print("Invalid move")

def draw_move(board):
  free_fields = make_list_of_free_fields(board)
  choice = randrange(len(free_fields))
  row, col = free_fields[choice]
  board[row][col] = "X"

def victory_for(board, sign):
  pattern = (sign, sign, sign)
  # check horizontal
  for i in range(3):
    if (board[i][0], board[i][1], board[i][2]) == pattern:
      return True
  # check vertical
  for i in range(3):
    if (board[0][i], board[1][i], board[2][i]) == pattern:
      return True
  # check diagonal
  if (board[0][0], board[1][1], board[2][2]) == pattern:
    return True
  if (board[0][2], board[1][1], board[2][0]) == pattern:
    return True
  return False

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
user_turn, victory = False, False

display_board(board)
for i in range(8):
  user_turn = not user_turn
  if user_turn:
    enter_move(board)
    victory = victory_for(board, "O")
  else:
    draw_move(board)
    victory = victory_for(board, "X")
  display_board(board)
  if victory:
    print("You won!") if user_turn else print("I won!")
    break
if not victory:
  print("Tie...")
