import sys, getopt
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
from datetime import date
import csv
from lib.tavuong_visual import *
from lib.tavuong_model import *
from lib.tavuong_readfile import *
from lib.tavuong_simulator import *
#from lib.vuong_covid19_visual import *
#from lib.vuong_covid19_model import *
from lib.user_visual import *

def main(argv):
# --------------------------------------
# ARGUMENT Processing
    inputfile = ''
    outputfile = ''
    country_in = ''
    mode_in = ""
    gesund_in =""    
    ncasesfile=''
    deathsfile =''
    try:
        opts, args = getopt.getopt(argv,"hi:o:c:m:g:n:d:t:r:s:",["ifile=","ofile=","country=","mode=", "recover=",\
        "nfile=","dfile=", "tau=", "recP="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('COVID19-SIMULATION: \n -n <new_Cases_file> -d <new_Deaths_file> -o outputfile \n -c country -o mode'+ \
            '\n VUONG Simulation Paramters: \n -g recover -t Incubation Periode -r Recovery Period -s simulation mode')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--nfile"):
            ncasesfile = arg
        elif opt in ("-d", "--dfile"):
            deathsfile = arg
        elif opt in ("-c", "--country"):
            country_in = arg
        elif opt in ("-m", "--mode"):
            mode_in = arg
        elif opt in ("-g", "--recover"):
            gesund_in = arg
        elif opt in ("-t", "--tau"):
            tau_in = arg
        elif opt in ("-r", "--recP"):
            recP_in = arg
        elif opt in ("-s", "--simu"):
            simu_mode = arg

# input control
#    print (argv)

#    if argv[0] != "": print (argv)
# --------------------------------------
# DIALOG
# Data-files amd country ( colum Name) choise
    print("---------------------------------------|")
    print("| VUONG Covid19 Simulator              |")
    print("| Data Simulation                      |")
    print("| Data Analysis                        |")
    print("| Author: Dr.-Ing. The Anh Vuong       |")
    print("---------------------------------------\n")

# covid19-data-kit: CSV Data reading
# source https://ourworldindata.org/coronavirus-source-data
# download put to ./data, eg. new_casesC.csv
    sname = inputfile
    if sname == "":
        sname = input ('VMODEL > Case data file? ')
    if sname =="":
        sname = './data/new_casesC.csv'
    
#    icountry = 0
#    iland = 0 

#    fig, ax = plt.subplots()
    sname = ncasesfile

    namecountry =""
    namecountry = country_in
    if namecountry == "": namecountry = input("VMODEL > country? ")

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
        print("| ta : tavuong                           |")
        mode  = input('VMODEL > What is your calculate-model? ')
    print ('KIT > model: ' + mode)
# RECOVERED SECLECT
    gesund = 0.0
    if ((mode == "ac") or mode == "sr"):
        gesund ='0.0'
    else:
        if (gesund_in == ""):
            gesund_in  = input('KIT > Recovered factor? ')
        gesund = float(str(gesund_in))
#       gesund = gesund_in
    #    print ('Recovered factor : ' + str(gesund)) 

    fig, ax = plt.subplots()

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

    if (mode in 'ta'):
#        simu_mode  = input('VMODEL > Simulation Stufe ? ')
#        print (simu_mode)
#        simu_mode = 3
        vuong_covid_Model (ncasesfile,deathsfile,country_in, gesund, int(simu_mode), int(tau_in),int(recP_in))
#        print ("OK")
#       if (iloop == 0): tavuong_multi_ac(x,nc,'blue',label_text=(namecountry + sname))
#        if (iloop == 1): tavuong_multi_ac(x,nd,'red', label_text=(namecountry + sname))

# JPEG OUTPUT: 
#   picstore = 1
    picstore = 0

    show_curve(ax,"Dr.Vuong-COVID19-SIMULATOR",namecountry,outputfile)

    
# main()
main(sys.argv[1:])
