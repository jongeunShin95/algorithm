import copy

def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for i in range(len(want)): want_dict[want[i]] = number[i]
    
    for i in range(len(discount) - 9):
        f = False
        copy_dict = copy.deepcopy(want_dict)
        
        for j in range(i, i + 10):
            if discount[j] in copy_dict:
                copy_dict[discount[j]] -= 1
        
        for k, v in copy_dict.items():
            if v > 0:
                f = True
                break
        
        if f == False: answer += 1
            
        
        
    return answer