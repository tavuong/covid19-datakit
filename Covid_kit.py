import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
from datetime import date
import csv
from lib.tavuong_visual import *

def main():

    print("---------------------------------------|")
    print("| Covid19-data-kit                     |")
    print("| Data Research - not medicin aproving |")
    print("| Case Data  analysis                  |")
    print("| ac : actual case                     |")
    print("| ca : actual case (Tau,r)             |")
    print("| sr : summe (Tau,r)                   |")
    print("| author: Dr.-Ing. The Anh Vuong       |")
    print("---------------------------------------\n")
    
# CSV-Data reading
# source https://ourworldindata.org/coronavirus-source-data

    sname =""
    sname = input ('Case data file:')
    if sname =="":
#        sname = 'new_cases.csv'
        sname = './data/new_casesC.csv'
    with open(sname,'r') as csvfile:
        x = [] # csv 0. Colum
        y = [] # csv 1. Colum
        y1 =[] # Csv 2. Colum  
        y2 =[] # buffer
        fields = [] #header

#  CSV-Data reading

        plots = csv.reader(csvfile, delimiter=',')

        icountry = 0
        fields = next(plots) 
        print (fields)
#   Country choise 
#   icountry is colum-numer of Data        
        namecountry = input("country:")
        icountry = 0
        ncountry = ''
        for ncountry in fields:
            if (ncountry == namecountry):
                print (str(icountry) + ": " + fields[icountry])
                break
            icountry = icountry + 1
#            print (str(icountry) + ": " + fields[icountry])


# Not : y= " " must be change to 0 or delete Line
# row 0 =Datum --> Lauf Index, row 1 y (n)   

# First Data row will not be read        
        index=0
        for row in plots:
            if (index!=0):
                x.append(date.fromisoformat(row[0]))
                if (row[icountry]==""):
                    y.append(0)
                else:
                    y.append(int(row[icountry]))
                y1.append(0)
                y2.append(0)
            else:
#                print (row[0])
#                print (row[icountry])
                index = index + 1
#        print (x)
#        print (y)    
# Mode select
    mode  = input('What is your calculate-mode? ')
    print ('mode: ' + mode) 

# Visualization
    if (mode in 'te'):
        corona_plot_test(x,y) 

    if (mode in 'ac'): 
        block_case_ac(x,y,y1,y2,namecountry)
    if (mode in 'ca'): 
        block_case_ca(x,y,y1,y2,namecountry)
    if (mode in 'sr'): 
        block_case_sr(x,y,y1,y2,namecountry)

    
main()