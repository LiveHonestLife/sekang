from collections import deque

N = int(input())

for i in range(N):
    p = input()
    n = int(input())
    arr = input()
    flag = 0
    cheak = 0

    if arr == '[]':
        q = deque()
    else:
        q = deque(list(map(int, arr[1:-1].split(','))))

    for ch in p:
        if ch == 'R':
            flag += 1

        else:
            if n == 0:
                cheak = 1
                print("error")
                break
            q.pop() if flag % 2 == 1 else q.popleft()
            n -= 1

    if cheak == 0:
        print('[', end="")
        if flag % 2 == 1:  # reverse
            for j in range(n - 1, -1, -1):
                print(q[j], end="")
                if j != 0:
                    print(',', end="")
        else:
            for j in range(n):
                print(q[j], end="")
                if j != n - 1:
                    print(',', end="")
        print(']')