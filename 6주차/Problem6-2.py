def solution(people, limit):
    answer = 0
    left = 0
    right = len(people)-1
    people.sort()

    while left < right:

      if len(people) == 0:
        answer += 1
        continue

      if people[left] + people[right] <= limit:
        left += 1
        right -= 1
        answer += 1

      else:
        right -= 1
        answer += 1

      if left == right:
        answer += 1

      print(left, right, answer)

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))