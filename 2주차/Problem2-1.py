def solution(lottos, win_nums):
    cnt = 0
    dict = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    joker = lottos.count(0)

    for num in lottos:
        if num in win_nums:
            cnt += 1

    print(joker, cnt)

    if cnt == 0 != joker:
        joker -= 1

    answer = [dict[cnt] - joker, dict[cnt]]

    return answer