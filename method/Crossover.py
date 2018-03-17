import random
from struct import unpack, pack

import numpy as np


class Crossover:
    def __init__(self,parent, pop, CROSS_RATE, POP_SIZE, filter):
        self.parent = parent
        self.pop = pop
        self.filter = filter
        self.CROSS_RATE = CROSS_RATE
        self.POP_SIZE = POP_SIZE
        self.childMlist = []
        self.childSlist = []
        self.crossover()
    def crossover(self):
        for key, value in self.parent.items():
            if np.random.rand() < self.CROSS_RATE:
                i_ = np.random.randint(0, self.POP_SIZE, size=1)
                mParent = list(bin(int(value[0]))[2:])
                mParentdot = self.transform(value[0]-int(value[0]))
                sParent = list(bin(int(value[1]))[2:])
                sParentdot = self.transform(value[1]-int(value[1]))
                mPop = list(bin(int(self.pop['child' + str(i_[0]+1)][0]))[2:])
                mPopdot = self.transform(self.pop['child' + str(i_[0]+1)][0] - int(self.pop['child' + str(i_[0]+1)][0]))
                sPop = list(bin(int(self.pop['child' + str(i_[0]+1)][1]))[2:])
                sPopdot = self.transform(self.pop['child' + str(i_[0]+1)][1]-int(self.pop['child' + str(i_[0]+1)][1]))
                if self.filter:
                    m2Parent = list(bin(int(value[2]))[2:])
                    m2Parentdot = self.transform(value[2] - int(value[2]))
                    s2Parent = list(bin(int(value[3]))[2:])
                    s2Parentdot = self.transform(value[3] - int(value[3]))
                    m2Pop = list(bin(int(self.pop['child' + str(i_[0]+1)][2]))[2:])
                    m2Popdot = self.transform(self.pop['child' + str(i_[0]+1)][2]-int(self.pop['child' + str(i_[0]+1)][2]))
                    s2Pop = list(bin(int(self.pop['child' + str(i_[0]+1)][3]))[2:])
                    s2Popdot = self.transform(self.pop['child' + str(i_[0]+1)][3] - int(self.pop['child' + str(i_[0]+1)][3]))
                    m2Parent, m2Pop = self.padding(m2Parent, m2Pop)
                    m2Parentdot, m2Popdot = self.padding(m2Parentdot, m2Popdot)
                    s2Parent, s2Pop = self.padding(s2Parent, s2Pop)
                    s2Parentdot, s2Popdot = self.padding(s2Parentdot, s2Popdot)
                mParent, mPop= self.padding(mParent,mPop)
                mParentdot, mPopdot = self.padding(mParentdot, mPopdot)
                sParent, sPop = self.padding(sParent, sPop)
                sParentdot, sPopdot = self.padding(sParentdot, sPopdot)
                m = self.cross(mParent, mPop)
                mdot = self.cross(mParentdot, mPopdot)
                s = self.cross(sParent, sPop)
                sdot = self.cross(sParentdot,sPopdot)
                self.childMlist.append(int("".join(map(str, m)), 2) + self.transformDec('0b' + ''.join(mdot)))
                self.childSlist.append(int("".join(map(str, s)), 2) + self.transformDec('0b' + ''.join(sdot)))
                if self.filter:
                    m2Parent, m2Pop = self.padding(m2Parent, m2Pop)
                    m2Parentdot, m2Popdot = self.padding(m2Parentdot, m2Popdot)
                    s2Parent, s2Pop = self.padding(s2Parent, s2Pop)
                    s2Parentdot, s2Popdot = self.padding(s2Parentdot, s2Popdot)
                    m2 = self.cross(m2Parent, m2Pop)
                    m2dot = self.cross(m2Parentdot, m2Popdot)
                    s2 = self.cross(s2Parent, s2Pop)
                    s2dot = self.cross(s2Parentdot, s2Popdot)
                    self.childMlist.append(int("".join(map(str, m2)), 2) + self.transformDec('0b' + ''.join(m2dot)))
                    self.childSlist.append(int("".join(map(str, s2)), 2) + self.transformDec('0b' + ''.join(s2dot)))
            else:
                self.childMlist.append(value[0])
                self.childSlist.append(value[1])
                if self.filter:
                    self.childMlist.append(value[2])
                    self.childSlist.append(value[3])
    def transform(self, num):
        change = []
        a = bin(unpack('I', pack('f', num))[0])
        for x in a[2:]:
            change.append(x)
        return change

    def transformDec(self, num):
        change = float(unpack('f', pack('I', int(num, 0)))[0])
        return change

    def padding(self, data1, data2):
        if len(data1) > len(data2):
            for i in range(len(data1) - len(data2)):
                data2.insert(0, '0')
        else:
            for i in range(len(data2) - len(data1)):
                data1.insert(0, '0')
        return data1, data2
    def cross(self, data1, data2):
        index = random.randint(1, len(data1))
        child = data1[:index] + data2[index:]
        return child