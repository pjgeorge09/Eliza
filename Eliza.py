# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:34:26 2020

@author: Peter
TODO:
    Catch Gibberish
    Catch Overly Discriptive
    Catch Cursing
    Catch emotions. {Sad, Angry, Happy}
    
"""
import re
import random

'''Catch their first name'''
def catchName(myNameIsPhrase):
    tokens = tokenize(myNameIsPhrase)
    for _ in tokens:
        _ = _.lower()
        if re.search(r'my|name|is|i\'m|i|am|they|call|me|you|can|nickname|go|by|sometimes|hello', _) is None:
            return _
    return 

'''Turn any string into an array of tokens based on white space(+)'''
def tokenize(phrase):
    return re.split('\s+',phrase)

'''--------------Init--------------'''
phrase = input("Hi, I'm a psychotherapist. What is your name?\n")
client = catchName(phrase)
count = 1
while(client is None and count < 3): #Three tries, then they get Bubbles.
    phrase = input("I'm sorry, I misunderstood something. Could you tell me your name again please?\n")
    client = catchName(phrase)
    count+=1
if(client is None):
    print("I'm going to call you Bubbles.")
    client = "Bubbles"
    
'''------------Start Convo------------''' #Consider alternate greetings, alternate phrases
waiting = input("Greetings, " + client + ". How are you feeling today?\n")

'''------------Respond to base state------------'''