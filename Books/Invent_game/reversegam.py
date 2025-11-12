
import random, sys

EMPTY = ' '
DIRECTIONS = ((0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))

def getNewBoard():
    board = []
    for i in range(8):
        board.append([EMPTY] * 8)
    return board

def resetBoard(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = EMPTY
    # Starting pieces:
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

def drawBoard(board):
    # Print the board to the screen.
    print('  1 2 3 4 5 6 7 8')
    print(' +---------------+')
    for y in range(8):
        print('%d|' % (y+1), end='')
        for x in range(8):
            print(board[x][y] + ' ', end='')
        print('|%d' % (y+1))
    print(' +---------------+')
    print('  1 2 3 4 5 6 7 8')

def isOnBoard(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7

def getBoardCopy(board):
    dupe = getNewBoard()
    for x in range(8):
        for y in range(8):
            dupe[x][y] = board[x][y]
    return dupe

def isValidMove(board, tile, xstart, ystart):
    # If the space is not empty or the coordinates are off the board, return False.
    if not isOnBoard(xstart, ystart) or board[xstart][ystart] != EMPTY:
        return False

    board[xstart][ystart] = tile  # temporarily set the tile on the board.

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in DIRECTIONS:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting each piece.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append((x, y))

    board[xstart][ystart] = EMPTY  # restore the empty space
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip

def getValidMoves(board, tile):
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y):
                validMoves.append((x, y))
    return validMoves

def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X': xscore, 'O': oscore}

def enterPlayerTile():
    # Let the player type which tile they want to be.
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if not tilesToFlip:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardWithValidMoves(board, tile):
    dupe = getBoardCopy(board)
    for x, y in getValidMoves(dupe, tile):
        dupe[x][y] = '.'
    return dupe

def getPlayerMove(board, playerTile):
    # Let the player type in their move.
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints.')
        move = input().lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'
        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y):
                return (x, y)
            else:
                print('That is not a valid move.')
        else:
            print('Enter the column (1-8) and the row (1-8). For example 81 will move to the top-right.')

def showPoints(playerTile, computerTile, board):
    scores = getScoreOfBoard(board)
    print('You: %s points. Computer: %s points.' % (scores[playerTile], scores[computerTile]))

def getComputerMove(board, computerTile):
    # Algorithm for the computer's move:
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)

    # If there's a corner move, take it.
    for x, y in possibleMoves:
        if (x, y) in [(0,0),(0,7),(7,0),(7,7)]:
            return (x, y)

    # Otherwise, choose the move that flips the most pieces.
    bestScore = -1
    bestMove = None
    for x, y in possibleMoves:
        dupe = getBoardCopy(board)
        makeMove(dupe, computerTile, x, y)
        score = getScoreOfBoard(dupe)[computerTile]
        if score > bestScore:
            bestScore = score
            bestMove = (x, y)
    return bestMove

def reset():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def playGame():
    print('Welcome to Reversegam!')
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    showHints = False
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    while True:
        playerValidMoves = getValidMoves(mainBoard, playerTile)
        computerValidMoves = getValidMoves(mainBoard, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return mainBoard  # No more valid moves; game over.

        if turn == 'player':
            if playerValidMoves != []:
                if showHints:
                    validBoard = getBoardWithValidMoves(mainBoard, playerTile)
                    drawBoard(validBoard)
                else:
                    drawBoard(mainBoard)
                showPoints(playerTile, computerTile, mainBoard)
                move = getPlayerMove(mainBoard, playerTile)
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit()
                if move == 'hints':
                    showHints = not showHints
                    continue
                else:
                    makeMove(mainBoard, playerTile, move[0], move[1])
            turn = 'computer'

        else:
            if computerValidMoves != []:
                drawBoard(mainBoard)
                showPoints(playerTile, computerTile, mainBoard)
                input('Press Enter to see the computer\'s move.')
                x, y = getComputerMove(mainBoard, computerTile)
                makeMove(mainBoard, computerTile, x, y)
            turn = 'player'

def main():
    while True:
        finalBoard = playGame()
        drawBoard(finalBoard)
        scores = getScoreOfBoard(finalBoard)
        print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
        if scores['X'] > scores['O']:
            print('X wins!')
        elif scores['O'] > scores['X']:
            print('O wins!')
        else:
            print('The game is a tie!')
        if not reset():
            break

if __name__ == '__main__':
    main()
