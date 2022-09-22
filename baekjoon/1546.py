import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
max_ = max(lst)
ans = 0

for l in lst:
    ans += l/max_*100
ans = ans / N
print(ans)