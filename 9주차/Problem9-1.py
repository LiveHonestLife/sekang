from collections import deque
import sys

n = int(input())
length = 0
q = deque(maxlen=n)
for i in range(n):
  str = sys.stdin.readline().split()
  if str[0] == 'push':
    q.append(int(str[1]))
    length += 1

  elif str[0] == 'pop':
    if length == 0:
      print(-1)
    else:
      print(q.popleft())
      length -= 1

  elif str[0] == 'size':
    print(length)

  elif str[0] == 'empty':
    if length == 0:
      print(1)
    else:
      print(0)

  elif str[0] == 'front':
    if length == 0:
      print(-1)
    else:
      print(q[0])

  elif str[0] == 'back':
    if length == 0:
      print(-1)
    else:
      print(q[-1])