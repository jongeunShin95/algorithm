import sys
input = sys.stdin.readline

N = input()
cnt = [0] * 10

for i in range(len(N) - 1):
    cnt[int(N[i])] += 1

num = (cnt[6] + cnt[9] + 1) // 2
cnt[6], cnt[9] = num, num

print(max(cnt))