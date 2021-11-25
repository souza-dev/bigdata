#!/usr/bin/env python3
import sys
from itertools import groupby
from operator import itemgetter

SEP = '\t'

class Reducer(object):

    def __init__(self, infile=sys.stdin, separator=SEP):
        self.infile = infile
        self.sep = separator

    def emit(self, key, value):
        sys.stdout.write(f"{key}{self.sep}{value}\n")
        
    def reduce(self):
        dic = {}
        for current, group in groupby(self, itemgetter(0)):
            try:
                total = sum(int(count) for current, count in group)
                dic[current] = total
                #self.emit(current, total)
            except ValueError:
                print('erro')
                pass
        maximo = max(dic, key = dic.get)
        self.emit(maximo, dic[maximo])
    def __iter__(self):
        for line in self.infile:
            try:
                parts = line.split(self.sep)
                yield parts[0], float(parts[1])
            except:
                continue


if __name__ == "__main__":
    reducer = Reducer()
    reducer.reduce()
