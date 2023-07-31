import itertools

def e(x1, x2, y1, y2):
    a = (y2 - y1) / (x2 - x1)
    b = (x2 * y1 - x1 * y2) / (x2 - x1)
    return a, b

def solution(dots):
    answer = 0
    nPr = list(itertools.permutations(dots, 4))
    for p in nPr:
        a1, b1 = e(p[0][0], p[1][0], p[0][1], p[1][1])
        a2, b2 = e(p[2][0], p[3][0], p[2][1], p[3][1])
        
        if a1 == a2:
            answer = 1
            break
    
    return answer