def gn(mat, y, x):
    n = []
    if x > 0:
        n.append((y, x-1))
    else:
        n.append((None, None))
    if y > 0:
        n.append((y-1, x))
    if x+1 < len(mat[y]):
        n.append((y, x+1))
    if y+1 < len(mat):
        n.append((y+1, x))
    return n


def gf(mat, y, x, prev):
    ret = {(y, x)}
    n = gn(mat, y, x)
    for i, (l, r) in enumerate(n):
        if i != prev and l and mat[l][r] != 9 and mat[l][r] > mat[y][x]:
            ret |= {(l, r)}
            np = (i + 2) % 4
            ret |= (gf(mat, l, r, np))
    return ret


with open("9in.txt") as f:
    mat = []
    bb = []
    for l in f:
        r = [int(t) for t in l.strip()]
        mat.append(r)
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            n = [mat[i][j] for i, j in gn(mat, y, x) if i]
            if mat[y][x] < min(n):
                bb.append(gf(mat, y, x, -1))
    res = 1
    lens = [len(x) for x in bb]
    for _ in range(3):
        res *= lens.pop(lens.index(max(lens)))
    print(res)
