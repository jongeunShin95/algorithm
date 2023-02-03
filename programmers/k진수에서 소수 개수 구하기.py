import string, math

tmp = string.digits
def convert(n, k):
    q, r = divmod(n, k)
    if q == 0: return tmp[r] 
    else: return convert(q, k) + tmp[r]

def prime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def solution(n, k):
    answer = 0
    converted = convert(n, k)
    converted = converted.split('0')
    
    for c in converted:
        if c == '' or c == '1': continue
        if prime(int(c)): answer += 1
    
    return answer

print(solution(437674, 3))