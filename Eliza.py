# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:34:26 2020

@author: Peter
"""
import re
import random

'''Catch their first name'''
def catchName():
    phrase = input("Hi, I'm a psychotherapist. What is your name?\n")
    tokens = tokenize(phrase)
    return 

'''Turn any string into an array of tokens based on white space(+)'''
def tokenize(phrase):
    return re.split('\s+',phrase)

client = catchName()
print(client)

