import numpy as np
l = open("16in.txt").readline().strip()
num = bin(int(l, 16))[2:]

# Siden python sløyfer leading zeros...
for _ in range((len(l)*4) - len(num)):
    num = "0"+num
idx = 0
vers = 0

def read_pak():  
    global idx
    global vers
    # Read version - 3 bits
    ver = int(num[idx:idx+3], 2)
    idx+=3
    vers += ver
    # Read type - 3 bits
    t = int(num[idx:idx+3], 2)
    idx+=3
    # print(t)
    # If 4 literal
    if t == 4:
        lit = ""
        while num[idx] == "1": 
            idx += 1
            lit += num[idx:idx+4]
            idx += 4
        idx+=1
        lit += num[idx:idx+4]
        idx += 4
        return int(lit, 2)
    else:
        packs = []
        length = int(num[idx], 2)
        idx += 1
        if length == 0:
            # 15 bit len
            length = int(num[idx:idx+15], 2)
            idx += 15
            # Recurse down while idx < idx+len
            target = idx+length
            while idx < target:
                packs.append(read_pak())
        else:
            n = int(num[idx:idx+11], 2)
            idx += 11
            # Recurse n times
            for _ in range(n):
                packs.append(read_pak())
        if t == 0:
            return sum(packs)
        elif t == 1:
            return np.prod(packs)
        elif t == 2:
            return min(packs)
        elif t == 3:
            return max(packs)
        elif t == 5:
            return int(packs[0] > packs[1])
        elif t == 6:
            return int(packs[0] < packs[1])
        elif t == 7:
            return int(packs[0] == packs[1])
    

print(read_pak())
print(vers)
