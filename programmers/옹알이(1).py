def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]

    for x in babbling:
        for y in arr:
            x = x.replace(y, " ")
        
        x = x.replace(" ", "")
        if x == "": answer += 1
    return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))