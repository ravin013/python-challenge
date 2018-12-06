import os
import csv

cwkdir = os.getcwd()

filepath = os.path.join( cwkdir,'D:\\','election_data.csv')

totalcount = 0; khancount = 0; correycount = 0; licount = 0; otooleycount = 0; max_votecount = 0

def percentage (part, whole):
    return 100 * float(part)/float(whole)

with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     for i in csvreader:
         voterid = i[0]
         country = i[1]
         candidate = i[2]
         
         totalcount = totalcount + 1

         if candidate =="Khan":
            khancount = khancount + 1
         if candidate =="Correy":
            correycount = correycount + 1
         if candidate =="Li":
            licount = licount + 1
         if candidate =="O'Tooley":
            otooleycount = otooleycount + 1
            

     candidatevote = {"Khan": khancount,"Correy": correycount,"Li" :licount, "O'Tooley": otooleycount}
      
     for candidate, value in candidatevote.items():
         if value > max_votecount:
            max_votecount = value
            winner = candidate
     
print(f'Election Results'+'\n')
print(f'-------------------------------'+'\n')
print(f'Total Votes: {totalcount}'+'\n')
print(f'-------------------------------'+'\n')

print(f'Khan: {percentage(khancount,totalcount):.3f}%  ({khancount})')
print(f'Correy: {percentage(correycount,totalcount):.3f}%  ({correycount})')
print(f'Li: {percentage(licount,totalcount):.3f}%  ({licount})')
print(f'O\'Tooley: {percentage(otooleycount,totalcount):.3f}%  ({otooleycount})')
print(f'--------------------------------'+'\n')
print(f'Winner: {winner} '+'\n')
print(f'--------------------------------'+'\n')

file_to_output = "D:\\/election_analysis.txt"
with open(file_to_output, "w") as txt_file:
    txt_file.write (f'Election Results'+'\n')
    txt_file.write(f'-------------------------------'+'\n')
    txt_file.write(f'Total Votes: {totalcount}'+'\n')
    txt_file.write(f'-------------------------------'+'\n')
    txt_file.write(f'Khan: {percentage(khancount,totalcount):.3f}%  ({khancount})' +'\n')
    txt_file.write(f'Correy: {percentage(correycount,totalcount):.3f}%  ({correycount})'+'\n')
    txt_file.write(f'Li: {percentage(licount,totalcount):.3f}%  ({licount})'+'\n')
    txt_file.write(f'O\'Tooley: {percentage(otooleycount,totalcount):.3f}%  ({otooleycount})'+'\n')
    txt_file.write(f'--------------------------------'+'\n')
    txt_file.write(f'Winner: {winner} '+'\n')
    txt_file.write(f'--------------------------------'+'\n')