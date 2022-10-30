import csv
import pandas as pd
rows = []

with open("gravityAdded.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
wholeData = rows[1:]
print(wholeData)

finalData = []
for i in wholeData:
    finalDict = {

    
        'name':i[1],
        'distance':i[2],
        'mass':i[3],
        'radius':i[4],
        'gravity':i[5],
    }
    finalData.append(finalDict)
print(finalData)