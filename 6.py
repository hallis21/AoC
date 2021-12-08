f = open("lant.txt", "r")
l = f.readline().strip().split(",")
lines = [int(t) for t in l]


# Denne er ikke min, tror jeg overskrev den når jeg teste denne :/
def fishy(a):
    fiskBarn = {}
    navn = ""

    for i in lines:
        navn += "a"
        fiskBarn[navn] = [1, i]
        
    dag = 0
    while dag < a:
        tmp = {}
        for i in fiskBarn:
            if fiskBarn[i][1] == 0:
                fiskBarn[i][1] = 6
                if tmp.get(dag) == None:
                    tmp[dag] = [fiskBarn[i][0], 8]
                else:
                    verdi = tmp[dag][0]
                    tmp[dag][0] = fiskBarn[i][0] + verdi
            else:
                fiskBarn[i][1] -=1
        for j in tmp:
            fiskBarn[dag] = tmp.get(j)
        dag += 1
    antall = 0
    for i in fiskBarn:
        v = fiskBarn.get(i)
        antall += v[0]

    return antall

print(fishy(80))
print(fishy(256))