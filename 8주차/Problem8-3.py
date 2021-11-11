n = int(input())

atm = list(map(int, input().split()))

atm.sort()

total = 0

for i in range(len(atm)):
    total += sum(atm[:i+1])

print(total)