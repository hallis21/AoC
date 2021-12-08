from typing import DefaultDict


map = DefaultDict(lambda: 0)
with open("lines.txt") as f:
    for line in f:
        ends = [[int(y) for y in x.split(",")] for x in line.split(" -> ")]
        diff = [ends[1][0]-ends[0][0], ends[1][1]- ends[0][1]]
        tmp = [ends[1][0], ends[1][1]]
        
        while sum([abs(x) for x in diff]) > 0:
            map[tuple(tmp)] += 1
            if diff[0] != 0:
                tmp[0] -= 1 if diff[0] > 0 else -1
                diff[0] -= 1 if diff[0] > 0 else -1
            if diff[1] != 0:
                tmp[1] -= 1 if diff[1] > 0 else -1
                diff[1] -= 1 if diff[1] > 0 else -1
        map[tuple(ends[0])] += 1

num = len([x for x in map.values() if x > 1])
print(num)
    
    
