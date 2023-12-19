import copy

g_score = 0
g_arr = []

def score(arr1, arr2): # arr1 = 어피치, arr2 = 라이언
    a, r = 0, 0
    for i in range(0, 11):
        if arr1[i] == 0 and arr2[i] == 0: continue
        if arr1[i] >= arr2[i]: a = a + (10 - i)
        else: r = r + (10 - i)
    return (r - a)

def dfs(arr1, arr2, c, n):
    global g_score, g_arr 
    if sum(arr2) == n:
        s = score(arr1, arr2)
        if s > 0 and s > g_score:
            g_score = s
            g_arr = copy.deepcopy(arr2)
            return
    if c < 0: return    
    for i in range(n, -1, -1):
        src = arr2[c]
        arr2[c] = i
        if sum(arr2) > n:
            arr2[c] = src
            continue
        dfs(arr1, arr2, c-1, n)
    

def solution(n, info):
    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dfs(info, answer, 10, n)
    answer = g_arr if g_arr != [] else [-1]
    return answer