def valid_solution(board):
    for i in board:
        for j in i:
            if i.count(j) == 1 and j != 0:
                continue
            else:
                return False
    for i in list(zip(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])):
        for j in i:
            if i.count(j) == 1 and j != 0:
                continue
            else:
                return False
    k1, k2, k3 = 0, 0, 0
    for o in range(0, 9, 3):
        for h in range(0, 9, 3):
            k1 = 0
            for i in range(0 + h, 3 + h):
                k1 = k1 + sum(board[i][(0 + o):(3 + o)])
            if k1 != 45:
                return False
    return True


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 0, 3, 4, 9],
                      [1, 0, 0, 3, 4, 2, 5, 6, 0],
                      [8, 5, 9, 7, 6, 1, 0, 2, 0],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 0, 1, 5, 3, 7, 2, 1, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 0, 0, 4, 8, 1, 1, 7, 9]]))
