"""
RANDO: Jian Hong Li, Ryan Lee
Soft Dev, pd 8
K05 -- Krewes
2022-09-30
time spent: (classtime) 2 hrs
DISCO: 
    To open a file you need file.open("file_name")
    You can then get the text of the file using file.read()
    To split a string into a list from a sequence of character, you can do .split("squence") 
QCC:
    What happens when you split a string twice? Will it be in a list within a list?

OPS Summary:
    1. Open krewes.txt and read it by using .read()method, which converts it to a string
    2. Split the string into list, separated by "@@@"
    3. Split each strings from the list into pd list, devo list, and ducky list by splitting "$$$"
    4. Using a for loop to input all the information into a dictionary
    5. Input the dictionary into the getRandom method to return what we want
"""

from random import randint

file = open("krewes.txt")
text = file.read()

pd = []
devo = []
ducky = []

diction = {}

def categorize(s):
    individual = s.split("@@@")
    for e in individual:
        t = e.split("$$$")
        pd.append(t[0])
        devo.append(t[1])
        ducky.append(t[2])
    for p in range(0, len(pd)):
        exists = False
        l = [devo[p] + " " + ducky[p]]
        for k in diction.keys():
            if pd[p] == k:
                diction[pd[p]] = diction[pd[p]] + l
                exists = True
        if not exists:
            diction[pd[p]] = l
    return None


def getRandom(dictionary):
    
    if len(dictionary) == 0:
        return "ERROR: Dictionary has no values" 
    key = []
    for e in dictionary.keys(): #gets all the keys
        key.append(e)
    while True:
        if len(key) == 0:
            return "ERROR: all lists empty"
        period = key[randint(0, len(key)-1)]  #chooses a random key
        if len(dictionary.get(period)) == 0:
            key.remove(period)
        else:
            r = randint(0, len(dictionary.get(period))-1) #chooses random index of the list associated with the random key
            k = dictionary.get(period)  #gets the list associated with the random key
            break
    return k[r] #returns value at random index of random lis
categorize(text)
print(diction)
print(getRandom(diction))

