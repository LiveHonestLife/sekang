nums = [3,3,3,2,2,2]

def solution(nums):
    choice = len(nums)//2
    answer = max_class = len(set(nums))
    if choice <= max_class:
        answer = choice

    return answer

print(solution(nums))
