map = [[int(x) for x in l.strip()] for l in open("15in.txxt")]
m = sum([sum(x) for x in map])
visted = [[False for x in y] for y in map]
scores = [[m for x in y] for y in map]

# DFS, probably too slow

# 0 left, 1 up, 2 right, 3 down (came from)
def to_right(x,y,dir, score):
    if visted[y][x]:
        return
    visted[y][x] = True
    scores[y][x] = min(score, scores[y][x])
    
    
    n = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    for i in range(4):
        try:
            if i != dir and min(n[i]) >= 0:
                to_right(*n[i], (i+2) % 4, score+map[y][x])
        except:
            pass
    
    visted[y][x] = False


