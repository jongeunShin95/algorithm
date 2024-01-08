def solution(str1, str2):
    answer = 0
    str1, str2 = str1.upper(), str2.upper()
    a_list, b_list = [], []
    c1, c2 = [], []

    for i in range(1, len(str1)):
        if (str1[i] >= 'A' and str1[i] <= 'Z') and (str1[i-1] >= 'A' and str1[i-1] <= 'Z'):
            a_list.append(str1[i-1] + str1[i])
    for i in range(1, len(str2)):
        if (str2[i] >= 'A' and str2[i] <= 'Z') and (str2[i-1] >= 'A' and str2[i-1] <= 'Z'):
            b_list.append(str2[i-1] + str2[i])

    # 다중 교집합
    a_temp = a_list.copy()
    for i in b_list:
        if i in a_temp:
            a_temp.remove(i)
            c1.append(i)

    # 다중합집합
    a_temp = a_list.copy()
    c2 = a_list.copy()

    for i in b_list:
        if i not in a_temp: c2.append(i)
        else: a_temp.remove(i)
        
    c1, c2 = len(c1), len(c2)

    if c2 == 0: answer = 65536
    else: answer = int((c1 / c2) * 65536)
    
    return answer