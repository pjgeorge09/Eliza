# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:34:26 2020

@author: Peter
TODO:
    Catch Gibberish
    Catch Overly Discriptive
    Catch Cursing
    Catch emotions. {Sad, Angry, Happy}
    Catch and trim punctuation (if it exists)
    Catch extremes (words like suicide)
"""
import re
import random
import sys

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
vulgar = 0

'''Random Lists to maybe be moved around later'''
cursing = ["ass","bitch","shit","fuck", "fucking", "shitting", "asshole"] #Just to demonstrate. I don't want to write a ton of them
# SOURCE FOR SYNONYMS :  https://www.thesaurus.com/browse/bad
S_bad = ["atrocious","awful","cheap","crummy","dreadful","lousy","poor","rough","sad","unacceptable","blah","bummer",
         "diddly","downer","garbage","gross","imperfect","inferior","junky","synthetic","abominable","amiss","bad news",
         "careless","cheesy","crappy","cruddy","defective","deficient","dissatisfactory","erroneous","fallacious",
         "faulty","godawful", "grody", "grungy", "icky", "inadequate", "incorrect", "off", "raunchy", "slipshod", 
         "stinking", "substandard", "unsatisfactory"]
S_sad = []
S_happy = []
S_calm = []


'''Catch their first name'''
def catchName(myNameIsPhrase):
    myNameIsPhrase = catchPreferredName(myNameIsPhrase)
    tokens = tokenize(myNameIsPhrase)
    for _ in tokens:
        _ = _.lower()
        if re.search(r'^(my)$|^(name)$|^(is)$|^(i\'m)$|^(i)$|^(am)$|^(they)$|^(call)$|^(me)$|^(you)$|^(can)$|^(nickname)$|^(go)$|^(by)$|^(sometimes)$|^(hello)$', _) is None:
            return _.capitalize()
    return 

''' Specifically catches "you can call me" "my friends call me" etc'''
def catchPreferredName(myNameIsPhrase):
    myNameIsPhrase = myNameIsPhrase.lower()
    if re.search(r'(call(s|ed|ing)?\s(me))', myNameIsPhrase) is not None:
        groupIt = re.search(r'(.*?)?(\s)?((call)(s|ed|ing)?\s(me))\s(.*?)$', myNameIsPhrase)
        return groupIt.group(len(groupIt.groups()))
    return myNameIsPhrase

'''Turn any string into an array of tokens based on white space(+)'''
def tokenize(phrase):
    return re.split('\s+', phrase)

''' Trim weird start words to reponses '''
def trim(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'^((yeah)|(yes)|(sure))(\W)?(\s)', "", sentence)
    sentence = re.sub(r'^((nah)|(no)|(eh)|(maybe)|(well))(\W)?(\s)', "", sentence)
    #sentence = re.sub(r'^((i don\'t know)|(i dont know)|(i am not sure)|(i\'m not sure))(\W)?(\s)', "", sentence)
    
    return sentence

''' Flip the start of standard responeses. Example : She is --> Why is she | They are --> Why are they '''
def  theyAreFlip(sentence):
    r = random.randint(1,10)
    #improved method of regex
    toReturn = ""
    groupIt = ""
    
    if(r < 3):
        return "How does that make you feel\n"
    elif(r >= 3 and r < 9):
        if re.match(r'(.*?)\b(he|she|they|them|it|those|this|these)\s(is|are|am)\b\s(.*)?', sentence):
            groupIt = re.search(r'(.*?)\b(he|she|they|them|it|those|this|these)\s(is|are|am)\b\s(.*)?', sentence)
            return (toReturn + "Why " + groupIt.group(3) + " " + groupIt.group(2) + " " + groupIt.group(4) + "\n")
        else:
            return sentence
    else:
        return sentence
    return sentence

''' Flip sentences centered around THINK '''
def  thinkFlip(sentence):
    r = random.randint(1,10)
    groupIt = ""
    print("R = " + str(r))
    if(r < 3):
        return "How are those thoughts affecting you\n"
    elif(r >= 3 and r < 7):
        if re.match(r'(.*?)?\b(think|thinks)\b\s(.*)?', sentence):
            groupIt = re.search(r'(.*?)?\b(think|thinks)\b\s(.*)?', sentence)
            additive = "Why do"
            pronouns = ["he ","she ","it "]
            if(groupIt.group(1) in pronouns):
                additive = additive + "es "
            else:
                additive = additive + " "
            return (additive + groupIt.group(1) + groupIt.group(2) + " " + groupIt.group(3) + "\n")
        else:
            return sentence
    elif(r>=7 and r <9):
        if re.match(r'(.*?)?\b(think|thinks)\b\s(.*)?', sentence):
            groupIt = re.search(r'(.*?)?\b(think|thinks)\b\s(.*)?', sentence)
            additive = "Why do"
            pronouns = ["he ","she ","it "]
            if(groupIt.group(1) in pronouns):
                additive = additive + "es "
            else:
                additive = additive + " "
            return ("Why do " + groupIt.group(1) + " " + groupIt.group(2) + " that\n")
        else:
            return sentence
    else:
        return sentence
    return sentence

'''Working on making a basic full sentence translation for basic sentences.'''
def flip(sentence):
    sentence = sentence.lower()
    sentence = trim(sentence)
    global vulgar
    tempvulgar = 0
    tokens = tokenize(sentence)
    toReturn = ""
    for token in tokens:
        if token in cursing:
            tempvulgar += 1
            vulgar += 1
            token = re.sub(r'\w+', '<Explicative>', token)
            
        token = re.sub(r'^i$|^(me)$', 'YOU', token)
        token = re.sub(r'^(am)$', 'ARE', token)
        token = re.sub(r'^(im)$|^(i\'m)$', 'YOU\'RE', token)
        token = re.sub(r'^my$', 'YOUR', token)
        token = re.sub(r'^was$', 'WERE', token)
        token = re.sub(r'^(i\'ve)$', 'YOU\'VE', token)
        token = re.sub(r'^(you\'re)$|^(youre)$|^(your\'e)$', 'I\'M', token)
        token = re.sub(r'^(you)$', 'ME', token)
        token = re.sub(r'^(dont)$', 'DON\'T', token)
        toReturn += (token + " ")  #Simply adds a space, can also be done in regex by adding a space to the sub but this is cleaner
    
    if re.match(r'(.*?)\b(he|she|they|them|it|those|this|these)\s(is|are|am)\b\s(.*)?', toReturn):
        toReturn = theyAreFlip(toReturn)    
    elif re.match(r'(.*?)\b(think|thinks)\b\s(.*)?',toReturn):
        toReturn = thinkFlip(toReturn)
    
        
    toReturn = toReturn[:-1].capitalize() #Remove last space, and capitalize start of sentence
    if(tempvulgar>0):
        print("\nPlease try to keep the language decent. My AI could learn to curse, and eventually we could have terminators.")
    
    return toReturn + "?"

''' Add a precursor statement to the start '''
def cursor(word):
    r = random.randint(1,100)
    precursors = ["I see. " , "Okay. " , "Alright. " , "Ah. " , "Hmm. " , "Sure. "]
    postcursors = [" Let's explore more about that.\n" , " Tell me more.\n" , " How is that affecting you?\n",]
    #" Why do you think that is?\n", " What do you think caused that?\n"," Why's that?\n" , 
    if r%2 == 0:
        if word == "pre":
            return random.choice(precursors)
        return random.choice(postcursors)
    if word == "pre":
        return ""
    return "\n"

''' Identify certain tones in a sentence'''
def parseEmotions(sentence):
    # Sad , Angry , Happy , Calm , Vulgar
    toReturn = [0,0,0,0,0]
    
    return toReturn    






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
waiting = input("Greetings, " + client + ". How can I help you today?\n").lower()
'''------------Respond to base state------------'''

while waiting is not None:
    emotions = parseEmotions(waiting)
    waiting = input(cursor("pre") + flip(waiting) + cursor("post"))
    #Catch Exit and Quit
    if re.search(r'[E|e]xit|[Q|q]uit', waiting[:4]) is not None:
        sys.exit("Program ended. I hope I can help you again! Goodbye, " + client)
    
    








'''TODO : Consider emotional state'''



''' #Currently unused but kind of cool and maybe useful code, if i can figure out how to implement it
for _ in range(0,len(waiting)):
    word = waiting[_]
    if word in waiting:
        waiting[_].upper()
    waiting[_] = transition(word)

print(waiting)
    


for word in waiting:
    if word in verbs:
        print("Verb found: " + word)'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
