#! /usr/bin/env python
# coding=utf-8

A = 10

def find_upper(s):
    a =[]
    for i in s:
        if str.isupper(i):
            a.append(i)
    return a

def find_upper2(s):
    return [i for i in s if str.isupper(i)]


def modify_global_var():
   global A
   A = 5
   print A

modify_global_var()
print A

a = [1, 2, 3]
b = [3, 2, 4]
c = [i for i in a if i not in b]

print c
