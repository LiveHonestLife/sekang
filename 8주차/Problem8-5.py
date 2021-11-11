n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

oil_price = price[0]
total = 0

start = 0
end = 0

for i in range(0, len(price)):

    if i == len(price)-1:
        total += oil_price * sum(road[start:end+1])
        break

    if price[i] < oil_price: # 이전 거리까지 정산
        total += oil_price * sum(road[start:end+1])
        oil_price = price[i]
        start = end + 1
        end = start

    else: # 지나치는 경우
         end = i

print(total)