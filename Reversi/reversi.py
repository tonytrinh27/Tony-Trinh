board = [[' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
         ['1', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['2', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['3', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['4', '.', '.', '.', 'W', 'B', '.', '.', '.'],
         ['5', '.', '.', '.', 'B', 'W', '.', '.', '.'],
         ['6', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['7', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['8', '.', '.', '.', '.', '.', '.', '.', '.']]

board[4][4] = 'W'
board[4][5] = 'B'
board[5][4] = 'B'
board[5][5] = 'W'


dir = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
direct= [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]