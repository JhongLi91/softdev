'''
Duo Jian Hong Li, Ryan Lee
SoftDev pd08
K06
2022-10-03
time spent: 1hrs
DISCO:
  * Parsing a csv file with "with open('___.csv', 'r') as ___"
  * We put the data into prefix so that it's easier to determine what percent range it has
  
QCC:
  * what does the 'r' mean in the "with open() as ' method

  
HOW THIS SCRIPT WORKS:
1. Open the cvs file using the method with open("file_name") as ""
2. Input the data from the csv file into the dictionary
3. Order the dictioanry file into prefix form
4. Randomly generate a number from 0 to 100
5. Select the occupation based on the randomly generated number
6. Checked our solution by running randomOccupation 50000 times
'''

import csv
import random as rng

diction = {}

#parsing occupation rows
with open('occupations.csv', 'r') as csv_file:
  occupations = csv.reader(csv_file)
  #putting the rows into diction mapping job to percent value
  for row in occupations:
    if (row[0] != "Job Class"):
      diction[row[0]] = float(row[1])
diction.pop("Total")
#print(diction)

pref = {}

#putting the dictionary into prefix notation where each successive occupation adds its percent to the percent of the occupation before it.
def prefix(dictionary):
  total = 0.0
  for key in diction.keys():
    total += diction.get(key)
    pref[key] = total
  return None

prefix(diction)

def randomOccupation(dictionary):
  r = rng.random() * 100
  for key in dictionary.keys():
    if dictionary[key] > r:
      return key
  return None

#running 5000 times and seeing how many times we get each occupation
result = {}
i = 0
while i < 50000:
    exists = False
    rand = randomOccupation(pref)
    for k in result.keys():
      if rand == k:
          result[rand] = result[rand] + 1
          exists = True
          i+=1
    if not exists:
      result[rand] = 1
      i+=1

#dividing how many times we see each occupation by 5000 and multiplying by 100 to get the percent each occurs
for key in result.keys():
  result[key] = result[key] / 500

print(diction)
print("-----------------------")
print(result)
