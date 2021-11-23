from collections import deque
import sys

n = int(input())
q = deque()
for i in range(n):
  cmd = sys.stdin.readline().split()

  if cmd[0] == 'push_front':
    q.appendleft(int(cmd[1]))
  elif cmd[0] == 'push_back':
    q.append(int(cmd[1]))
  elif cmd[0] == 'pop_front':
    print(-1) if len(q) == 0 else print(q.popleft())
  elif cmd[0] == 'pop_back':
    print(-1) if len(q) == 0 else print(q.pop())
  elif cmd[0] == 'size':
    print(len(q))
  elif cmd[0] == 'empty':
    print(1) if len(q) == 0 else print(0)
  elif cmd[0] == 'front':
    print(-1) if len(q) == 0 else print(q[0])
  elif cmd[0] == 'back':
    print(-1) if len(q) == 0 else print(q[-1])