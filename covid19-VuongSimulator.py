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
    tau_in =''
    recP_in=''
    simu_mode =''
    try:
        opts, args = getopt.getopt(argv,"hi:o:c:m:g:n:d:t:r:s:",["ifile=","ofile=","country=","mode=", "recover=",\
        "nfile=","dfile=", "tau=", "recP=","simu="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('VuongSimulation: \n -n <new_Cases_file> -d <new_Deaths_file> -o outputfile \n -c country'+ \
            '\n -t Incubation Periode Tau \n -r Recovery Period \n -s simulation mode \n')
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
    print (argv)

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
# VMODEL input file is now -n and  -nd, -i is commented 
    sname = inputfile
#    if sname == "":
#        sname = input ('VMODEL > Case data file? ')
#    if sname =="":
#        sname = './data/new_casesC.csv'
    
#    icountry = 0
#    iland = 0 

#    fig, ax = plt.subplots()
    sname = ncasesfile

    namecountry =""
    namecountry = country_in
    if namecountry == "": namecountry = input("VMODEL > country? ")
    print ('Country' , namecountry)

# DIALOG
# Mode select
# set deirect to VUONG MODEL ta
    mode =""
    mode = mode_in
    
    mode ="ta"

    if mode == "": 
        print("| Visualization models:                  |")
        print("| ac : actual cases                      |")
        print("| sr : daily sum of cases                |")
        print("| gc : actual incl. estim. recovery rate |")
        print("| gs : accum.  incl. estim. recovery rate|")
        print("| me : my model                          |")
        print("| t2 : test plot                         |")
        print("| ta : VuongModell                       |")
        mode  = input('KIT  > What is your calculate-model? ')
#   print ('KIT > VuongModell' + mode)
# RECOVERED SECLECT
    gesund = 0.0
    if ((mode == "ac") or mode == "sr"or mode == "ta"):
        gesund ='0.0'
    else:
        if (gesund_in == ""):
            gesund_in  = input('KIT > Recovered factor? ')
        gesund = float(str(gesund_in))
    gesund = 0.0

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
#        simu_mode  = int(input('VMODEL > Simulation Stufe ? '))
#        if (simu_mode == ''):
# simu_mode  -----------------------------------------------------------------
        sread = ta_para_read('VMODEL > new_case-file ? ',ncasesfile, './data/new_cases.csv')
        ncasesfile = sread
        print ('new_case-file', ncasesfile)

        sread = ta_para_read('VMODEL > deaths-file ? ',deathsfile, './data/new_deaths.csv')
        deathsfile = sread
        print ('deaths-file', deathsfile)

        sread = ta_para_read('VMODEL > VuongSimualtion mode ? ',simu_mode, 6)
        simu_mode = sread
        print ('VuongSimualtion mode' , simu_mode)

#       sread = ta_para_read('VMODEL > Simulation Stufe ? ',gesund, '0.90')
#       gesund = float(str(sread))
#       print (sread , gesund)
        sread = ta_para_read('VMODEL > Incubation Period? ',tau_in, 7)
        tau_in = sread
        print ('Incubation Period' , tau_in)

        sread = ta_para_read('VMODEL > Recovery Period ? ',recP_in, 14)
        recP_in = sread
        print ('Recovery Period' , recP_in)
        
        gesund = 0.0
        if (gesund_in == ""):
            gesund_in  = input('VMODEL > Fix factor? ')
        gesund = float(str(gesund_in))

# One  Country - Mode 1-6
        if (int(simu_mode) <= 6):
            vuong_covid_Model (ncasesfile,deathsfile,namecountry, gesund, int(simu_mode), int(tau_in),int(recP_in),5)

# MUlti Country - Mode 7-9
# ----List von Country ./data/country:list.csv
# ----new parameter for mode 7
        else:
            switch7 = '5'
# ------dialog for mode 7
            if (int(simu_mode) == 7):
                switch7 = ''
                sread = ta_para_read('VMODEL > Mode Switch ? ',switch7, '5')
                switch7 = sread
                print ('Mode ', simu_mode, 'switch: ', switch7)
#-------command line for mode 7
            if (int(simu_mode) > 70) and (int(simu_mode) < 79):
                switch7 = int(simu_mode) - 70
                simu_mode = '7'


#           listn = ['Germany', 'Italy', 'France', 'Sweden', 'Belgium', 'United Kingdom', 'Russia']
            listn = []
            listn = tavuong_country_name('./data/vmodel_testlist.csv')
            print (listn)
            for ncc in listn:
                namecountry = ncc
                print ('VMODEL > ', ncc, namecountry) 
                vuong_covid_Model (ncasesfile,deathsfile,namecountry, gesund, int(simu_mode), int(tau_in),int(recP_in),int(switch7))
            
            namecountry = "Multi"

# show
#    picstore = 0

    show_curve(ax,"Dr.Vuong-COVID19-SIMULATOR",namecountry,outputfile)

    
# main()
main(sys.argv[1:])
