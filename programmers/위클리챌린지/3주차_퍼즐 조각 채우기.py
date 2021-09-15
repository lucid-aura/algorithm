################################## 퍼즐 조각 채우기 ###################################
import copy

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
#game_board = [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
#table = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]

def solution(game_board, table):
    def rotate(table, length):
        rotate_table = copy.deepcopy(table)
        for i in range(length):
            for j in range(length):
                rotate_table[j][length - i - 1] = table[i][j]
        return rotate_table

    answer = 0
    length = len(game_board[0])
    for i in range(length):
        for j in range(length):
            table[i][j] = 1-table[i][j]


    def ishole(i, j, board, block):
        board[i][j] = 1
        block.append([i,j])
        if j < length-1:
            if board[i][j+1] == 0:
                ishole(i, j+1, board, block)
        if j > 0:
            if board[i][j-1] == 0:
                ishole(i, j-1, board, block)
        if i < length-1:
            if board[i+1][j] == 0:
                ishole(i+1, j, board, block)
        if i > 0:
            if board[i-1][j] == 0:
                ishole(i-1, j, board, block)
        return 0

    # resize
    def resize(holes):
        for i in holes:
            x = i[0][0]
            y = i[0][1]
            for j in i:
                j[0] = j[0] - x
                j[1] = j[1] - y

    def task(game_board, table, answer):
        origin_board = copy.deepcopy(game_board)
        origin_table = copy.deepcopy(table)

        # find board hole 
        holes = list()
        for i in range(length):
            for j in range(length):
                if game_board[i][j] == 0:
                    hole = list()
                    ishole(i, j, game_board, hole)
                    holes.append(hole)

        origin_hole = copy.deepcopy(holes)
        resize(holes)

        # find block
        blocks = list()
        for i in range(length):
            for j in range(length):
                if table[i][j] == 0:
                    block = list()
                    ishole(i, j, table, block)
                    blocks.append(block)

        # compare block and hole
        block_number = []
        hole_number = []
        origin_block = copy.deepcopy(blocks)
        resize(blocks)
        for i in range(len(holes)):
            for j in range(len(blocks)):
                if holes[i] == blocks[j] and j not in block_number and i not in hole_number:
                    block_number.append(j)
                    hole_number.append(i)

        # remove holes
        for i in hole_number:
            for j in origin_hole[i]:
                origin_board[j[0]][j[1]] = 1
                answer += 1

        # remove blocks
        for i in block_number:
            for j in origin_block[i]:
                origin_table[j[0]][j[1]] = 1


        # update board and table
        game_board = origin_board
        table = origin_table
        return game_board, table, answer

    # task1 - 0 degree
    game_board, table, answer = task(game_board, table, answer)

    # rotate table
    table = rotate(table, length)

    # task2 - 90 degree
    game_board, table, answer = task(game_board, table, answer)

    # rotate table
    table = rotate(table, length)

    # task3 - 180 degree
    game_board, table, answer = task(game_board, table, answer)

    # rotate table
    table = rotate(table, length)

    # task4 - 270 degree
    game_board, table, answer = task(game_board, table, answer)
    return answer