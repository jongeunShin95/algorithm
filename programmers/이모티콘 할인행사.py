result = [0, 0]
cur_price = []
rate = []

def dfs(users, cur, price, total):
    global cur_price, rate, result
    if cur >= total:
        temp_result = [0, 0]
        for user in users:
            temp_price = 0
            for i in range(0, total):
                if user[0] <= rate[i]: temp_price += cur_price[i]
            if user[1] <= temp_price: temp_result[0] += 1
            else: temp_result[1] += temp_price
        
        if temp_result[0] > result[0]:
            result[0], result[1] = temp_result[0], temp_result[1]
        elif temp_result[0] == result[0]:
            result[1] = temp_result[1] if temp_result[1] > result[1] else result[1]
        return
        
    for i in range(0, 4):
        cur_price[cur] = price[cur][i]
        rate[cur] = (i + 1) * 10
        dfs(users, cur+1, price, total)
        

def solution(users, emoticons):
    answer, price = [], []
    global cur_price, rate
    for _ in range(len(emoticons)): 
        cur_price.append(0)
        rate.append(0)
    
    for emoticon in emoticons:
        t, i = [], 0.1
        while i < 0.5:
            t.append(emoticon - int(emoticon * i))
            i += 0.1
        price.append(t)
    print(price)
        
    dfs(users, 0, price, len(price))
    answer = result
        
    return answer