def solution(ss):
    result = []



    answer = ss.replace('{', '')
    answer = answer.replace('}}', '},')
    answer = answer.split("},")
    answer.pop(-1)

    #print(answer)

    for s in answer:
      result.append(list(map(int, s.split(','))))

    result = sorted(result, key=len)


    # answer = str(answer).replace('}', '')
    
    # answer = list(map(int, answer)) # map?

    answer = []
    #answer = [o for li in result for o in li if o not in answer]
    
    for li in result:
      for o in li:
        if o not in answer:
          #print(o)
          answer.append(o)

    print(answer)
    print()

    return answer
