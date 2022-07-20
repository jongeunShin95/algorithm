import sys
input = sys.stdin.readline

S = input()
ans = ''

temp_S = ''
flag = False
for c in S:
    if c == '\n': # <-- 엔터 때문에 실패됨
        break
    if c == '<':
        if temp_S != '':
            ans += temp_S[::-1]
            temp_S = ''
        temp_S += c
        flag = True
    elif c == '>':
        temp_S += c
        ans += temp_S
        temp_S = ''
        flag = False
    elif c == ' ' and flag == False:
        ans += temp_S[::-1] + ' '
        temp_S = ''
    else:
        temp_S += c

if temp_S != '':
    ans += temp_S[::-1]

print(ans)