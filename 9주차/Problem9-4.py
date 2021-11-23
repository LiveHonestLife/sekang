from collections import deque

n = int(input())

for i in range(n):
  # N : 개수, M : index
  N, M = map(int, input().split())
  q = deque(list(map(int, input().split())))
  cnt = 0
  while True:
    if q[0] != max(q):
      q.rotate(-1)
      M = (M-1) % N
    else:
      cnt += 1
      if M == 0:
        print(cnt)
        break
      q[0] = 0