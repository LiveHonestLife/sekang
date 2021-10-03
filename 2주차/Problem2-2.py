s = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]

def solution(s):
    answer = 0
    num_eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for idx, value in enumerate(num_eng):
        if value in s:
            s = s.replace(value, str(num[idx]))
    answer = int(s)
    return answer

for ss in s:
    print(solution(ss))