import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
from datetime import date
import csv
from lib.tavuong_visual import *
from lib.user_visual import *

def main():

    print("---------------------------------------|")
    print("| Covid19-data-kit                     |")
    print("| Tools for Development                |")
    print("| Data Visualiszation                  |")
    print("| Data Analysis                        |")
    print("| author: Dr.-Ing. The Anh Vuong       |")
    print("---------------------------------------\n")
    print("| Demo Visualisation                   |")

# covid19-data-kit: CSV Data reading
# source https://ourworldindata.org/coronavirus-source-data
# download put to ./data, eg. new_casesC.csv

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
# covid19-data-kit: Visualization 
# Mode select
    print("| Visualization mode                   |")
    print("| ac : actual case                     |")
    print("| sr : accumulate of cases             |")
    print("| me : my model                        |")
    print("| t2 : test plot                       |")
  
    mode  = input('What is your calculate-model? ')
    print ('model: ' + mode) 

#    if (mode in 'te'):
#        corona_plot_test(x,y) 

    fig, ax = plt.subplots()
# my_Model
    if (mode in 'me'): 
        my_collection_1(x,y,y1,y2,namecountry)

# Example Model    
    if (mode in 'ac'): 
        tavuong_collection_ac(x,y,y1,y2,namecountry)
    if (mode in 'sr'): 
        tavuong_collection_sr(x,y,y1,y2,namecountry)
# in development     
    if (mode in 'rf'): 
        tavuong_collection_rf1(x,y,y1,y2,namecountry)
# test     
    if (mode in 't2'):
        kit_plot_test2(x,y) 

    show_curve(ax,namecountry)

    
main()