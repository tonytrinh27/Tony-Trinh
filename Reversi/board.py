# from random import randint


board = [[' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
         ['1', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['2', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['3', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['4', '.', '.', '.', 'W', 'B', '.', '.', '.'],
         ['5', '.', '.', '.', 'B', 'W', '.', '.', '.'],
         ['6', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['7', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['8', '.', '.', '.', '.', '.', '.', '.', '.']]


dir = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
direct= [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]


# create board
def creatboard(board):
    for i in board:
        print(" ".join(i))


# change player inputs from string to (x , y)
def pointInput(inputs):
    if inputs[0] in dir.keys():
        r = int(dir[inputs[0]])
        c = int(inputs[1])
    return c, r


# check limited in board
def onBoard(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8


# search for the location of the player in the board
def getplayer(player):
    getlist = []
    for i in range(1,9):
        for j in range(1,9):
            if board[i][j] == player:
                getlist.append([j, i])
    return getlist


# check location player can go
def valid_choose(player):
    possible = []
    a = getplayer(player)
    if player == "B":
        opponnent = "W"
    else:
        opponnent = "B"
    for i in a:
        c = i[0]
        h = i[1]
        for u in direct:
            x, y = c, h
            y += u[1]
            x += u[0]
            if onBoard(x, y):
                if board[y][x] == opponnent:
                    while 1 <= y + u[1] <= 8 and 1 <= x + u[0] <= 8:
                        if board[y + u[1]][x + u[0]] == opponnent:
                            y += u[1]
                            x += u[0]
                        elif board[y + u[1]][x + u[0]] == player:
                            break
                        elif board[y + u[1]][x + u[0]] == '.':
                            possible.append([x + u[0], y + u[1]])
                            break
    return possible


# Output valid_choose list
def outValid(player):
    valid = []
    for i in valid_choose(player):
        valid.append(get_location(i[0], i[1]))
    print("Valid choices: " + ' '.join(sorted(set(valid))))


# used to check the player in next positions
def check_line(x,y,x_move,y_move, elplayer, player):
    while 1 <= x + x_move <= 8 and 1 <= y + y_move <= 8:
        if board[y + y_move][x + x_move] == elplayer:
            x += x_move
            y += y_move
        elif board[y + y_move][x + x_move] == player:
            return True
        else:
            return False


# Used to flip elplayer
def flip(player, playerInput):
    if player == "B":
        elplayer = "W"
    else:
        elplayer = "B"
    r, c = pointInput(playerInput)
    board[r][c] = player
    for rec in direct:
        x, y = c, r
        x += rec[0]
        y += rec[1]
        if onBoard(x, y):
            if board[y][x] == elplayer and onBoard(x + rec[0], y + rec[1]):
                if board[y + rec[1]][x + rec[0]] == player:
                    board[y][x] = player
                elif board[y + rec[1]][x + rec[0]] == elplayer:
                    if check_line(x, y , rec[0], rec[1], elplayer, player):
                        board[y][x] = player
                        while 1 <= x + rec[0] <= 8 and 1 <= y + rec[1] <= 8:
                            if board[y + rec[1]][x + rec[0]] == elplayer:
                                board[y + rec[1]][x + rec[0]] = player
                                x += rec[0]
                                y += rec[1]
                            else:
                                break


# used to check location input player
def get_location(x, y):
    return board[0][x] + board[y][0]


# Used to check for dots
def check_dot():
    for i in range(1,9):
        for j in range(1,9):
            if board[i][j] == ".":
                return True
    return False


# Used to calculate points
def score():
    scoreW = 0
    scoreB = 0
    for i in range(1,9):
        for j in range(1,9):
            if board[i][j] == "W":
                scoreW += 1
            if board[i][j] == "B":
                scoreB += 1
    if scoreB > scoreW:
        print("End of the game. W: {}, B: {}".format(scoreW, scoreB))
        print("B wins.")
    elif scoreB < scoreW:
        print("End of the game. W: {}, B: {}".format(scoreW, scoreB))
        print("W wins.")
    else:
        print("End of the game. W: {}, B: {}".format(scoreW, scoreB))
        print("Draw.")


end = True
game = True


while check_dot():
    # player B Input
    creatboard(board)
    outValid("B")
    arr1 = []
    for j in valid_choose('B'):
        arr1.append(get_location(j[0], j[1]))
    if arr1 == []:
        print("Player B cannot play.")
        score()
        game = False
        break
    arr1.sort()
    playerB = input("Player B: ")
    # rad1 = randint(0, len(arr1) - 1)
    # playerB = arr1[rad1]
    # print(playerB)
    while playerB not in arr1:
        print(playerB + ': Invalid choice')
        outValid("B")
        playerB = input("Player B: ")
    flip("B", playerB)
        # playerB = arr1[rad1]


    # player W Input
    creatboard(board)
    outValid("W")
    arr = []
    for i in valid_choose('W'):
        arr.append(get_location(i[0], i[1]))
    if arr == []:
        print("Player W cannot play.")
        score()
        game = False
        break
    arr.sort()
    # rad = randint(0, len(arr) - 1)
    # playerW = arr[rad]
    # print(playerW)
    # print(sorted(arr))
    playerW = input("Player W: ")
    while playerW not in arr:
        print(playerW + ': Invalid choice')
        outValid("W")
        playerW = input("Player W: ")
        # playerW = arr[rad]
    flip("W", playerW)
# when game End
if game:
    creatboard(board)
    score()
