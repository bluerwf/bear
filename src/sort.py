#! /usr/bin/env python

def deco(ver=True):
    def realdeco(f):
        def wrap(*args, **kargs):
            if ver is True:
                print 'before sunset'
                f(*args, **kargs)
                print 'after sunset'
            else:
                f(*args, **kargs)
        return wrap
    return realdeco

class Sort:
    def qsort(self):
        pass

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
    Sort().bubble([2, 1, 0])
