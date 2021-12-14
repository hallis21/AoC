def pp(maps):
    for l in maps:
        print("".join([str(x) for x in l]))
with open("11in.txt") as f:
    map = []
    res = 0
    for l in f:
        map.append([])
        [map[-1].append(int(s)) for s in l.strip()]
    tot_oct = sum(len(x) for x in map)
    for i in range(0, 1000):
        # Increase all by 1
        map = [[x+1 for x in y] for y in map]
        # Find nines
        bout2pop = [(y, x) for y, l in enumerate(map) for x,v in enumerate(l) if v > 9]
        popped = []    
        # Increase naboer
        while len(bout2pop) > 0:
            for p in bout2pop:
                popped.append(p)
                y,x = p
                yx = [(y-1, x), (y, x-1), (y-1, x-1),(y-1, x+1),
                    (y+1, x), (y, x+1), (y+1, x+1),(y+1, x-1)]
                for y,x in yx:
                    if y >= 0 and x >= 0:
                        try:
                            map[y][x] += 1
                        except:
                            pass
            bout2pop = [(y, x) for y, l in enumerate(map)
                        for x, v in enumerate(l) if v > 9]
            bout2pop = list(set(bout2pop)-set(popped))
        map = [[x if x <= 9 else 0 for x in r] for r in map]
        f = sum([x.count(0) for x in map])
        if f == tot_oct:
            print(i+1)
            break
        res += f
    print(res)