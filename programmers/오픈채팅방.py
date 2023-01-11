def solution(record):
    answer = []
    users = []
    nicknames = {}
    
    for r in record:
        user = r.split()
        if len(user) == 3: nicknames[user[1]] = user[2]
        users.append([user[0], user[1]])

    for user in users:
        if user[0] == 'Enter': answer.append("%s님이 들어왔습니다." % nicknames[user[1]])
        elif user[0] == 'Leave': answer.append("%s님이 나갔습니다." % nicknames[user[1]])
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))