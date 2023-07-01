def solution(A, B):
    B *= 2
    if A in B: return B.find(A)
    else: return -1

print(solution("hello", "ohell"))