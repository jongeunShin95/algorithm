import math

def h2m(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)
    
def solution(fees, records):
    answer = []
    cars = {}
    times = {}

    for record in records:
        time, number, act = record.split()

        if act == "IN": cars[number] = h2m(time)
        elif act == "OUT":
            if number in times: times[number] += h2m(time) - cars[number]
            else: times[number] = h2m(time) - cars[number]
            del cars[number]

    for number in cars:
        if number in times: times[number] += h2m("23:59") - cars[number]
        else: times[number] = h2m("23:59") - cars[number]

    for (_, value) in sorted(times.items()):
        if fees[0] - value >= 0: answer.append(fees[1])
        else: answer.append(fees[1] + (math.ceil((value - fees[0]) / fees[2]) * fees[3]))
    
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
