with open("8in.txt") as f:
    lines = [line.replace("|", "").strip().split() for line in f.readlines()]
    combs = {"abcefg":0, "cf":1, "acdeg":2, "acdfg":3, "bcdf":4, "abdfg":5, "abdefg":6, "acf":7, "abcdefg":8, "abcdfg":9}
    tot = 0
    
    for line in lines[0:]:
        # Possible combinations
        nums = [list(x) for x in line]
        to_find = ["".join(x) for x in nums[-4:]]
        
        [x.sort() for x in nums]
        nums = ["".join(x) for x in nums]
        nums = list(set(nums))
        nums.sort(key=len)
        possible = {"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[]}
        used = []
        for entry in nums:
            int_possible = {"a": [], "b": [], "c": [],
                        "d": [], "e": [], "f": [], "g": []}
            if len(entry) in [2,3,4,7]:
                comb = [n for n in combs if len(n) == len(entry)][0]
                for letter in comb:
                    if len(int_possible[letter]) == 0:
                        int_possible[letter] = [x for x in list(entry) if x not in used]
                used.extend(list(entry))
            for k in int_possible:
                if len(possible[k]) == 0:
                    possible[k] = int_possible[k]
        
        
        l = 5
        codes = [x for x in combs if len(x) == l]
        remove = [x for x in possible.keys() if len(possible[x]) == 1]
        remove.extend([x for x in codes[0] if len(
            [y for y in codes if x in y]) == 3])
        for i in range(len(codes)):
            for letter in remove:
                codes[i] = codes[i].replace(letter, "")
        # print(codes)

        entries = [x for x in nums if len(x) == l]
        remove = [x[0] for x in possible.values() if len(x)==1]
        remove.extend([x for x in entries[0] if len([y for y in entries if x in y]) == 3])
        for i in range(len(entries)):
            for letter in remove:
                entries[i] = entries[i].replace(letter, "")
        
        
        # use codes to find all possible permutations
        
        for pos in codes:
            all = []
            for t in possible[pos[0]]:
                for tt in possible[pos[1]]:
                    tmp = list(t+tt)
                    tmp.sort()
                    all.append("".join(tmp))
            # find it in the thingy
            for test in entries:
                if test in all:
                    idx = all.index(test)
            # print(pos, idx)
            if idx == 0 and len(possible[pos[0]]) == 2:
                possible[pos[0]] = [possible[pos[0]][0]]
                possible[pos[1]] = [possible[pos[1]][0]]
            elif idx == 1 and len(possible[pos[0]]) == 2:
                possible[pos[0]] = [possible[pos[0]][0]]
                possible[pos[1]] = [possible[pos[1]][1]]
            elif idx == 2 and len(possible[pos[0]]) == 2:
                possible[pos[0]] = [possible[pos[0]][1]]
                possible[pos[1]] = [possible[pos[1]][0]]
            elif idx == 3 and len(possible[pos[0]]) == 2:
                possible[pos[0]] = [possible[pos[0]][1]]
                possible[pos[1]] = [possible[pos[1]][1]]
        
        for k in possible.values():
            if len(k) == 1:    
                for kk in possible:
                    if len(possible[kk]) != 1:
                        if k[0] in possible[kk]:
                            possible[kk].remove(k[0])

        result = []
        for val in to_find:
            n = ""
            for letter in val:
                for other in possible:
                    if letter in possible[other]:
                        n += other
            result.append(n)
        result = [list(x) for x in result]
        [x.sort() for x in result]
        result = ["".join(x) for x in result]
        result = [str(combs[x]) for x in result]
        tot += int("".join(result))
        

    print(tot)
    
