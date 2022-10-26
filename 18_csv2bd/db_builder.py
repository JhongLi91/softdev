#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O




DB_FILE="courses"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


command = "CREATE TABLE rosters(name TEXT, mark INTEGER);"
# test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row_data = row['code']
        mark_data = row['mark']
        c.execute("INSERT INTO rosters VALUES(" + '"' +  row_data + '"'  + "," + mark_data + ");")
#==========================================================

db.commit() #save changes
db.close()  #close database

