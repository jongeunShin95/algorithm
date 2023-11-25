def solution(bandage, health, attacks):
    answer = 0
    s, f = 0, health
    
    for i in range(1, attacks[-1][0] + 1):
        if attacks[0][0] == i:
            health -= attacks[0][1]
            s = 0
            attacks.pop(0)
            if health < 0: return -1
        else:
            s += 1
            health += bandage[1]
            if s == bandage[0]:
                health += bandage[2]
                s = 0
            if health > f: health = f
    return health if health > 0 else -1
