str = input()
string = ""
flag = 0
number = '0123456789'
tmp = ''
for ch in str:
    if ch in number:
        tmp += ch
    else:
        if ch == '-' and flag == 0: # 열어야 하는 경우
            if tmp == '0':
                string += tmp
            else:
                string += tmp.lstrip('0')
                tmp = ''
            if string.count('(') > string.count(')'):
                string += ')'
            string += ch
            string += '('
            flag = 1

        elif ch == '-' and flag == 1: # 닫아야 하는 경우
            if tmp == '0':
                string += tmp
            else:
                string += tmp.lstrip('0')
                tmp = ''
            string += ')'
            string += ch
            string += '('
            flag = 0

        else: # '+'
            if tmp == '0':
                string += tmp
            else:
                string += tmp.lstrip('0')
                tmp = ''
            string += ch

if tmp == '0':
    string += tmp
else:
    string += tmp.lstrip('0')
    tmp = ''

if string.count('(') > string.count(')'):
    string += ')'

# print(string)
print(eval(string))