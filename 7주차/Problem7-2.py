# 최종 코드

# ord() : 파라미터c의 유니코드 int 값을 return
# chr() : int값을 character로 변환할 때

def solution(name):
    answer = 0
    idx = 0
    name = list(name)
    corr = ['A'] * len(name)

    diff_idx = [i for i in range(1, len(name)) if name[i] != 'A']
    left = 0
    right = len(diff_idx)-1
    while True:
        ch = name[idx]
        diff = abs(ord('A') - ord(ch))
        name[idx] = 'A'
        answer += min(diff, 26 - diff)

        if name == corr:
            break

        l = min(abs(idx-(diff_idx[left])), len(name)-abs((idx-diff_idx[left])))
        r = min(abs(idx-(diff_idx[right])), len(name)-abs((idx-diff_idx[right])))
        if l > r: # 뒤로 돌아가는 경우가 빠를 때,
            idx = diff_idx[right]
            right -= 1
            answer += r
        else:
            idx = diff_idx[left]
            left += 1
            answer += l
    return answer

print(solution("JEROEN"))
print(solution("JAN"))
print(solution("BBBAAAB")) #9
print(solution("ABABAAAAABA")) #11
print(solution("ZAAAZZZZZZZ"))

# 초기 아이디어
# def solution(name):
#     answer = 0
#     k = 1  # 순방향
#     idx = 0
#     name = list(name)
#     corr = ['A'] * len(name)

#     if name[1] == 'A':  # 역방향
#         k = -1

#     while True:
#         ch = name[idx]
#         diff = abs(ord('A') - ord(ch))
#         name[idx] = 'A'
#         answer += min(diff, 26 - diff)

#         if name == corr:
#             break
#         if k == 1:
#             idx += 1
#         else:
#             idx -= 1  # (idx-1) % len(name)
#         answer += 1

#     return answer
