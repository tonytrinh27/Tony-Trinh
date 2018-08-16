import reversi as bo
from random import randint


def creatboard(board):
    for i in bo.board:
        print(" ".join(i))


def pointInput(inputs):
    r = 0
    c = 0
    if inputs[0] in bo.dir.keys():
        r = int(bo.dir[inputs[0]])
        c = int(inputs[1])
    return r, c


def onBoard(x, y):
    return x >= 1 and x < 9 and y >= 1 and y < 9


def getplayer(player):
    getlist = []
    for i in range(1,9):
        for j in range(1,9):
            if bo.board[i][j] == player:
                getlist.append([i, j])
    return getlist


def valid_choose(player):
    possible = []

    # Get all position of player now in board
    a = getplayer(player)

    # Make a opponnent
    if player == "B":
        opponnent = "W"
    else:
        opponnent = "B"


    # Check each location player
    for i in a:
        c = i[0]
        h = i[1]
        for u in bo.direct:
            x, y = c, h
            y += u[0]
            x += u[1]
            if onBoard(x, y):
                if bo.board[y][x] == opponnent:
                    while 1 <= y + u[0] <= 8 and 1 <= x + u[1] <= 8:
                        if bo.board[y + u[0]][x + u[1]] == opponnent:
                            y += u[0]
                            x += u[1]
                        elif bo.board[y + u[0]][x + u[1]] == player:
                            break
                        elif bo.board[y + u[0]][x + u[1]] == '.':
                            possible.append([y + u[0], x + u[1]])
                            break
    return possible
    # list_Dot = []
    # if player == "B":
    #     elplayer = "W"
    # else:
    #     elplayer = "B"
    # for i in getplayer(player):
    #     h = i[0]
    #     c = i[1]
    #     for rec in bo.direct:
    #         x, y = h, c
    #         y += rec[1]
    #         x += rec[0]
    #         if bo.board[x][y] == elplayer:
    #             while True:
    #                 y += rec[1]
    #                 x += rec[0]
    #                 print(bo.board[x][y])
    #                 print(player)
    #                 if not onBoard(x, y):
    #                     break
    #                 elif bo.board[x][y] == '.':
    #                     print("ok")
    #                 elif bo.board[x][y] == elplayer:
    #                     print('f**k')
    #                 else:
    #                     print('poot')
                        # y += rec[1]
                        # x += rec[0]
                        # print(elplayer)
                        # if a == elplayer:
                            # print("ok")
                            # break
            #                 print(elplayer)
            #                 print(bo.board[x+rec[0]][y+rec[1]])
                            # x += rec[0]
                            # y += rec[1]
                        # elif a == player:
                            # print("ok")
            #                 print(bo.board[x+rec[0]][y+rec[1]])
                            # break
                        # break
                        # elif a == ".":
                            # print(bo.board[x + rec[0]][y + rec[1]])
                            # list_Dot.append([x + rec[0], y + rec[1]])
                            # print(list_Dot)
                            # break
    return list_Dot


def outValid(player):
    valid = []
    # print(valid_choose(player))
    for i in valid_choose(player):
        for key, val in bo.dir.items():
            if i[0] == val:
                valid.append(key+str(i[1]))
    print("Valid choices: " + ' '.join(set(valid)))


def flip(player, playerInput):
    if player == "B":
        elplayer = "W"
    else:
        elplayer = "B"
    r, c = pointInput(playerInput)
    bo.board[c][r] = player
    for rec in bo.direct:
        x, y = r, c
        x += rec[0]
        y += rec[1]
        if onBoard(x, y):
            if bo.board[y][x] == elplayer and onBoard(x+rec[0], y+rec[1]):
                if bo.board[y+rec[1]][x+rec[0]] == player:
                    bo.board[y][x] = player
                elif bo.board[y+rec[1]][x+rec[0]] == elplayer:
                    bo.board[y][x] = player
                    while 1 <= x + rec[0] <= 8 and 1 <= y + rec[1] <= 8:
                        if bo.board[y+rec[1]][x+rec[0]] == elplayer:
                            bo.board[y+rec[1]][x+rec[0]] = player
                        else:
                            break

#
while 1:
    creatboard(bo.board)
    outValid("W")
    playerW = input("Player W: ")
    flip("W", playerW)


    creatboard(bo.board)
    outValid("B")
    playerB = input("Player B: ")
    flip("B", playerB)

# while 1:
#     creatboard(bo.board)
#     # valid_choice_W = outValid("W").split(" ")
#     outValid("W")
#     # playerW = input("Player W: ")
#     print("Player W: ",end='')
#     rad = randint(0, len(valid_choose('W')) -1)
#     playerW = valid_choose('W')[rad]
#     # print(playerW)
#
#     # valid_choose("W")
#     # getplayer("W")
#     outValid('W')
#     # pointInput(playerW)
#     flip("W", playerW)
#     chr, Elchr = playerChr("W")
#     pointChoose(playerW, chr)
#
#     creatboard(bo.board)
#     # valid_choice_B = outValid("B").split(" ")
#     outValid("B")
#     # playerB = input("Player B: ")
#     print("Player B: ",end='')
#     rad = randint(0, len(valid_choose('B')) -1)
#     playerB = valid_choose('B')[rad]
#
#     # valid_choose("B")
#     # getplayer("B")
#     # pointInput(playerB)
#     outValid('B')
#     flip("W", playerB)
#     chr, Elchr = playerChr("W")
#     pointChoose(playerB, chr)
