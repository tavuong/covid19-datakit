import sys, getopt
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
from datetime import date
import csv
from lib.tavuong_visual import *
from lib.tavuong_readfile import *
from lib.user_visual import *

#  CSV-Data reading -> Header Filter 
#------------------------------------------------------
def tavuong_country_position(sname, namecountry, iland):
# sanme : csv File
# country_im : Filter value
# icountry : Field Position

    with open(sname,'r') as csvfile:
        fields = []  #header
        plots = csv.reader(csvfile, delimiter=',')
        
        icountry = 0
        fields = next(plots)
        field_length = len(fields) 
# list of countries
#        print (fields)
#        print (field_length)
            
#   Country / Fieldname choise 
#   icountry is colum-numer of Data
        icountry = 0
        ncountry = ''
        for ncountry in fields:
            if (ncountry == namecountry):
#                print (str(icountry) + ": " + fields[icountry])
                iland = icountry
                return iland 
#            print (str(icountry) + ": " + fields[icountry])
            icountry = icountry + 1


    
#---------------------------------------------------------------
# First Data row will not be read
def tavuong_read_timeseries(sname, iland,x,y, control):

#    icountry = 0
    icountry = iland
#    print (iland, icountry)        
    with open(sname,'r') as csvfile:
#            print ("loop"+ str(iloop) + " >"+ sname + str(icountry) + ": " +  "namecountry:"+ namecountry)
#        fields = []  #header
        x = [] # csv 0. Colum
        y = [] # csv 1. Colum
#            nc = [] # new_case 1. Colum
#            nd = [] # new_death 1. Colum
#            y1 =[] # Csv 2. Colum  
#            y2 =[] # buffer
        plots = csv.reader(csvfile, delimiter=',')
        index=0
        for row in plots:
            if (index!=0):
                x.append(date.fromisoformat(row[0]))
                if (row[icountry]==""):
                    y.append(0)
                else:
                    y.append(int(row[icountry]))
#                y1.append(0)
#                y2.append(0)
            else:
                index = index + 1
    if (control =='x'):
        return (x)
    else:
        return (y)

#    kit_plot_test2 (x,y)                
# tavuong_multi_ac(x,y,color_text="blue",label_text=sname)

# --------------------------------------------------------
def tavuong_timeseries_generator(x,y):

    k = 0
    for k in x:
        y.append(0)    
    return (y)

# --------------------------------------------------------
