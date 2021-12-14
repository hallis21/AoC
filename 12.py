class Cave:
    def __init__(self,name) -> None:
        self.name = name
        self.small = name.islower()
        self.visited = 0
        self.connections = []
        
    def add_c(self, other):
        other.connections.append(self)
        self.connections.append(other)
    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name
    
    
    def walk(self, dob, st):
        if self.name == "end":
            return {st+"end"}
        if self.small and self.visited > 0:
            return {None}
        if self.name == "start":
            self.visited = 1
        y = set()
        if self.small and not dob:
            # self.visited = 1
            for n in self.connections:
                y.update(n.walk(True, st+self.name))
            
        self.visited = 1
        for n in self.connections:
            y.update(n.walk(dob, st+self.name))
        self.visited = 0
        return y


with open("12in.txt") as f:
    routes = [[Cave(n) for n in l.strip().split("-")]for l in f]
    caves = []
    for r in routes:
        if r[0] not in caves:
            caves.append(r[0])
        if r[1] not in caves:
            caves.append(r[1])
        caves[caves.index(r[0])].add_c(caves[caves.index(r[1])])
    
    start = [x for x in caves if x.name == "start"][0]
    print(len(start.walk(False, ""))-1)
    

    
