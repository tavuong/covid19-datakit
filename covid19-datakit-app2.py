import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
from datetime import date
import csv
from lib.tavuong_visual import *
from lib.user_visual import *

def main():

    print("---------------------------------------|")
    print("| Covid19-datakit                     |")
    print("| Tools for Development                |")
    print("| Data Visualiszation                  |")
    print("| Data Analysis                        |")
    print("| author: Dr.-Ing. The Anh Vuong       |")
    print("---------------------------------------\n")
    print("| Demo Visualisation Multi Countries   |")

# covid19-data-kit: CSV Data reading
# source https://ourworldindata.org/coronavirus-source-data
# download put to ./data, eg. new_casesC.csv
    
    mode3 = input ('Mode:')
    fig, ax = plt.subplots()    
    sname =""
    sname = input ('Case data file:')
    if sname =="":
#        sname = 'new_cases.csv'
        sname = './data/new_casesC.csv'
    with open(sname,'r') as csvfile:
        
        fields = [] #header
        plots = csv.reader(csvfile, delimiter=',')

        fields = next(plots) 
        print (fields)
    
#   Country choise 
#   icountry is colum-numer of Data         
    iloop = 0
    while iloop < 3:
        namecountry = input("country : ")
        icountry = 0
        ncountry = ''
        for ncountry in fields:
            if (ncountry == namecountry):
#                    print ("loop"+ str(iloop) + " >"+ str(icountry) + ": " + fields[icountry])
                break
            icountry = icountry + 1
#            print (str(icountry) + ": " + fields[icountry])


# Not : y= " " must be change to 0 or delete Line
# row 0 =Datum --> Lauf Index, row 1 y (n)   

# First Data row will not be read        
        print ("loop"+ str(iloop) + " >"+ str(icountry) + ": " + fields[icountry]+ "namecountry:"+ namecountry)

        index=0
        with open(sname,'r') as csvfile:
            x = [] # csv 0. Colum
            y = [] # csv 1. Colum
            y1 =[] # Csv 2. Colum  
            y2 =[] # buffer
            plots = csv.reader(csvfile, delimiter=',')
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
                    index = index + 1

        print ("loop"+ str(iloop) + " >"+ str(icountry) + ": " + fields[icountry]+ "namecountry:"+ namecountry)
#            ax.plot(x,y, label=namecountry)

#            tavuong_collection_ac(x,y,y1,y2,namecountry)
        
        label_text= namecountry
        if (mode3 =="1"):
            if (iloop == 0): tavuong_multi_ac(x,y,"red", label_text)
            if (iloop == 1): tavuong_multi_ac(x,y,"black", label_text)
            if (iloop == 2): tavuong_multi_ac(x,y,"green", label_text)
            if (iloop == 3): tavuong_multi_ac(x,y,"blue", label_text)
        else:
            if (iloop == 0): tavuong_multi_s(x,y,y1,y2,"red", label_text)
            if (iloop == 1): tavuong_multi_s(x,y,y1,y2,"black", label_text)
            if (iloop == 2): tavuong_multi_s(x,y,y1,y2,"green", label_text)
            if (iloop == 3): tavuong_multi_s(x,y,y1,y2,"blue", label_text)
        
        iloop = iloop + 1
            
    show_curve(ax,"")

main()
