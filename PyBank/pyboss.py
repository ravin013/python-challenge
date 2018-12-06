import os

import csv


cwkdir = os.getcwd()

filepath = os.path.join(cwkdir,'D:\\','employee_data.csv')

with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csv.reader)
    
for i in csv.reader:
    EmpID = i(0)
    name = i(1)
    DOB = i(2)
    SSN = i(3)
    State = i(4)

    str.split(' ')