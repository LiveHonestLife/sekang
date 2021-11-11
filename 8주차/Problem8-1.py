n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

coin = sorted(coin, reverse=True)
n = 0
for c in coin:
    n += k//c
    k %= c
    if k == 0:
        break

print(n)

