import sys
input = sys.stdin.readline

def solve(s):
    flag = True
    lst = set()
    pre = ''
    
    for c in s:
        if pre != c:
            if c in lst:
                flag = False
            else:
                lst.add(c)
        pre = c
    
    return flag

N = int(input())
ans = 0

for i in range(N):
    text = input()
    if solve(text) == True:
        ans += 1

print(ans)