def solution(places):
    result = []

    for place in places:
      dis = []
      for line in place:
        dis.append(list(line))

      index_ij = []

      for i in range(5):
        for j in range(5):
          if dis[i][j] == 'P':
            index_ij.append([i,j])
      #print(index_ij)

      k = 1

      for i in range(len(index_ij)):
        for j in range(i+1, len(index_ij)):

          x1 = index_ij[i][0] # 0
          y1 = index_ij[i][1] # 3

          x2 = index_ij[j][0] # 1
          y2 = index_ij[j][1] # 2
          dis_x = abs(x1 - x2)
          dis_y = abs(y1 - y2)

          if dis_x + dis_y < 2: # 거리가 1인 경우
            k = 0
            break

          elif dis_x + dis_y == 2:
            if dis_x == 2: # 열 비교
              if dis[(x1+x2)//2][y1] == 'O':
                k = 0
                break
            elif dis_y == 2: # 행 비교
              if dis[x1][(y1+y2)//2] == 'O':
                k = 0
                break
            else: # 대각선 비교
              if dis[min(x1,x2)][min(y1,y2)] == 'O' or dis[max(x1,x2)][max(y1,y2)] == 'O': # 상승 대각
                k = 0
                break
              elif dis[min(x1,x2)][max(y1,y2)] == 'O' or dis[max(x1,x2)][min(y1,y2)] == 'O': # 하강 대각
                k = 0
                break

          else: # 거리가 3이상
            continue
      result.append(k)

    print(result)
    return result