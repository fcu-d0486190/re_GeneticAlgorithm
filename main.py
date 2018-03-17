import operator

from openpyxl import Workbook

from method.CreateChlid import CreateChlid
from method.Crossover import Crossover
from method.Filter import Filter
from method.Fitness import Fitness
from method.Mutate import Mutate
from method.ReadFile import ReadFile
from method.Select import Select

POP_SIZE = 800
CROSS_RATE = 0.8
MUTATION_RATE = 0.2
N_GENERATIONS = 100
Time = 10
ws = Workbook()
wb = ws.active
wb.append(['工具代碼', '一件時間','','兩件時間'])
readfile = ReadFile()
anslist = {}
for key, value in readfile.information.items():
    ans = []
    print(key, value)
    for i in range(Time):
        data = value
        f = Filter(value)
        filter = f.multiple
        print(filter)
        createchlid = CreateChlid(data, POP_SIZE, filter)
        pop = createchlid.getPop()
        for i in range(N_GENERATIONS):
            F_values = Fitness(pop, data, filter)
            fitness = F_values.getFitness()
            print(max(fitness.items(), key=operator.itemgetter(1))[0])
            print(pop[max(fitness.items(), key=operator.itemgetter(1))[0]])
            select = Select(pop, fitness, POP_SIZE)
            pop_copy = pop.copy()  # 原
            pop = select.getPop()  # 選擇過後
            crossover = Crossover(pop, pop_copy, CROSS_RATE, POP_SIZE, filter)
            mutate = Mutate(crossover.childMlist, crossover.childSlist, MUTATION_RATE, POP_SIZE, filter)
            pop = mutate.getPop()
        remend = pop[max(fitness.items(), key=operator.itemgetter(1))[0]]
        remend.append(max(fitness.items(), key=operator.itemgetter(1))[1])
        ans.append(remend)
    anslist.update({key: ans})
for key,value in anslist.items():
    print(key)
    print(value)
    if len(value[0]) == 3:
        for i in value:
            wb.append([key, i[0], i[1], '', '', i[2]])
    else:
        for i in value:
            wb.append([key, i[0], i[1], i[2], i[3], i[4]])

ws.save('D:\\result\\time_model\\' + readfile.machinename[0] +'_GATimeModel.xlsx')
