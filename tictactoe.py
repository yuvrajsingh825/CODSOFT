# Initialize board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# Function to print the game board
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("_________")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("_________")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("_________")

# Function for player input
def playerInput(board):
    inp = int(input("Enter a number (1-9): "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops! That spot is already taken!")

# Check for horizontal winner
def checkHorizontle(board):
    global winner 
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

# Check for vertical winner
def checkRow(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True 
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True 
    return False

# Check for diagonal winner
def checkDiag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

# Check for a tie
def checkTie(board):
    if "-" not in board and winner is None:
        printBoard(board)
        print("It's a Tie!")
        return True
    return False

# Main game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    
    if checkHorizontle(board) or checkRow(board) or checkDiag(board):
        printBoard(board)
        print(f"Player '{winner}' wins!")
        gameRunning = False
    
    if checkTie(board):
        gameRunning = False

    # Switch players
    currentPlayer = "O" if currentPlayer == "X" else "X"
