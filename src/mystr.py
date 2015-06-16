#! /usr/bin/env python
# coding=utf-8

def find_upper(s):
    a =[]
    for i in s:
        if str.isupper(i):
            a.append(i)
    return a

def find_upper2(s):
    return [i for i in s if str.isupper(i)]



    
