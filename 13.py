with open("13in.txt") as f:
    coords= []
    folds = []
    x,y = (0,0)
    for l in f:
            if "fold" in l:
                folds.append(l.strip()[11:])
            elif l.strip() == "":
                pass
            else:
                s = l.strip().split(",")
                coords.append((int(s[0]), int(s[1])))
                y = coords[-1][1] if coords[-1][1] > y else y
                x = coords[-1][0] if coords[-1][0] > x else x
    map = [[0 for _ in range(x+1)] for _ in range(y+1)]
    for c in coords:
        map[c[1]][c[0]] = 1
    for f in folds:
        if "y" in f:
            tmp = map[int(f[2:])+1:]
            map = map[:int(f[2:])]
            while len(map) > len(tmp):
                tmp.append([0 for _ in map[0]])
            while len(map) < len(tmp):
                t = [[0 for _ in map[0]]]
                t.extend(map)
                map = t
            tmp.reverse()
            for l,_ in enumerate(map):
                map[l] = [(x+y) for (x, y) in zip(tmp[l], map[l])]
        if "x" in f:
            for i,r in enumerate(map):
                tmp = r[int(f[2:])+1:]
                map[i] = r[:int(f[2:])]
                while len(map[i]) > len(tmp):
                    tmp.append(0)
                while len(map[i]) < len(tmp):
                    map[i].insert(0,0)
                tmp.reverse()
                map[i] = [x+y for (x,y) in zip(tmp,map[i])]
        map = [[1 if z > 0 else 0 for z in k] for k in map]
    
    
    print('Part 2:')
    for line in map:
        print(''.join(['█' if x else ' ' for x in line]))
