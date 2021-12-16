import numpy as np
map = [[int(x) for x in l.strip()] for l in open("15in.txxt")]
for row in map:
    old_row = row[:]
    for i in range(1,5):
        for n in old_row:
            row.append(n+i if n+i < 10 else (n-9)+i)
old_map = map[:]
for i in range(1, 5):
    for row in old_map:
        map.append([x+i if x+i < 10 else (x-9)+i for x in row])


map[0][0] = 0
map = np.array([np.array(x) for x in map])





min_val, max_val = 0, len(map)


#Initialize auxiliary arrays
distmap=np.ones((max_val,max_val),dtype=int)*np.Infinity
distmap[0,0]=0
originmap=np.ones((max_val,max_val),dtype=int)*np.nan
visited=np.zeros((max_val,max_val),dtype=bool)
finished = False
x,y=np.int(0),np.int(0)
count=0

#Loop Dijkstra until reaching the target cell
while not finished:
  if count % 1000 == 0:
      print(count)
  # move to x+1,y
  if x < max_val-1:
    if distmap[x+1,y]>map[x+1,y]+distmap[x,y] and not visited[x+1,y]:
      distmap[x+1,y]=map[x+1,y]+distmap[x,y]
      originmap[x+1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
  # move to x-1,y
  if x>0:
    if distmap[x-1,y]>map[x-1,y]+distmap[x,y] and not visited[x-1,y]:
      distmap[x-1,y]=map[x-1,y]+distmap[x,y]
      originmap[x-1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
  # move to x,y+1
  if y < max_val-1:
    if distmap[x,y+1]>map[x,y+1]+distmap[x,y] and not visited[x,y+1]:
      distmap[x,y+1]=map[x,y+1]+distmap[x,y]
      originmap[x,y+1]=np.ravel_multi_index([x,y], (max_val,max_val))
  # move to x,y-1
  if y>0:
    if distmap[x,y-1]>map[x,y-1]+distmap[x,y] and not visited[x,y-1]:
      distmap[x,y-1]=map[x,y-1]+distmap[x,y]
      originmap[x,y-1]=np.ravel_multi_index([x,y], (max_val,max_val))

  visited[x,y]=True
  dismaptemp=distmap
  dismaptemp[np.where(visited)]=np.Infinity
  # now we find the shortest path so far
  minpost=np.unravel_index(np.argmin(dismaptemp),np.shape(dismaptemp))
  x,y=minpost[0],minpost[1]
  if x==max_val-1 and y==max_val-1:
    finished=True
  count=count+1
#   print(len(np.where(visited)))
print(count)



print('The path length is: '+np.str(distmap[max_val-1,max_val-1]))
# print('The dump/mean path should have been: '+np.str(maxnum*max_val))
