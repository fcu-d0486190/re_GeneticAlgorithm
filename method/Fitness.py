import numpy as np


class Fitness:
    def __init__(self, pop, data, filter):
        self.pop = pop
        self.data = data
        self.filter = filter
        self.grade = {}
        self.fitness()

    def fitness(self):
        result = []
        for key, value in self.pop.items():
            whichWave = []
            for j in self.data:
                gausslist = []
                gauss = np.exp(-(j - value[0]) ** 2 / (2 * value[1] ** 2)) / (value[1] * np.math.sqrt(2 * np.math.pi))
                gausslist.append(gauss)
                if self.filter:
                    for i in range(1, 10):
                        gauss = np.exp(-(j - (value[0] + (i * (value[2] - value[0])))) ** 2 / (2 * value[3] ** 2)) / (value[3] * np.math.sqrt(2 * np.math.pi))
                        gausslist.append(gauss)
                    which = gausslist.index(max(gausslist)) + 1
                    whichWave.append(which)
                    if value[0] > value[2]:
                        ans = 0
                    else:
                        if value[0] / (value[2] - value[0]) > (value[2] - value[0]) / value[0]:
                            c = value[0] / (value[2] - value[0])
                        else:
                            c = (value[2] - value[0]) / value[0]
                        ans = max(gausslist) / which * value[0] / value[2] / c
                    result.append(ans)
                else:
                    result.append(gauss)
            if whichWave == []:
                self.grade.update({key: sum(result) / len(result) * min(result)})
            else:
                self.grade.update({key: sum(result) / len(result) * min(result)})
            result = []
    def getFitness(self):
        return self.grade