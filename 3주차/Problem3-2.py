record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

# "Enter uid1234 Muzi"
# "Enter uid4567 Prodo"
# "Leave uid1234"
# "Enter uid1234 Prodo"
# "Change uid4567 Ryan"

def solution(record):
    answer = []
    logList = []
    dict1 = dict()
    for line in record:
        tmp = line.split()
        if tmp[0] == 'Enter':
            dict1[tmp[1]] = tmp[2]
            logList.append([tmp[1], "님이 들어왔습니다."])
        elif tmp[0] == 'Leave':
            logList.append([tmp[1], "님이 나갔습니다."])
        else:
            dict1[tmp[1]] = tmp[2]
    print(logList)

    for log in logList:
        answer.append(dict1[log[0]]+log[1])

    return answer

print(solution(record))

# 전체를 string으로 접근하는 경우 타임 초과 발생 ?
# 1. dictionary에 user_id & name을 먼저 받고 시작하기
# 2. user_id & name을 같은 반복문에서 받으면서 logList에 user_id & 문장 따로 저장 후 검색