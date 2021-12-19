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
        for current, group in groupby(self, itemgetter(0)):
            try:
                all_airports = []
                for current, airports in group:
                    for aiport in airports.split(','):
                        if aiport not in all_airports:
                            all_airports.append(aiport)
                self.emit(current, all_airports)
            except ValueError:
                print('erro')
                pass

    def __iter__(self):
        for line in self.infile:
            try:
                parts = line.split(self.sep)
                yield parts[0], parts[1].rstrip()
            except:
                continue


if __name__ == "__main__":
    reducer = Reducer()
    reducer.reduce()
