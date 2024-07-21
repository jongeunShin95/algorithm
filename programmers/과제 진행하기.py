def solution(plans):
    answer = []
    st = []
    
    for plan in plans:
        h, m = plan[1].split(':')
        plan[1] = int(h) * 3600 + int(m) * 60
        plan[2] = int(plan[2]) * 60
    plans = sorted(plans, key=lambda x: x[1])
    t = plans[0][1]
    
    while (len(plans) > 0):
        if plans[0][1] > t:
            if len(st) > 0:
                cur = st.pop()
            else:
                cur = plans.pop(0)
                t = cur[1]
        elif plans[0][1] == t:
            cur = plans.pop(0)
        
        if len(plans) > 0:
            if (t + cur[2]) <= plans[0][1]:
                t += cur[2]
                answer.append(cur[0])
            elif (t + cur[2]) > plans[0][1]:
                cur[2] = cur[2] - (plans[0][1] - t)
                t = plans[0][1]
                st.append(cur)
        else:
            answer.append(cur[0])

    while (len(st) > 0):
        answer.append(st.pop()[0])
    
    return answer