# 재귀 + python

# def convert(n, base):
#     arr = "0123456789ABCDEF"
#     q, r = divmod(n, base)
#     if q == 0:
#         return arr[r]
#     else:
#         return convert(q, base) + arr[r]

# 반복문 + python

def convert(number, base):
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', }

    str1 = ''
    while number > 0:
        r = number % base
        if r in dic:
            r = dic[r]
        str1 += str(r)
        number //= base
    return str1[::-1]


def solution(n, t, m, p):
    answer = ''

    strr = '0'  # 초반 0이 반복문에서 포함이 안되어서 추가
    for i in range(t * m):  # 횟수가 중요 -> 실제 크기는 이것보다 작음
        strr += convert(i, n)

    idx = [(p - 1) + m * i for i in range(t)]

    for id in idx:
        answer += strr[id]

    # print(answer)

    return answer