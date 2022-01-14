s = "target area: x=20..30, y=-10..-5"[13:]
s = s.split(",")
x_r = [int(x) for x in s[0][2:].split("..")]
y_r = [int(x) for x in s[1][3:].split("..")]
# print(x_r, y_r)


# Factorial up for y speed
# Factorial down per time once at yvel = 0

# ignore x for now


lh = 0
h = []
y = 1
# while too low or inbetween
y_target = [abs(x) for x in y_r]
y_target.sort()
diff = 0

diff = 0
y_max = y_target[1]
# print((y_max)*(((y_max)+1)/2))
# exit()
y = 0 
# positives
while diff <= y_max:
    height = (y+1)*(((y+1)+1)/2)
    diff = height - lh
    tmp = 1
    while diff <= y_target[1]:
        if y_target[0] <= diff:
            h.append((y, tmp*2))
        tmp+=1
        diff += y+tmp
        
    height = (y+1)*(((y+1)+1)/2)
    diff = height - lh
    lh = height
    y += 1
    
for y in range(0, y_max+1):
    pos = y
    y2 = y
    while pos < y_target[0] < y_target[1]:
        y2+=1
        pos += y2
        if pos <= y_target[1]:
            h.append((-y, y2-y))
    if pos <= y_target[1]:
        h.append((-y, y2-y))

x_target = [abs(x) for x in x_r]
x_target.sort()
vels = []
for y in h:
    # Test all x for all y
    for x in range(1, x_target[1]):
        pos = x
        x2 = x
        for _ in range(y[1]):
            x2 -= 1 if x2 > 0 else 0
            pos += x2
        if x_target[0] <= pos <= x_target[1]:
            vels.append((x, y[0]))
vels = set(vels)
print(vels)
print(len(vels))

nv = set()
for v in vels:
    t = 0
    xt=v[0]
    yt=v[1]
    xv = v[0]
    yv = v[1]
    while (0 < xv and not (yt )) and xt <= x_target[1]:
        if x_target[0] <= xt <= x_target[1]:
            if y_target[0] <= yt <= y_target[1]:
                nv.add(v)
                break
        xv -= 1 if xv > 0 else 0
        yv -= 1
        xt += xv 
        yt += yv
print(nv)
print(len(nv))


    # 
    
