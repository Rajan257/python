# # import random

# # EMPTY = ' '
# # DIRECTIONS = ((0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))

# # def getNewBoard():
# #     board = []
# #     for i in range(8):
# #         board.append([EMPTY] * 8)
# #     return board

# # def resetBoard(board):
# #     for x in range(8):
# #         for y in range(8):
# #             board[x][y] = EMPTY
# #     board[3][3] = 'X'
# #     board[3][4] = 'O'
# #     board[4][3] = 'O'
# #     board[4][4] = 'X'

# # def isOnBoard(x, y):
# #     return 0 <= x <= 7 and 0 <= y <= 7

# # def getBoardCopy(board):
# #     dupe = getNewBoard()
# #     for x in range(8):
# #         for y in range(8):
# #             dupe[x][y] = board[x][y]
# #     return dupe

# # def isValidMove(board, tile, xstart, ystart):
# #     if not isOnBoard(xstart, ystart) or board[xstart][ystart] != EMPTY:
# #         return False
# #     board[xstart][ystart] = tile
# #     otherTile = 'O' if tile == 'X' else 'X'
# #     tilesToFlip = []
# #     for xdirection, ydirection in DIRECTIONS:
# #         x, y = xstart, ystart
# #         x += xdirection
# #         y += ydirection
# #         if isOnBoard(x, y) and board[x][y] == otherTile:
# #             x += xdirection
# #             y += ydirection
# #             if not isOnBoard(x, y):
# #                 continue
# #             while board[x][y] == otherTile:
# #                 x += xdirection
# #                 y += ydirection
# #                 if not isOnBoard(x, y):
# #                     break
# #             if not isOnBoard(x, y):
# #                 continue
# #             if board[x][y] == tile:
# #                 while True:
# #                     x -= xdirection
# #                     y -= ydirection
# #                     if x == xstart and y == ystart:
# #                         break
# #                     tilesToFlip.append((x, y))
# #     board[xstart][ystart] = EMPTY
# #     if len(tilesToFlip) == 0:
# #         return False
# #     return tilesToFlip

# # def getValidMoves(board, tile):
# #     validMoves = []
# #     for x in range(8):
# #         for y in range(8):
# #             if isValidMove(board, tile, x, y):
# #                 validMoves.append((x, y))
# #     return validMoves

# # def getScoreOfBoard(board):
# #     xscore = oscore = 0
# #     for x in range(8):
# #         for y in range(8):
# #             if board[x][y] == 'X':
# #                 xscore += 1
# #             elif board[x][y] == 'O':
# #                 oscore += 1
# #     return {'X': xscore, 'O': oscore}

# # def makeMove(board, tile, xstart, ystart):
# #     tilesToFlip = isValidMove(board, tile, xstart, ystart)
# #     if not tilesToFlip:
# #         return False
# #     board[xstart][ystart] = tile
# #     for x, y in tilesToFlip:
# #         board[x][y] = tile
# #     return True

# # def getCornerBestMove(board, tile):
# #     possibleMoves = getValidMoves(board, tile)
# #     if not possibleMoves:
# #         return None
# #     random.shuffle(possibleMoves)
# #     for x, y in possibleMoves:
# #         if (x, y) in [(0,0),(0,7),(7,0),(7,7)]:
# #             return (x, y)
# #     bestScore = -1
# #     bestMove = None
# #     for x, y in possibleMoves:
# #         dupe = getBoardCopy(board)
# #         makeMove(dupe, tile, x, y)
# #         score = getScoreOfBoard(dupe)[tile]
# #         if score > bestScore:
# #             bestScore = score
# #             bestMove = (x, y)
# #     return bestMove

# # def getWorstMove(board, tile):
# #     possibleMoves = getValidMoves(board, tile)
# #     if not possibleMoves:
# #         return None
# #     worstScore = float('inf')
# #     worstMove = None
# #     for x, y in possibleMoves:
# #         dupe = getBoardCopy(board)
# #         makeMove(dupe, tile, x, y)
# #         score = getScoreOfBoard(dupe)[tile]
# #         if score < worstScore:
# #             worstScore = score
# #             worstMove = (x, y)
# #     return worstMove

# # def getRandomMove(board, tile):
# #     possibleMoves = getValidMoves(board, tile)
# #     if not possibleMoves:
# #         return None
# #     return random.choice(possibleMoves)

# # def getCornerSideBestMove(board, tile):
# #     possibleMoves = getValidMoves(board, tile)
# #     if not possibleMoves:
# #         return None
# #     random.shuffle(possibleMoves)
# #     for m in possibleMoves:
# #         if m in [(0,0),(0,7),(7,0),(7,7)]:
# #             return m
# #     sides = [(0,i) for i in range(8)] + [(7,i) for i in range(8)] + [(i,0) for i in range(8)] + [(i,7) for i in range(8)]
# #     for m in possibleMoves:
# #         if m in sides:
# #             return m
# #     bestScore = -1
# #     bestMove = None
# #     for x, y in possibleMoves:
# #         dupe = getBoardCopy(board)
# #         makeMove(dupe, tile, x, y)
# #         score = getScoreOfBoard(dupe)[tile]
# #         if score > bestScore:
# #             bestScore = score
# #             bestMove = (x, y)
# #     return bestMove

# # def playGameWithAI(ai_X, ai_O):
# #     board = getNewBoard()
# #     resetBoard(board)
# #     turn = 'computer' if random.randint(0,1) == 0 else 'player'
# #     while True:
# #         validX = getValidMoves(board, 'X')
# #         validO = getValidMoves(board, 'O')
# #         if validX == [] and validO == []:
# #             return board
# #         if turn == 'player':
# #             if validX:
# #                 move = ai_X(board, 'X')
# #                 if move:
# #                     makeMove(board, 'X', *move)
# #             turn = 'computer'
# #         else:
# #             if validO:
# #                 move = ai_O(board, 'O')
# #                 if move:
# #                     makeMove(board, 'O', *move)
# #             turn = 'player'

# # def main():
# #     NUM_GAMES = 200
# #     xWins = oWins = ties = 0
# #     print('AISim3: corner-best (X) vs worst-move (O)')
# #     for i in range(NUM_GAMES):
# #         final = playGameWithAI(getCornerBestMove, getWorstMove)
# #         scores = getScoreOfBoard(final)
# #         if scores['X'] > scores['O']:
# #             xWins += 1
# #         elif scores['X'] < scores['O']:
# #             oWins += 1
# #         else:
# #             ties += 1
# #     print('X wins: %s (%s%%)' % (xWins, round(xWins / NUM_GAMES * 100, 1)))
# #     print('O wins: %s (%s%%)' % (oWins, round(oWins / NUM_GAMES * 100, 1)))
# #     print('Ties:   %s (%s%%)' % (ties, round(ties / NUM_GAMES * 100, 1)))

# # if __name__ == '__main__':
# #     main()
























# import random

# EMPTY = ' '
# DIRECTIONS = ((0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))

# def getNewBoard():
#     board = []
#     for i in range(8):
#         board.append([EMPTY] * 8)
#     return board

# def resetBoard(board):
#     for x in range(8):
#         for y in range(8):
#             board[x][y] = EMPTY
#     board[3][3] = 'X'
#     board[3][4] = 'O'
#     board[4][3] = 'O'
#     board[4][4] = 'X'

# def isOnBoard(x, y):
#     return 0 <= x <= 7 and 0 <= y <= 7

# def getBoardCopy(board):
#     dupe = getNewBoard()
#     for x in range(8):
#         for y in range(8):
#             dupe[x][y] = board[x][y]
#     return dupe

# def isValidMove(board, tile, xstart, ystart):
#     if not isOnBoard(xstart, ystart) or board[xstart][ystart] != EMPTY:
#         return False
#     board[xstart][ystart] = tile
#     otherTile = 'O' if tile == 'X' else 'X'
#     tilesToFlip = []
#     for xdirection, ydirection in DIRECTIONS:
#         x, y = xstart, ystart
#         x += xdirection
#         y += ydirection
#         if isOnBoard(x, y) and board[x][y] == otherTile:
#             x += xdirection
#             y += ydirection
#             if not isOnBoard(x, y):
#                 continue
#             while board[x][y] == otherTile:
#                 x += xdirection
#                 y += ydirection
#                 if not isOnBoard(x, y):
#                     break
#             if not isOnBoard(x, y):
#                 continue
#             if board[x][y] == tile:
#                 while True:
#                     x -= xdirection
#                     y -= ydirection
#                     if x == xstart and y == ystart:
#                         break
#                     tilesToFlip.append((x, y))
#     board[xstart][ystart] = EMPTY
#     if len(tilesToFlip) == 0:
#         return False
#     return tilesToFlip

# def getValidMoves(board, tile):
#     validMoves = []
#     for x in range(8):
#         for y in range(8):
#             if isValidMove(board, tile, x, y):
#                 validMoves.append((x, y))
#     return validMoves

# def getScoreOfBoard(board):
#     xscore = oscore = 0
#     for x in range(8):
#         for y in range(8):
#             if board[x][y] == 'X':
#                 xscore += 1
#             elif board[x][y] == 'O':
#                 oscore += 1
#     return {'X': xscore, 'O': oscore}

# def makeMove(board, tile, xstart, ystart):
#     tilesToFlip = isValidMove(board, tile, xstart, ystart)
#     if not tilesToFlip:
#         return False
#     board[xstart][ystart] = tile
#     for x, y in tilesToFlip:
#         board[x][y] = tile
#     return True

# def getComputerMove(board, computerTile):
#     possibleMoves = getValidMoves(board, computerTile)
#     if not possibleMoves:
#         return None
#     random.shuffle(possibleMoves)
#     for x, y in possibleMoves:
#         if (x, y) in [(0,0),(0,7),(7,0),(7,7)]:
#             return (x, y)
#     bestScore = -1
#     bestMove = None
#     for x, y in possibleMoves:
#         dupe = getBoardCopy(board)
#         makeMove(dupe, computerTile, x, y)
#         score = getScoreOfBoard(dupe)[computerTile]
#         if score > bestScore:
#             bestScore = score
#             bestMove = (x, y)
#     return bestMove

# def playGame():
#     board = getNewBoard()
#     resetBoard(board)
#     playerTile, computerTile = ['X', 'O']
#     turn = 'computer' if random.randint(0, 1) == 0 else 'player'
#     while True:
#         playerValidMoves = getValidMoves(board, playerTile)
#         computerValidMoves = getValidMoves(board, computerTile)
#         if playerValidMoves == [] and computerValidMoves == []:
#             return board
#         if turn == 'player':
#             if playerValidMoves:
#                 move = getComputerMove(board, playerTile)
#                 if move:
#                     makeMove(board, playerTile, *move)
#             turn = 'computer'
#         else:
#             if computerValidMoves:
#                 move = getComputerMove(board, computerTile)
#                 if move:
#                     makeMove(board, computerTile, *move)
#             turn = 'player'

# def main():
#     NUM_GAMES = 250
#     xWins = oWins = ties = 0
#     print('Welcome to Reversegam AI Tournament (AISim2)')
#     for i in range(NUM_GAMES):
#         final = playGame()
#         scores = getScoreOfBoard(final)
#         print('#%s: X scored %s points. O scored %s points.' % (i+1, scores['X'], scores['O']))
#         if scores['X'] > scores['O']:
#             xWins += 1
#         elif scores['X'] < scores['O']:
#             oWins += 1
#         else:
#             ties += 1
#     print('X wins: %s (%s%%)' % (xWins, round(xWins / NUM_GAMES * 100, 1)))
#     print('O wins: %s (%s%%)' % (oWins, round(oWins / NUM_GAMES * 100, 1)))
#     print('Ties:   %s (%s%%)' % (ties, round(ties / NUM_GAMES * 100, 1)))

# if __name__ == '__main__':
#     main()




























import random

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
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

def isOnBoard(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7

def getBoardCopy(board):
    dupe = getNewBoard()
    for x in range(8):
        for y in range(8):
            dupe[x][y] = board[x][y]
    return dupe

def isValidMove(board, tile, xstart, ystart):
    if not isOnBoard(xstart, ystart) or board[xstart][ystart] != EMPTY:
        return False
    board[xstart][ystart] = tile
    otherTile = 'O' if tile == 'X' else 'X'
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
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append((x, y))
    board[xstart][ystart] = EMPTY
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

def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if not tilesToFlip:
        return False
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

# --- AI strategies ---
def getCornerBestMove(board, tile):
    possibleMoves = getValidMoves(board, tile)
    if not possibleMoves:
        return None
    random.shuffle(possibleMoves)
    for x,y in possibleMoves:
        if (x,y) in [(0,0),(0,7),(7,0),(7,7)]:
            return (x,y)
    bestScore = -1; bestMove = None
    for x,y in possibleMoves:
        dupe = getBoardCopy(board)
        makeMove(dupe, tile, x, y)
        score = getScoreOfBoard(dupe)[tile]
        if score > bestScore:
            bestScore = score; bestMove = (x,y)
    return bestMove

def getWorstMove(board, tile):
    possibleMoves = getValidMoves(board, tile)
    if not possibleMoves:
        return None
    worstScore = 10**9; worstMove = None
    for x,y in possibleMoves:
        dupe = getBoardCopy(board)
        makeMove(dupe, tile, x, y)
        score = getScoreOfBoard(dupe)[tile]
        if score < worstScore:
            worstScore = score; worstMove = (x,y)
    return worstMove

def getRandomMove(board, tile):
    possibleMoves = getValidMoves(board, tile)
    if not possibleMoves:
        return None
    return random.choice(possibleMoves)

def getCornerSideBestMove(board, tile):
    possibleMoves = getValidMoves(board, tile)
    if not possibleMoves:
        return None
    random.shuffle(possibleMoves)
    # corners first
    for m in possibleMoves:
        if m in [(0,0),(0,7),(7,0),(7,7)]:
            return m
    # sides next
    sides = [(0,i) for i in range(8)] + [(7,i) for i in range(8)] + [(i,0) for i in range(8)] + [(i,7) for i in range(8)]
    for m in possibleMoves:
        if m in sides:
            return m
    # otherwise best-scoring
    bestScore = -1; bestMove = None
    for x,y in possibleMoves:
        dupe = getBoardCopy(board)
        makeMove(dupe, tile, x, y)
        score = getScoreOfBoard(dupe)[tile]
        if score > bestScore:
            bestScore = score; bestMove = (x,y)
    return bestMove

# Play a single game where AI_X and AI_O are functions that take (board, tile) and return a move
def playGameWithAI(ai_X, ai_O):
    board = getNewBoard()
    resetBoard(board)
    playerTile, computerTile = ['X','O']
    turn = 'computer' if random.randint(0,1) == 0 else 'player'
    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)
        if playerValidMoves == [] and computerValidMoves == []:
            return board
        if turn == 'player':
            if playerValidMoves != []:
                move = ai_X(board, playerTile)
                if move:
                    makeMove(board, playerTile, move[0], move[1])
            turn = 'computer'
        else:
            if computerValidMoves != []:
                move = ai_O(board, computerTile)
                if move:
                    makeMove(board, computerTile, move[0], move[1])
            turn = 'player'

def main():
    NUM_GAMES = 200
    xWins = oWins = ties = 0
    print('AISim3: corner-best (X) vs worst-move (O)')
    for i in range(NUM_GAMES):
        final = playGameWithAI(getCornerBestMove, getWorstMove)
        scores = getScoreOfBoard(final)
        if scores['X'] > scores['O']:
            xWins += 1
        elif scores['X'] < scores['O']:
            oWins += 1
        else:
            ties += 1
    print('X wins: %s (%s%%)' % (xWins, round(xWins / NUM_GAMES * 100, 1)))
    print('O wins: %s (%s%%)' % (oWins, round(oWins / NUM_GAMES * 100, 1)))
    print('Ties:   %s (%s%%)' % (ties, round(ties / NUM_GAMES * 100, 1)))

if __name__ == '__main__':
    main()
