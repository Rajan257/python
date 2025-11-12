import random
import sys
import math

def drawBoard(board):
    # Draw the game board
    for i in range(60):
        print('-', end='')
    print()
    for row in board:
        for spot in row:
            print(spot, end='')
        print()
    for i in range(60):
        print('-', end='')
    print()

def getNewBoard():
    board = []
    for x in range(60):  # 60 columns
        board.append([])
        for y in range(15):  # 15 rows
            board[x].append(' ')
    return board

def getNewSonarBoard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def isOnBoard(x, y):
    return x >= 0 and x < 60 and y >= 0 and y < 15

def makeMove(board, sonar, x, y):
    if not isOnBoard(x, y):
        return False

    smallestDistance = 100  # Start with large number

    for tx, ty in treasureCoords:
        distance = abs(tx - x) + abs(ty - y)
        if distance < smallestDistance:
            smallestDistance = distance

    if smallestDistance == 0:
        # Treasure found
        treasureCoords.remove([x, y])
        return True
    else:
        if smallestDistance < 10:
            sonar[x][y] = str(smallestDistance)
        else:
            sonar[x][y] = 'O'
        board[x][y] = sonar[x][y]
        return False

def enterPlayerMove():
    print('Enter sonar coordinates (0-59 0-14):')
    while True:
        move = input()
        if len(move) == 3 and move[0].isdigit() and move[2].isdigit() and move[1] == ' ':
            x = int(move[0])
            y = int(move[2])
            if isOnBoard(x, y):
                return x, y
        print('Invalid coordinates. Try again.')

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def showInstructions():
    print('''Instructions:
You are the captain of a treasure hunting ship.
Your goal is to find 3 sunken treasures at sea.
You have sonar devices to detect how close you are.
Enter coordinates like 10 5 to scan that area.
The number you get is the distance to the nearest treasure.
If you get a 0, you found a treasure!
You have 20 sonar devices before you run out.
Good luck!''')

def main():
    print('''Sonar Treasure Hunt
by Al Sweigart
''' )
    showInstructions()

    while True:
        global treasureCoords
        board = getNewBoard()
        sonar = getNewSonarBoard()
        treasureCoords = []

        # Place 3 treasures randomly
        while len(treasureCoords) < 3:
            newX = random.randint(0, 59)
            newY = random.randint(0, 14)
            if [newX, newY] not in treasureCoords:
                treasureCoords.append([newX, newY])

        sonarDevices = 20

        while sonarDevices > 0 and len(treasureCoords) > 0:
            drawBoard(board)
            print(f'Sonar devices left: {sonarDevices}')
            x, y = enterPlayerMove()
            if makeMove(board, sonar, x, y):
                print('You found a sunken treasure!')
            else:
                print('Sonar scan complete.')

            sonarDevices -= 1

        if len(treasureCoords) == 0:
            print('Congratulations! You found all the treasures!')
        else:
            print('Game over! You ran out of sonar devices.')
            print('The remaining treasures were at:')
            for tx, ty in treasureCoords:
                print(f'{tx} {ty}')

        if not playAgain():
            break

if __name__ == '__main__':
    main()
