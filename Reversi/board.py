import reversi as bo

player = "W"

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
    return x >= 0 and x <= 9 and y >= 0 and y <= 9


def valid_choose(player):
    if player == "W":
        elplayer = 'B'
    else:
        elplayer = "W"

    list_Dot = []

    for j in range(1, 9):
        for i in range(1, 9):
            if onBoard(j, i) and bo.board[i][j] == player:
                for r, c in bo.direct:
                    j += r
                    i += c
                    if not onBoard(j, i):
                        continue
                    if bo.board[i][j] == elplayer:
                        j += r
                        i += c
                        if bo.board[i][j] == player:
                            break
                    if not onBoard(j, i):
                        continue
                    if bo.board[i][j] == player:
                        break
                    if bo.board[i][j] == ".":
                        list_Dot.append([j,i])
    return list_Dot

a = valid_choose(player)

def point(a):
    valid = set([])
    for i in a:
        for key, val in bo.dir.items():
            if i[0] == val:
                valid.add(key+str(i[1]))
    return valid


while 1:
    creatboard(bo.board)
    print("Valid choices: ", point(a))
    playerW = input("Player W: ")
    valid_choose(playerW)
    chr, Elchr = playerChr(playerW)
    pointChoose(playerW, chr)

    creatboard(bo.board)
    print("Valid choices: ", point(a))
    playerB = input("Player B: ")
    valid_choose(playerB)
    chr, Elchr = playerChr(playerB)
    pointChoose(playerB, Elchr)
