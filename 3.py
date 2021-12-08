with open("bin.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    l3 = lines.copy()
    
    ix = 0
    while len(lines) > 1:
        # find most occurences
        occ = [0 for x in range(len(lines[0]))]
        for i in range(len(lines[0])):
            for line in lines:
                occ[i] += int(line[i])
        mc = ""
        for o in occ:
            mc += "1" if o >= len(lines)/2 else "0"
        # print(mc)
        # mc = int(mc, base=2)
        
        
        # remove non compliant'
        l2 = []
        for line in lines:
            if line[ix] == mc[ix]:
                l2.append(line)
        lines = l2
            
        ix += 1
        
    n1 = int(lines[0], base=2)
    
    lines = l3
    
    ix = 0
    while len(lines) > 1:
        # find most occurences
        occ = [0 for x in range(len(lines[0]))]
        for i in range(len(lines[0])):
            for line in lines:
                occ[i] += int(line[i])
        mc = ""
        for o in occ:
            mc += "1" if o < len(lines)/2 else "0"
        # print(mc)
        # mc = int(mc, base=2)
        
        
        # remove non compliant'
        l2 = []
        for line in lines:
            if line[ix] == mc[ix]:
                l2.append(line)
        lines = l2
            
        ix += 1
        
    n2 = int(lines[0], base=2)
    print(n1*n2)