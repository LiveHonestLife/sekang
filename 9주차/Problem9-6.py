from collections import deque

N, M = map(int, input().split())
number = list(map(int, input().split()))
q = deque([i for i in range(1, N+1)])
cnt = 0
for num in number:
  right = q.index(num)
  left = len(q) - right
  if left > right:
    q.rotate(-right)
  else:
    q.rotate(left)
  cnt += min(left, right)
  q.popleft()

print(cnt)

# https://mong9data.tistory.com/118