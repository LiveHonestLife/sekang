# TTTANT
# RRFACC
# RRRFCC
# TRRRAA
# TTMMMF
# TMMTTJ

def solution(row, col, board):  # 0~ row-1, 0~col-1
    answer = 0
    array = []
    block = [[0]*row for _ in range(col)]

    for line in board:
        array.append(list(line))

    for j in range(row - 1, -1, -1):
        for i in range(col):
            block[i][j] = array[row-1-j][i]

    #print(block)

    while True:
        idxlist = []
        for j in range(row - 1, 0, -1):
            for i in range(col-1):
                if block[i][j] == block[i][j-1] == block[i+1][j] == block[i+1][j-1] and block[i][j] != 0:
                    idxlist.append([i, j])
        if len(idxlist) == 0:  # end
            break
        for idx in idxlist:  # change value
            i, j = idx[0], idx[1]

            if block[i][j] != 1:
                block[i][j] = 1
                answer += 1
            if block[i][j-1] != 1:
                block[i][j-1] = 1
                answer += 1
            if block[i+1][j] != 1:
                block[i+1][j] = 1
                answer += 1
            if block[i+1][j-1] != 1:
                block[i+1][j-1] = 1
                answer += 1

        for idx in idxlist:  # sort value
            i, j = idx[0], idx[1]
            l1 = block[i].count(1)
            l2 = block[i+1].count(1)
            for ll in range(l1):
                block[i].remove(1)
                block[i].append(0)
            for ll in range(l2):
                block[i+1].remove(1)
                block[i+1].append(0)

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))