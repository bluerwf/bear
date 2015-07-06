#! /usr/bin/env python
# coding=utf-8

class Queue:
    def __init__(self, size):

        self._lst = []
        self.size = size
    
    def enqueue(self, i):
        if len(self._lst) < self.size:
            self._lst.append(i)
        else:
            print'full'
    
    def dequene(self):
        try:
            self._lst.pop(0)
        except IndexError:
            print "dequeue from empty queue!"

    def __len__(self):
        return len(self._lst)

    def __str__(self):
        return str(self._lst)

    @property
    def length(self):
        return len(self)
