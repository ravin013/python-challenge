
import os

import csv


cwkdir = os.getcwd()

filepath = os.path.join( cwkdir,'C:\\','budget_data.csv')


monthcount = 0; total = 0; PreValue = 0; Diff = 0; DiffMax = 0; DiffMin = 0


with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f'----------------------------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue
        
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
       
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
         
         monthcount = monthcount + 1
         total = total + int(Amount) 


print(f'Total Months : {monthcount}')

print(f'Total: $ {total}')

print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')

print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')




file_to_output = "D:\\/budget_analysis.txt"
with open(file_to_output, "w") as txt_file:
    txt_file.write(f'Financial Analysis'+'\n')
    txt_file.write(f'----------------------------'+'\n')
    txt_file.write(f'Total Months : {monthcount}' +'\n')
    txt_file.write(f'Total: $ {total}' + '\n')
    txt_file.write(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})' + '\n')
    txt_file.write(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})' + '\n')
    
