'''
JeLifish Trio: Jian Hong Li, Verit Li, Erica Li, Nibbles, Hugo, JHL
Soft Dev
K04 -- Random Devo from Krewes
2022-09-27
time spent: 4 hrs
DISCO: 
You can get the length of a dictionary through just using the method len(dictionary) on it.  
You have to import randint from random to use it
QCC: Would it be faster to take all of the lists associated with the keys, make a giant list, and then pick a random value from the lists? 
OPS SUMMARY: 
If krewes is empty, return ERROR
Gets a list of the keys in the krewes
Randomly iterates through all the list of keys to determine whether it contains values or not. If the key is empty, it will remove the key and continue on. If all the keys’ lists are empty, return ERROR. 
When one of the keys is found to have a non-empty list, this key is chosen. 
Choose a random index from list associated with chosen key
Return value at the random index of the associated key. 
'''
from random import randint

krewes1 = {1:["1", "2", "3"], 2:["A", "B", "C"]}
krewes2 = {
    2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"],
    7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
    8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
}
krewes3 = {}
krewes4 = {1:["1"], 2:[]}
krewes5 = {1:[], 2:[]}

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
    return k[r] #returns value at random index of random list


print(getRandom(krewes1))
print(getRandom(krewes2))
print(getRandom(krewes3))
print(getRandom(krewes4))
print(getRandom(krewes5))
