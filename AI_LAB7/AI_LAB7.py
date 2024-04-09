import math
import csv

with open("16.csv","r", newline='') as file, open("redacted.csv", "w") as wFile:
    ReadFile=csv.reader(file, delimiter=';')
    WriteFile=csv.writer(wFile, dialect='excel',lineterminator='')

    a=0

    for row in ReadFile:
        values=row

        if(not values[0]):
            values[0]='p'
        if(not values[1]):
            values[1]='10.0'
        if(not values[2]):
            values[2]='f'
        if(not values[3]):
            values[3]='g'
        if(not values[4]):
            values[4]='e'
        if(not values[5]):
            values[5]='f'
        if(not values[6]):
            values[6]='e'
        if(not values[7]):
            values[7]='c'
        if(not values[8]):
            values[8]='w'
        if(not values[9]):
            values[9]='15.0'
        if(not values[10]):
            values[10]='13.0'
        if(not values[11]):
            values[11]='s'
        if(not values[12]):
            values[12]='y'
        if(not values[13]):
            values[13]='w'
        if(not values[14]):
            values[14]='u'
        if(not values[15]):
            values[15]='w'
        if(not values[16]):
            values[16]='t'
        if(not values[17]):
            values[17]='g'
        if(not values[18]):
            values[19]='w'
        if(not values[20]):
            values[20]='d'
            
        WriteFile.writerow(values)

        a+=1
        
