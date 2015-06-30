#! /usr/bin/env python

def deco(ver=True):
    def realdeco(f):
        def wrap(*args, **kargs):
            if ver is True:
                print 'before sunset'
                v = f(*args, **kargs)
                print 'after sunset'
            else:
                v = f(*args, **kargs)
            return v
        return wrap
    return realdeco

class Sort:

    def qsort(self, l, h, lst):
        def par(l, h, lst):
            i = l
            j = h
            p = lst[i]
            while i < j:
                while i < j and lst[j] > p:
                    j -= 1
                lst[i], lst[j] = lst[j], lst[i]
                while i <j and lst[i] < p:
                    i +=1
                lst[i], lst[j] = lst[j], lst[i]
            return i

        if l < h:
            idx = par(l, h, lst)
            self.qsort(l, idx-1, lst)
            self.qsort(idx+1, h, lst)

    @deco(ver=False)
    def bubble(self, lst):
        l = len(lst)
        while l:
            for i in range(l-1):
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
            l  -= 1
        return lst

if __name__ == '__main__':
    a = Sort()
    a.bubble([2, 1, 0])
