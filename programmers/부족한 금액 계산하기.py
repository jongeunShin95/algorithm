import sys
input = sys.stdin.readline

def solution(price, money, count):
    answer = -1
    temp = 0

    for i in range(1, count + 1):
        temp += price * i

    print(temp)

    answer = temp - money if temp - money > 0 else 0
    return answer

price, money, count = map(int, input().split())

solution(price, money, count)