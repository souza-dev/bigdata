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
                flights = []
                for _, fly in group:
                    flights.append(fly.rstrip())
                most_freq = max(set(flights), key=flights.count)
                self.emit(current, most_freq)
            except ValueError:
                print('erro')
                pass

    def __iter__(self):
        for line in self.infile:
            try:
                parts = line.split(self.sep)
                yield parts[0], parts[1]
            except:
                continue


if __name__ == "__main__":
    reducer = Reducer()
    reducer.reduce()
