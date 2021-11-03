def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)

    #print(participant, completion)
    for idx, comp in enumerate(completion):
        if comp != participant[idx]:
            return participant[idx]
    return participant[-1]
