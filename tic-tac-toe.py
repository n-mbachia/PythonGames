import random

print("Welcome to tic tac toe")
print("----------------------")

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3


def printGameBoard():
  for x in range(rows):
    print("\n+---+---+---+")  # prints the rows defininations as defined
    print("|", end="")
    for y in range(cols):
      print("", gameBoard[x][y], end=" |")  # prints | seperatorin column as defined
  print("\n+---+---+---+")  # prints last line


def modifyArray(num, turn):
  num -= 1
  if(num == 0):
    gameBoard[0][0] = turn
  elif(num == 1):
    gameBoard[0][1] = turn
  elif(num == 2):
    gameBoard[0][2] = turn
  elif(num == 3):
    gameBoard[1][0] = turn
  elif(num == 4):
    gameBoard[1][1] = turn
  elif(num == 5):
    gameBoard[1][2] = turn
  elif(num == 6):
    gameBoard[2][0] = turn
  elif(num == 7):
    gameBoard[2][1] = turn
  elif(num == 8):
    gameBoard[2][2] = turn

# check for winner three possible win scenarios


def winnerCheck(gameBoard):
  # Horizontal winner scenerio for both X & O (x-axis)
  if(gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X"):
    return "X"
  elif(gameBoard[0][0] == "O" and gameBoard[0][1] == "O" and gameBoard[0][2] == "O"):
    return "O"
  elif(gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X"):
    return "X"
  elif(gameBoard[1][0] == "O" and gameBoard[1][1] == "O" and gameBoard[1][2] == "O"):
    return "O"
  elif(gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X"):
    return "X"
  elif(gameBoard[2][0] == "O" and gameBoard[2][1] == "O" and gameBoard[2][2] == "O"):
    return "O"
# The vertical winner scenario for both X & O (y-axis)
  elif(gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X"):
    return "X"
  elif(gameBoard[0][0] == "O" and gameBoard[1][0] == "O" and gameBoard[2][0] == "O"):
    return "O"
  elif(gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X"):
    return "X"
  elif(gameBoard[0][1] == "O" and gameBoard[1][1] == "O" and gameBoard[2][1] == "O"):
    return "O"
  elif(gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X"):
    return "X"
  elif(gameBoard[0][2] == "O" and gameBoard[1][2] == "0" and gameBoard[2][2] == "0"):
    return "O"
  # The diagonally winner check scenario
  elif(gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X"):
    return "X"
  elif(gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O"):
    return "O"
  elif(gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X"):
    return "X"
  elif(gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O"):
    return "O"
  else:
    return "N"


leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
  # it's the player turn
  if(turnCounter % 2 == 0):
    printGameBoard()  # invokes function
    try:
      numberPicker = int(input("\nPick a number between [1 - 9]: "))
      if(type(numberPicker) is int, (numberPicker >= 1 or numberPicker <= 9)):
        modifyArray(numberPicker, "X")
        possibleNumbers.remove(numberPicker)
      turnCounter += 1
    except ValueError:
      print("Please pick a number between [1 - 9]: ")
    except:
      if(type(numberPicker) is int, (numberPicker > 9)):
        print("Please try again. Pick a number between [1 - 9]: ")
    #turnCounter += 1
  # the other player's turn (In this case, it is the computer's turn)
  else:
    while(True):
      compChoice = random.choice(possibleNumbers)
      print("\n iMacMbachia: ", compChoice)
      if(compChoice in possibleNumbers):
        modifyArray(compChoice, "O")
        possibleNumbers.remove(compChoice)
        turnCounter += 1
        break

  winner = winnerCheck(gameBoard)
  if(winner != "N"):
    print("\nThe winner is,", winner, "!!!! Thank you for playing :-)")
    break
  elif(winner == "N"):
    print("Its a tie between players!!! ;-|")
