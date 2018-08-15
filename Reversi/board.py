import reversi as bo


def creatboard(board):
    for i in bo.board:
        print(" ".join(i))


def playerChr(inputPlayer):
    chr = ""
    Elchr = ""
    if inputPlayer == "B":
        Elchr += "W"
        chr += "B"
    else:
        Elchr += "B"
        chr += "W"
    return chr, Elchr


def pointChoose(inputs, chr):
    if inputs[0] in bo.dir.keys():
        row = int(bo.dir[inputs[0]])
        col = int(inputs[1])
    if bo.board[col][row] == ".":
        bo.board[col][row] = chr


def onBoard(x, y):
    return x >= 1 and x < 9 and y >= 1 and y < 9


def getplayer():
    getlist = []
    for i in range(1,9):
        for j in range(1,9):
            if bo.board[i][j] == "B":
                getlist.append([j, i])
            elif bo.board[i][j] == "W":
                getlist.append([j, i])
    return getlist


def valid_choose(player):
    for i in getplayer():
        x = i[0]
        y = i[1]
        bo.board[x][y]
    if player == "W":
        elplayer = "B"
    else:
        elplayer = "W"
    replace_list = []
    list_Dot = []
    valid = set([])
    for r, c in bo.direct:
        x += c
        y += r
        if onBoard(x, y) and bo.board[x][y] == elplayer:
            x += c
            y += r
            if not onBoard(x, y):
                continue
            if bo.board[x][y] == ".":
                list_Dot.append([x, y])
            while bo.board[x][y] == elplayer:
                x += c
                y += r
                if not onBoard(x, y):
                    break
            if bo.board[x][y] == player:
                while True:
                    x -= c
                    y -= r
                    if x == i[0] and y == i[1]:
                        break
                    replace_list.append([x, y])
        if onBoard(x, y) and bo.board[y][x] == ".":
            list_Dot.append([x, y])
        if onBoard(x, y) and bo.board[y][x] == player:
            break
    for i in list_Dot:
        for key, val in bo.dir.items():
            if i[0] == val:
                valid.add(key+str(i[1]))


    return ' '.join(valid), replace_list


valid, replace = valid_choose("W")


def flip(rep, chr):
    for i in rep:
        print(i)
        bo.board[i[0]][i[1]] = player


while 1:
    creatboard(bo.board)
    print("Valid choices: ",valid)
    playerW = input("Player W: ")
    valid_choose("W")
    flip(replace, "W")
    chr, Elchr = playerChr(playerW)
    pointChoose(playerW, chr)

    creatboard(bo.board)
    print("Valid choices: ",valid)
    playerB = input("Player B: ")
    valid_choose("B")
    flip(replace, "B")
    chr, Elchr = playerChr(playerB)
    pointChoose(playerB, Elchr)
