def x1():
    with open("TXT.txt") as f:
        prev = -1
        i = 0
        for l in f:
            n = int(l)
            if prev < 0:
                prev = n
            else:
                if prev < n:
                    i += 1
                prev = n
        print(i)
        

with open("TXT.txt") as f:
    nums = []  
    i = 0
    lls = f.readlines()
    lls = [int(x) for x in lls] 
    
    ix = 0
    ixx = 1
    while ixx < len(lls):
        if sum(lls[ix:ix+3]) < sum(lls[ixx:ixx+3]):
            i += 1
        
        ix +=1
        ixx +=1
    
    
    print(i)
        