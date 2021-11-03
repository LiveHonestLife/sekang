# dictionary func 종류, list 만들고 0으로 나눠지는지 ...

N = [5, 4, 5]
stages = [[2, 1, 2, 6, 2, 4, 3, 3], [4,4,4,4,4], [2,2,2,2,2]]

# 실패율 : 스테이지 도달 & 미클리어 / 스테이지 도달
def solution(N, stages):
    array = [0] * (N+2)
    answer = {}

    for i in range(1, N+2):
        array[i] = stages.count(i)
        answer[i] = 0
    for i in range(1, N + 1):
        if sum(array[i:])!=0:
            answer[i] = array[i]/sum(array[i:])
    answer = sorted(answer.items(), key = lambda x: -x[1])
    # 1 3 2 1 0 1 #
    ##
    #
    ##
    ######
    ##
    ####
    ###
    ###
    answer = dict(answer).keys()
    return list(answer)[:-1]

for i in range(3):
    print(solution(N[i], stages[i]))
