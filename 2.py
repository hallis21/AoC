pos = [0,0,0] 
for l in [x.split() for x in open("up.txt").readlines()]:
    i = 1 if "f" in l[0] else 0
    n = int(l[1])
    pos[1-i] += n if "d" in l[0] else -n
    pos[2] += (pos[1] * n)*i
print(pos[0]*pos[2])