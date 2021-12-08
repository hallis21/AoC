class Num:
    def __init__(self, n) -> None:
        self.n = n
        self.marked = False
        
class Board:
    def __init__(self) -> None:
        self.board = [[] for x in range(5)]
        self.len = 0
        self.last = 0
        self.won = False
    
    def add_num(self, num):
        if len(self.board[self.len]) >= 5:
            self.len += 1
        self.board[self.len].append(Num(num))
        
    def mark(self, num):
        for r in self.board:
            for n in r:
                if n.n == num:
                    n.marked = True
        self.last = num
        return self.check_win()
        
    def check_win(self):
        for r in self.board:
            if len([x for x in r if x.marked == True]) == 5:
                return True
        tmp = list(zip(*self.board[::-1]))
        for r in tmp:
            if len([x for x in r if x.marked == True]) == 5:
                return True   
        return False
    
    def score(self):
        l = []
        for r in self.board:
            [l.append(n.n) for n in r if not n.marked]    
        return sum(l)*self.last

    def marked(self):
        return '\n'.join([str([x.draw() for x in y]) for y in self.board])
    def __str__(self) -> str:
        return '\n'.join([str([x.n for x in y]) for y in self.board])
        

class Game:
    def __init__(self) -> None:
        self.boards = [] 
        self.nums = []
    
    def add_num(self, num):
        self.nums.append(int(num))

    def add_board(self, b):
        self.boards.append(Board())
        
        for l in b:
            for n in l.strip().split():
                self.boards[-1].add_num(int(n))
                
    def run_first(self):
        for n in self.nums:
            for b in [x for x in self.boards if not x.won]:
                if b.mark(n):
                    print(b.score())
                    b.won = True
                   
            

g = Game()
with open("3t.txt") as f:
    lines = f.readlines()
    for n in lines[0].strip().split(","):
        g.add_num(n)
    lines = [x.strip() for x in lines[1:] if x.strip() != ""]
    ll = []
    for l in lines:
        if len(ll) < 5:
            ll.append(l)
        else:
            g.add_board(ll)
            ll = []
            ll.append(l)
    g.add_board(ll) 
    
    g.run_first()