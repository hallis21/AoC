import numpy as np
l = open("16in.txt").readline().strip()
num = bin(int(l, 16))[2:]

for _ in range((len(l)*4)- len(num)):
    num = "0"+num
idx = 0
# num = "11101110000000001101010000001100100000100011000001100000"
vers = []

def read_pak():  
    # Read version - 3 bits
    global idx
    ver = int(num[idx:idx+3], 2)
    idx+=3
    vers.append(ver)
    # Read type - 3 bits
    t = int(num[idx:idx+3], 2)
    idx+=3
    # print(t)
    # If 4 literal
    if t == 4:
        
        lit = ""
        # idx += 1
        # lit += num[idx:idx+4]
        # idx += 4
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
            # print(length)
            target = idx+length
            while idx < target:
                packs.append(read_pak())
            # print(packs)
            # print(idx, target)
        else:
            n = int(num[idx:idx+11], 2)
            idx += 11
            # Recurse n times
            for _ in range(n):
                packs.append(read_pak())
            # print(packs)
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
print(sum(vers))
    
    

# while idx < len(num):
#     # Read version - 3 bits
#     ver = int(num[idx:idx+3], 2)
#     idx += 3
#     # Read type - 3 bits 
#     t = int(num[idx:idx+3], 2)
#     idx+=3
#     if t == 4:
#         pass
#     else:
#         length = int(num[idx],2)
        
#         idx+=1
#         if length == 0:
#             # 15 bit len
#             length = int(num[idx:idx+15], 2)
#             idx += 15
            
#             # store length and operator
#             continue
#             idx += length
            
#             pass
#         else:
#             length = int(num[idx:idx+11], 2)
#             idx += 11
#             pass
    
#     # If 4
#         # 5 * 3 bits
#         # + 3  0-bits
    
#     break
    

