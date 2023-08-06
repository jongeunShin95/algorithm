dir = {'up': [0, 1], 'right': [1, 0], 'down': [0, -1], 'left': [-1, 0]}

def solution(keyinput, board):
    answer = []
    lx, ly = board[0] // 2, board[1] // 2
    cx, cy = 0, 0
    
    for key in keyinput:
        dx = cx + dir[key][0]
        dy = cy + dir[key][1]
        
        if dx < -lx or dx > lx or dy < -ly or dy > ly:
            continue
        cx, cy = dx, dy
        
    answer.append(cx)
    answer.append(cy)

    return answer