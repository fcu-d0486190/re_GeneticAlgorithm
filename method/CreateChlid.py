import random


class CreateChlid:
    def __init__(self, data, POP_SIZE, filter):
        self.pop = {}
        self.POP_SIZE = POP_SIZE
        self.filter = filter
        self.data = data
        self.random()
    def random(self):
        for i in range(self.POP_SIZE):
            list = []
            m = random.uniform(1, max(self.data))   # uniform(x,y)  random (x~y) range
            s = random.uniform(0.0000000000000001, 10)
            m2 = random.uniform(m, 2 * m)
            s2 = random.uniform(0.0000000000000001, 10)
            list.append(m)
            list.append(s)
            if self.filter:
                list.append(m2)
                list.append(s2)
            self.pop.update({"child" + str(i + 1): list})
    def getPop(self):
        return self.pop
