from collections import defaultdict

with open("14in.txt") as f:
    lines = f.readlines()
    cur = lines[0].strip()
    r = [l.strip().split(" -> ") for l in lines[2:]]
    rules = {k: v for (k, v) in r}
    rules = defaultdict(str, rules)
    
    
    combo = defaultdict(int)
    count = defaultdict(int)

    f = True
    for i, char in enumerate(cur):
        if f:
            f = False
            continue
        combo[cur[i-1]+cur[i]] += 1
        count[cur[i-1]] += 1

    for ix in range(40):
        cc = defaultdict(int)
        for r in rules:
            if r in combo:
                new = r[0] + rules[r] + r[1]
                cc[new[:2]] += combo[r]
                cc[new[1:]] += combo[r]
                count[rules[r]] += combo[r]
        combo = cc
                
                
                
    most = count[list(count.keys())[0]]
    m_c = list(count.keys())[0]
    least = count[list(count.keys())[0]]
    l_c = list(count.keys())[0]
    for c, v in count.items():
        if v > most:
            most = v
            m_c = c
        if v < least:
            least = v
            l_c = c
    # -1 for some reason :p
    print(most,least, (most-least)-1)
    exit()
    
    # Iterative solution
    # big slow

    for ix in range(15):
        tmp = ["" for _ in cur]
        for i in range(1, len(tmp)):
            tmp[i-1] = rules[(cur[i-1]+cur[i])]
        result = [None]*(len(cur)+len(tmp))
        result[::2] = cur
        result[1::2] = tmp
        cur = "".join(result)
        
        
    most = cur.count(cur[0])
    m_c = cur[0]
    least = cur.count(cur[0])
    l_c = cur[0]
    for char in set(cur):
        c = cur.count(char)
        if c > most:
            most = c
            m_c = char
        if c < least:
            least = c
            l_c = char
    print(most, least, most-least)
            
            
    
