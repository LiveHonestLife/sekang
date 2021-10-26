s = ["{{2},{2,1},{2,1,3},{2,1,3,4}}", "{{1,2,3},{2,1},{1,2,4,3},{2}}", "{{20,111},{111}}", "{{123}}", "{{4,2,3},{3},{2,3,4,1},{2,3}}"]

def solution(ss):
    result = []

    print("ss", ss)
    print()

    answer = ss.replace('{', '')
    answer = str(answer).replace('}}', '},')
    answer = answer.split("},")
    answer.pop(-1)

    print("answer", answer)
    print()

    for s in answer:
      result.append(list(map(int, s.split(','))))

    result = sorted(result, key=len)

    print("result", result)
    print()

    answer = []
    #answer = [o for li in result for o in li if o not in answer]
    
    for li in result:
      for o in li:
        if o not in answer:
          answer.append(o)

    print("최종", answer)
    print()
    print()

    return answer

for ss in s:
  solution(ss)
