import copy
from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    limit = (len(queue1) + len(queue2)) * 2
    if (sum1 + sum2) % 2 != 0:
        answer = -1
        return answer

    while True:
        if sum1 > sum2:
            n = queue1.popleft()
            queue2.append(n)
            sum1 -= n
            sum2 += n
            answer += 1
        elif sum1 < sum2:
            n = queue2.popleft()
            queue1.append(n)
            sum1 += n
            sum2 -= n
            answer += 1
        
        if sum1 == sum2: break
        if answer >= limit:
            answer = -1
            return answer
    return answer