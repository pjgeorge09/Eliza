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

verbs = []
file = "C:\\Users\\Peter\\OneDrive\\Documents\\listofwords\\verbs\\31Kverbs.txt"
with open(file, 'r') as f:
    verbs = f.read().splitlines()
f.close()

'''Emotional State Quanifier Counters'''
sad = 0
anger = 0
happy = 0
calm = 0

'''Random Lists to maybe be moved around later'''
cursing = ["Ass","Bitch","Shit","Fuck", "Fucking", "Shitting", "Asshole"] #Just to demonstrate. I don't want to write a ton of them
# SOURCE FOR SYNONYMS :  https://www.thesaurus.com/browse/bad
S_bad = ["atrocious","awful","cheap","crummy","dreadful","lousy","poor","rough","sad","unacceptable","blah","bummer",
         "diddly","downer","garbage","gross","imperfect","inferior","junky","synthetic","abominable","amiss","bad news",
         "careless","cheesy","crappy","cruddy","defective","deficient","dissatisfactory","erroneous","fallacious",
         "faulty","godawful", "grody", "grungy", "icky", "inadequate", "incorrect", "off", "raunchy", "slipshod", 
         "stinking", "substandard", "unsatisfactory"]
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

def transition(word):
    toBeNamed = { 
            "i" : "you",
            "am" : "are",
            "we" : "you all",
            "my" : "your"}
    if word not in toBeNamed:
        return word
    return toBeNamed[word]

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
waiting = input("Greetings, " + client + ". How are you feeling today?\n").lower()
waiting = tokenize(waiting)   

'''------------Respond to base state------------'''
for _ in range(0,len(waiting)):
    word = waiting[_]
    if word in waiting:
        waiting[_].upper()
    waiting[_] = transition(word)

print(waiting)
    


for word in waiting:
    if word in verbs:
        print("Verb found: " + word)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
