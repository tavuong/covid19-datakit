import sys, getopt
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
from datetime import date
import csv
from lib.tavuong_visual import *
from lib.user_visual import *

def main(argv):
# --------------------------------------
# ARGUMENT Processing
    inputfile = ''
    outputfile = ''
    country_in = ''
    mode_in = ""
    gesund_in =""    
    try:
        opts, args = getopt.getopt(argv,"hi:o:c:m:g:",["ifile=","ofile=","country=","mode=", "recover="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('covid19-datakit \n -i <inputfile> -o <outputfile> \n -c country \n -o mode \n -g recover')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-c", "--country"):
            country_in = arg
        elif opt in ("-m", "--mode"):
            mode_in = arg
        elif opt in ("-g", "--recover"):
            gesund_in = arg

#    print ('Input file is "', inputfile)
#    print ('Output file is "', outputfile)
#    print ('Country is "', country_in, mode_in)
    print ('Country is "', country_in, mode_in, gesund_in)

    print (argv)

#    if argv[0] != "": print (argv)
# --------------------------------------
# DIALOG
# Data-files amd country ( colum Name) choise
    print("---------------------------------------|")
    print("| Covid19-datakit                     |")
    print("| Tools for Development                |")
    print("| Data Visualiszation                  |")
    print("| Data Analysis                        |")
    print("| author: Dr.-Ing. The Anh Vuong       |")
    print("---------------------------------------\n")
    print("| Demo Visualisation                   |")

# covid19-data-kit: CSV Data reading
# source https://ourworldindata.org/coronavirus-source-data
# download put to ./data, eg. new_casesC.csv
    sname = inputfile
    if sname == "":
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
#   Country / Fieldname choise 
#   icountry is colum-numer of Data        
        namecountry =""
        namecountry = country_in
        if namecountry == "": namecountry = input("country:")
        icountry = 0
        ncountry = ''
        for ncountry in fields:
            if (ncountry == namecountry):
                print (str(icountry) + ": " + fields[icountry])
                break
            icountry = icountry + 1
#            print (str(icountry) + ": " + fields[icountry])


# Not : y= " " must be change to 0 or delete Line
# row 0 =Datum --> X-axis , row 1 = y (x) ---> Y-axis  

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
# --------------------------------------
# DIALOG
# Mode select
    mode =""
    mode = mode_in
    if mode == "": 
        print("| Visualization models:                  |")
        print("| ac : actual cases                      |")
        print("| sr : daily sum of cases                |")
        print("| gc : actual incl. estim. recovery rate |")
        print("| gs : accum.  incl. estim. recovery rate|")
        print("| me : my model                          |")
        print("| t2 : test plot                         |")
        mode  = input('What is your calculate-model? ')
        print ('model: ' + mode)
# RECOVERED SECLECT
    gesund = 0.0
    if ((mode == "ac") or mode == "sr"):
        gesund ='0.0'
    else:
        if (gesund_in == ""):
            gesund_in  = input('Recovered factor? ')
        gesund = float(str(gesund_in))
    
    print ('Recovered factor : ' + str(gesund)) 

#    if (mode in 'te'):
#        corona_plot_test(x,y) 

    fig, ax = plt.subplots()
# my_Model
    if (mode in 'me'): 
        my_collection_1(x,y,y1,y2,namecountry,gesund)

# EXAMPLE MODEL    
    if (mode in 'ac'): 
        tavuong_collection_ac(x,y,y1,y2)
    if (mode in 'sr'): 
        tavuong_collection_sr(x,y,y1,y2)
# IN DEVELOPING     
    if (mode in 'gc'):
#        gesund = 0.8 
        tavuong_collection_gc(x,y,y1,y2,gesund)
    if (mode in 'gs'):
#        gesund = 0.8 
        tavuong_collection_gs(x,y,y1,y2,gesund)
    if (mode in 'rf'): 
        tavuong_collection_rf1(x,y,y1,y2,gesund)
# TEST     
    if (mode in 't2'):
        kit_plot_test2(x,y) 
# JPEG OUTPUT: 
#   picstore = 1
    picstore = 0

    show_curve(ax,sname,namecountry,outputfile)

    
# main()
main(sys.argv[1:])
