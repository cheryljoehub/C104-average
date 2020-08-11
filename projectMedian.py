# import csv
import  csv

#Using a loop.
with    open('fat.csv',newline='')  as  f:
    reader= csv.reader(f)
    file_data   =  list(reader)
file_data.pop(0)
new_data    =   []

for i   in  range(len(file_data)):
    n_number   =   file_data[i][1]
    new_data.append(n_number)
    
n   =   len(new_data)
new_data.sort()

# An if & else statement to check if the number of entries are even or odd.
if  n %2    == 0:
    median1 =   float(new_data[n//2])
    median2 =   float(new_data[n//2-1])
    median  =   (median1 +   median2)/2
    
else:
    median  =   new_data[n//2]
    print(n)
    
print('The median is ' + str(median))
    