with open("7in.txt") as f:
    pos = [int(x) for x in f.readline().split(",")]
    tots = []
    for num in range(0, max(pos)):
        tot = 0
        for n in pos:
            diff = abs(num-n)
            tot  += (diff*(diff+1))/2
        tots.append(tot)
    print(min(tots))
        
        
        
