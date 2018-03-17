import numpy as np


class Select:
    def __init__(self, pop, fitness, POP_SIZE):
        self.pop = pop
        self.fitness = fitness
        self.POP_SIZE = POP_SIZE
        self.select()
    def select(self):
        fitness = []
        for key, value in self.fitness.items():
            fitness.append(value)
        idx = np.random.choice(np.arange(self.POP_SIZE), size=self.POP_SIZE, replace=True,
                                   p=fitness / sum(fitness))
        for i in range(self.POP_SIZE):
            self.pop.update({"child" + str(i + 1): self.pop["child" + str(idx[i]+1)]})
    def getPop(self):
        return self.pop
