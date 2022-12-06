
#!/usr/bin/env python3

class Q:
    def __init__(self):
        self.size = 14
        self.data = []

    def add(self, x):
        if len(self.data) == self.size:
            self.data.pop(0)
        self.data.append(x)

    def is_marker(self):
        if len(set(self.data)) == self.size:
            print(self.data)
            return(True)
        else:
            return(False)



with open("input") as f:
    line = f.readline().strip()
    q  = Q()
    for i in range(len(line)):
        q.add(line[i])
        if q.is_marker():
            print("msg found at %d " % (i+1))
            break
    