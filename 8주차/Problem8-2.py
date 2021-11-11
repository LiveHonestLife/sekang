import heapq

heap = []

n = int(input())

for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(heap, [e, s])

start = 0
answer = 0

while heap:
    e, s = heapq.heappop(heap)
    if s >= start:
        start = e
        answer += 1
        # print(start)

print(answer)