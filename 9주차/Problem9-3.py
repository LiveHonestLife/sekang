n, k = map(int, input().split())

q = [i for i in range(1, n+1)]
idx = k-1
print('<%d' %(q.pop(idx)), end="")
while len(q)!=0:
    idx = (idx + k - 1) % len(q)
    print(",", q.pop(idx), end="")
print(">")
