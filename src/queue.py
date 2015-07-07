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
    
    def dequeue(self):
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

class AbsStack:
    def push(self, i):
        raise NotImplemented

    def pop(self):
        raise NotImplemented

class Stack(AbsStack):
    def __init__(self, size):
        self._lst = []
        self.size = size
    
    def push(self, i):
        if len(self._lst) < self.size:
            self._lst.append(i)
        else:
            print'full'

    def pop(self):
        try:
            v = self._lst.pop()
            return v
        except IndexError:
            print 'this stack is empty'

    @property
    def top(self):
        try:
            return self._lst[-1]
        except IndexError:
            return None

    @property
    def base(self):
        try:
            return self._lst[0]
        except IndexError:
            return None

    def __str__(self):
        return str(self._lst)

sstack = Stack(10)

sstack.push(1)
sstack.push(2)
