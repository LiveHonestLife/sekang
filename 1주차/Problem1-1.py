def solution(dartlist):
    score = 0
    idx = 0
    tmplist = [0] * 3
    j = 0

    while idx < len(dartlist):

        if dartlist[idx] >= '0' and dartlist[idx] <= '9':
            if dartlist[idx + 1] == '0':
                tmp = 10
                idx += 1
            else:
                tmp = int(dartlist[idx])
            idx += 1

            if dartlist[idx] == 'S':
                tmp = tmp ** 1
            elif dartlist[idx] == 'D':
                tmp = tmp ** 2
            elif dartlist[idx] == 'T':
                tmp = tmp ** 3
            idx += 1

            tmplist[j] += tmp
            j += 1
            # print(tmplist)

        elif dartlist[idx] == '*':
            tmplist[j - 2] *= 2
            tmplist[j - 1] *= 2
            idx += 1

        else:
            if dartlist[idx] == '#':
                tmplist[j - 1] *= -1
                idx += 1

    answer = tmplist[0] + tmplist[1] + tmplist[2]

    return answer