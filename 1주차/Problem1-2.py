def solution(n, arr1, arr2):
    answer = []
    # arr1, arr2 n번씩 나눈 나머지를 arr 배열에 거꾸로 저장
    i = 0

    while i < n:
        j = n - 1
        num1 = arr1[i]
        num2 = arr2[i]
        string = ""

        # print(arr[i])
        while j >= 0:
            if num1 % 2 == num2 % 2 == 0:
                string += ' '
            else:
                string += '#'

            num1 = num1 // 2
            num2 = num2 // 2

            j -= 1
        # print(string)
        answer.append(string[::-1])
        i += 1

    return answer