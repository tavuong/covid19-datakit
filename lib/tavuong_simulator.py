import sys, getopt
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
from datetime import date
import csv
from lib.tavuong_visual import *
from lib.tavuong_model import *
from lib.tavuong_readfile import *
from lib.user_visual import *
# VUONG SIMULATION
# ---LIB of system 
# ---VUONG ALGORITHM
#  Author: Dr. The Anh Vuong
# (c) 2020 by Dr.-The Anh Vuong
# Licence: MIT , Patent right is reserved
# ------------------------------------------
    
def vuong_covid_Model (ncasesfile,deathsfile,country_in, gesund,simu_mode,tau,recP,sw7):
# VUONG SIMULATOR 
# ---INPUT BLOCK

    x = [] # csv 0. Colum
    y = [] # csv 1. Colum
    nc = [] # new_case 1. Colum
    nd = [] # new_death 1. Colum
    y1 =[] # Csv 2. Colum  
    y2 =[] # buffer
    icountry = 0
    iland = 0 

#    fig, ax = plt.subplots()
    sname = ncasesfile

#    namecountry =""
    namecountry = country_in
    if namecountry == "": namecountry = input("KIT > country? ")

#--------------------------------
# country read
    icountry = tavuong_country_position(sname, namecountry,iland)
#    print ('after:' + str(icountry)+ str(iland))

# x, nc (time, newcase)
    x =  tavuong_read_timeseries(sname, icountry,x,nc,'x')
    nc = tavuong_read_timeseries(sname, icountry,x,nc,'nc')
#   print (nc)
#   tavuong_multi_ac(x,nc,'blue',label_text="")

# x, nd (time, newdeaths)

    sname = deathsfile
    nd = tavuong_read_timeseries(sname, icountry,x,nd,'nd')
#   print (nd)    
#   tavuong_multi_ac(x,nd,'red', label_text="")

    y = tavuong_timeseries_generator(x,y)
    y1 = tavuong_timeseries_generator(x,y1)
    y2 = tavuong_timeseries_generator(x,y2)
#----------------------------------------------------------
# Data Visualizing

#   Swwitch per Program
#    icontrol = 1
#    icontrol = 3
#    print(simu_mode,tau)
    ta_covid19_anlysis(x,nc,nd,y1,y2,gesund,namecountry,simu_mode,tau,recP,sw7)
    
    return()

def ta_covid19_anlysis(x,nc,nd,y1,y2,gesund,namecountry,control,tau,recP,sw7):
# VUONG SIMULATOR 
# ---Covid-data Analysis 
#  Author: Dr. The Anh Vuong
# (c) 2020 by Dr.-The Anh Vuong
# Licence: MIT , Patent right is reserved
#--------------------------------------------------
#   x [] datum
#   nc [] confirm Cases
#   nd [] deaths
#   y1[] buffer/ Reserved
#   y2[] buffer/ Reserved
#   namecountry = Choice Colume 
#   gesund = recovery factor
#   tau = Incubation Period
#   recP = Recovery Period
#   control = Analysis mode
#   sw7 = Swicht mode 7

    y = [] # Buffer
    y = tavuong_timeseries_generator(x,y)
    y3=[]
    y3 = tavuong_timeseries_generator(x,y3)

#    print (control)
    r=0 # dummy
    summe_t = 0.0
#   ------- control =1  ------------
    if (control==1):
#        cal_y(y1,nc,1,0)    
#        plt.plot(x,y1, label='infection (t)')

#        y2 = cal_vuomod(y1,nc,1,tau,0.)
#        summe_text ='Incub. ='+ str(tau) + '/ Est. inf.='
#        plt.plot(x,y1, label=summe_text)

        y2 = ta_norm (nc)
        summe_text ='Norm confirmed ' 
        plt.plot(x,y2, label=summe_text)

        y = cal_vuomod(y1,nc,1,tau,0.)
        y2 = ta_norm (y)
        summe_text ='R-Factor / Incub.P='+ str(tau) 
        plt.plot(x,y2, label=summe_text)
        
#        cal_y(y1,nd,1,0)    
#        plt.bar(x,y1, label='deaths')

#   ------- control =2   ------------
    
    if (control==2):
        summe_text ="confirmed Inf.= "
        summe_t = tavuong_plot_summe(x,y1,nc, summe_text,'')
    # plt.bar(x,y2, label='Sum infected')

        summe_text ="Deaths Cases= "
        summe_t = tavuong_plot_summe(x,y1,nd, summe_text,'')
        plt.bar(x,y1, label='')

#   ------- control =3   ------------

    if (control==3):

# 1. new daily cases
        summe_text ="confirmed Inf.= "
        summe_t = tavuong_plot_summe(x,y1,nc, summe_text,'')
#        print ('Summe case =', summe_t)    
# gesund = 0    
#        cal_yf(y1,y,2,tau,0)
#        cal_s(y2,y1,1,0,0)    
#        plt.plot(x,y2, label='Inf/ Incub='+ str(tau) + "fix R-F =2" )

        cal_sig(y1,nc,0,recP,gesund)    
        plt.plot(x,y1, label='Inf.- rec. R='+ str(recP) + "fix" + str (gesund) )

        cal_yg(y1,nc,0,recP,gesund)
        cal_s(y2,y1,1,0,0)    
        plt.plot(x,y2, label='rec. R='+ str(recP) + "fix" + str (gesund))

        summe_text ="Deaths Cases= "
        summe_t = tavuong_plot_summe(x,y1,nd, summe_text,'')
        plt.bar(x,y1, label='')

#   ------- control =4   ------------
    
    if (control==4):

        summe_text ="confirmed Inf.="
        summe_t = tavuong_plot_summe(x,y1,nc, summe_text,'')

#        cal_s(y1,nc,1,0,0)    
#        plt.plot(x,y1, label='Sume Cases')

#        cal_vuomod(y1,nc,2,7,0.0)
#        cal_s(y2,y1,1,0,0)    
#        plt.plot(x,y2, label='Inf (T=7,f:log')

        ta_recovery(y1,nc, nd, 1, recP, gesund)
        ta_active_Infection(y2,nc,y1)

        summe_text ='Reco.P ='+ str(recP) + '/ Est. Inf.='
        summe_t = tavuong_plot_summe(x,y,y2, summe_text,'')

#        cal_s(y1,y2,1,0,0)
#        plt.bar(x,y1, label='Recover / Period ='+ str(recP))
        
        summe_text ="Deaths Cases= "
        summe_t = tavuong_plot_summe(x,y1,nd, summe_text,'')
        plt.bar(x,y1, label='')

#   ------- control =5   ------------
    
    if (control==5):
#        summe_t = cal_s(y1,nc,1,0,0)
#        print ('Summe case =', summe_t)    
#        plt.plot(x,y1, label='Infection: '+ str(summe_t))
        summe_text ="confirmed Inf.="
        summe_t = tavuong_plot_summe(x,y1,nc, summe_text,'')
        #        print ('confirmed Inf.=', summe_t)    

# 
#        cal_yf(y1,nc,2,7,gesund)
#        cal_s(y2,y1,1,0,0)    
#        plt.plot(x,y2, label='Inf (ESt: 14, f=2)')

        cal_vuomod(y1,nc,1,tau,0.)
#        cal_s(y2,y1,1,0,0)    y
#        plt.plot(x,y2, label='Inf / Tau='+ str(tau))
        summe_text ='Incub.P ='+ str(tau) + '/ Est. inf.='
        summe_t = tavuong_plot_summe(x,y2,y1, summe_text,'')

#        cal_vuomod(y1,nc,2,7,gesund)
#        cal_s(y2,y1,1,0,0)    
#        plt.plot(x,y2, label='Inf (EST:7,f:log, fix gesund')

        cal_vuomod(y1,nc,1,tau,0.0)
        ta_recovery(y2,y1,nd, 1, recP, gesund)
        ta_active_Infection(y,y1,y2)
#        cal_s(y2,y,1,0,0)
#        plt.plot(x,y2, label='Inf/Recovery Period ='+ str(recP))

        summe_text ='Reco.P ='+ str(recP) + '/ Est. Inf.='
        summe_t = tavuong_plot_summe(x,y2,y, summe_text,'')


        summe_text ="Deaths Cases= "
        summe_t = tavuong_plot_summe(x,y1,nd, summe_text,'')
        plt.bar(x,y1, label='')
#   ------- control = 6   ------------
# MODE 6 ############## PUBLICATION TSD _ MEDIUM ########################
    if (control==6):
# 1. new daily cases
        summe_text ='confirmed Cases='
        summe_t = tavuong_plot_summe(x,y1,nc, summe_text,'')
#        print ('Summe case =', summe_t)    

# 2. extimate infection cases
# tau = 0 use the real cases
#        tau = 0
        if (tau!=0):
            cal_vuomod(y1,nc,1,tau,0.)
            summe_text ='Incub.P ='+ str(tau) + '/ Est. inf.='
            summe_t = tavuong_plot_summe(x,y2,y1, summe_text,'')
        else:
            ta_recovery_copy(y1,nc)

# 3. recovery cases after VUONG MODEL
        ta_recovery(y2,y1,nd, 1, recP, gesund)
        summe_text ='Reco.P ='+ str(recP) + '/ Est. recovery='
        summe_t = tavuong_plot_summe(x,y,y2,summe_text,'')

# 4. extimat infection after VUONG MODEL
        ta_active_Infection(y,y1,y2)
        summe_text ='Reco.P ='+ str(recP) + '/ Est. Inf.='
        summe_t = tavuong_plot_summe(x,y2,y, summe_text,'')

# 5 death cases
        summe_text ="Deaths Cases= "
        summe_t = tavuong_plot_summe(x,y1,nd,summe_text,'')
        plt.bar(x,y1, label='')

#   ------- control = 7 MULTI RUNs   ------------
#   ------- control = 71-76 for Country  --------
#   ------- control = 81-86 for Incubation Periods  --------
#   ------- control = 91-76 for Recovery Period  --------

# MOde 7 : 11.06.2020 -16-06-2020  --------------------------------------------------------------   
    if ((control==7) or (control==8)or (control==9)):

# 71. new daily cases
        if (sw7 == 1):
#  --------- absolute compare
#            summe_text ='['+ namecountry + '] confirmed Cases='
#            plt.plot(x,nc, label=summe_text)
#  --------- prozentual compare
            y2 = ta_norm (nc)
            summe_text ='['+ namecountry + '] confirmed Cases='
            plt.plot(x,y2, label=summe_text)

            return

# 72. Summe  cases
        if (sw7 == 2):
            summe_text ='['+ namecountry + '] confirmed Cases='
            summe_t = tavuong_plot_summe(x,y1,nc, summe_text,"")
            print ('Summe cases =', summe_t)    
            return
# 73. Active Case
# ----confirmed Cases
# ----Fix Gesund recovery 
        if (sw7 == 3):
            ta_recovery_copy(y1,nc)
            cal_yg(y2,nc,1, recP, gesund)
            ta_active_Infection(y,y1,y2)
            ta_recovery_copy(y3,y)
            if (control==7):
                summe_text ='['+ namecountry + '] f-Active='
            if (control==8):
                summe_text ='['+ namecountry + ' IP='+ str(tau)+ '] f-Active='
            if (control==9):
                summe_text ='['+ namecountry + ' RecP='+ str(recP)+ '] f-Active='
#            summe_text ='Country ='+ namecountry + '/ f-Active='
            summe_t = tavuong_plot_summe(x,y2,y3, summe_text, "")
            return        
# 74. unified active Case
# ----confirmed Cases
# ----Fix Gesund recovery
        if (sw7 == 4):
            ta_recovery_copy(y1,nc)
            cal_yg(y2,nc,1, recP, gesund)
            ta_active_Infection(y,y1,y2)
            y3 = ta_vuong_norm_s (y)
            if (control==7):
                summe_text ='['+ namecountry + '] f-Active (%)='
            if (control==8):
                summe_text ='['+ namecountry + ' IP='+ str(tau)+ '] f-Active (%)='
            if (control==9):
                summe_text ='['+ namecountry + ' RecP='+ str(recP)+ '] f-Active (%)='

#            summe_text ='Country ='+ namecountry + '/ f-Active (%)='
            summe_t = tavuong_plot_summe(x,y2,y3, summe_text, "")
            return        
# 75. VUONG-ALorithm : Active Cases
# ----estimated Infections cases 
# ----estimated  Gesund recovery
        if (sw7 == 5):
            cal_vuomod(y1,nc,1,tau,0.)
            ta_recovery(y2,y1,nd, 1, recP, gesund)
            ta_active_Infection(y,y1,y2)
            ta_recovery_copy(y3,y)
            if (control==7):
                summe_text ='['+ namecountry + '] V-Active='
            if (control==8):
                summe_text ='['+ namecountry + ' IP='+ str(tau)+ '] V-Active='
            if (control==9):
                summe_text ='['+ namecountry + ' RecP='+ str(recP)+ '] V-Active='

#            summe_text ='Country ='+ namecountry + '/ V-Active='
            summe_t = tavuong_plot_summe(x,y2,y3, summe_text, "")
#            plt.bar(x,y2, label='')
            return

# 76. VUONG-ALorithm : unified Active Cases
# ----estimated Infections cases 
# ----estimated  Gesund recovery
        if (sw7 == 6):
            cal_vuomod(y1,nc,1,tau,0.)
            ta_recovery(y2,y1,nd, 1, recP, gesund)
            ta_active_Infection(y,y1,y2)
            y3 = ta_vuong_norm_s (y)
            if (control==7):
                summe_text ='['+ namecountry + '] V-Active (%)='
            if (control==8):
                summe_text ='['+ namecountry + ' IP='+ str(tau)+ '] V-Active (%)='
            if (control==9):
                summe_text ='['+ namecountry + ' RecP='+ str(recP)+ '] V-Active (%)='

#            summe_text ='Country ='+ namecountry + '/ V-Active(%)='
            summe_t = tavuong_plot_summe(x,y2,y3, summe_text, "")
#           plt.bar(x,y2, label='')
#           plt.plot(x,y3, label=summe_text)
            return

# MOde 8: 11.06.2020 multy country ##########################   
    if (control==18):
# ----VUONG-ALorithm Prediction
        cal_vuomod(y1,nc,1,tau,0.)
        ta_recovery(y2,y1,nd, 1, recP, gesund)
        ta_active_Infection(y,y1,y2)

        summe_text ='Country ='+ namecountry + '/ V-Active='
        summe_t = tavuong_plot_summe(x,y2,y, summe_text, "")

# MOde 9: 12.06.2020 multy country Normierte ######################
# by Tau = 0 : use nc and recovery (nc , fix gesund)
# by Tau != 0 : use Vmodel with nc (Tau) and recovery (nd, recP)   
    if (control==19):
        if (tau == 0):
# Gesund after nc
            ta_recovery_copy(y1,nc)
            cal_yg(y2,nc,1, recP, gesund)        
        else:
# ---- VUONG-ALorithm Prediction
            cal_vuomod(y1,nc,1,tau,0.)
# ---- VUONG-ALorithm gesund function
            ta_recovery(y2,y1,nd, 1, recP, gesund)
        
# ---- VUONG-ALorithm extimate active cases
        ta_active_Infection(y,y1,y2)
        y3 = ta_vuong_norm_s (y)
        summe_text ='Country ='+ namecountry + '/ V-Active(%)='
        summe_t = tavuong_plot_summe(x,y2,y3, summe_text, "")
#        plt.plot(x,y3, label=summe_text)


    return {}

#-----------------------------------------------------
def cal_vuomod(yr,y, faktor, Tau, gesund) :
# VUONG SIMULATOR 
# --- Vuong Algorithm  Estimate infection cases 
#  Author: Dr. The Anh Vuong
# (c) 2020 by Dr.-The Anh Vuong
# Licence: MIT , Patent right is reserved
#--------------------------------------------------
#  faktor is fix R-factor is dummy here
#  Tau is incubation period. Tau = 0 : direct to nc data without estimation
#  gesund is fix recovery rate is dummy here


#   r-Factor File generator
    rfl = [] # log R-Factor buffer
    k = 0
    for k in y:
        rfl.append(0.0)    
# Preset of Simulator
    k = 0
    T = Tau + 7 # Window-wide for Caculation
    py2 = 0.0
    wa = 0
    wb = 0
    ya = 0
    yb = 0
    yr[0] = 0
    rfl[0] = 0.0
        
    for i in  y:
        wa = k-1
        wb = k-1 -T
        if (k <= T):
            py2 = 0.0
            rfl[k] = py2
            yr[k] = y[k]
        else:
            ya = y[wa]
            yb = y[wb]
            if (yb ==0) and  (ya!=0):
                py2 = rfl[k-1]
            if (yb ==0) and  (ya==0):
                py2 = 0.0
            if (yb !=0) and  (ya==0):
                py2 = rfl[k-1]
            if (yb !=0) and  (ya!=0):
                    py2 = np.log10(ya) - np.log10(yb)
                    py2 = py2 / float(T-Tau-1)
                    py2 = 10 **py2
            rfl[k] = py2
            yr[k] = py2*y[wa]                                    
            
#        print ("R-Factor:" + str(py2) + "--" + str(yr[k]) + "\r")
        k = k + 1
    return rfl
# -----------------------------------------------------------
def ta_recovery(yr,y, yd, faktor, recP, gesund) :
# VUONG SIMULATOR 
# ---- VUONG-Aligorithm: Calculation of recovery cases from daily deaths
#  Author: Dr. The Anh Vuong
# (c) 2020 by Dr.-The Anh Vuong
# Licence: MIT , Patent right is reserved
#--------------------------------------------------
#  faktor is fix R-factor is dummy here
#  Tau is incubation period. Tau = 0 : direct to nc data without estimation
#  gesund is fix recovery rate is dummy here
#  yr : Out put
#  y : inf cases
#  yd: deaths cases
#  in developping
    k = 0
    T = recP     # Recovery Period
    f = faktor  # f is generated, f=1 by Tau =0 
    yr[0] = 0
    py2 = 0.0
    rec_rate = 0.0  # recovery rate 
    for i in  y:       
        if k >T: 
            if (y[k-T] != 0):
                py2 = y[k-T] - yd[k]
                if (py2 <= 0):
                    py2 = 0.0
                else:
                    rec_rate = 1.0 / py2
#                print ("Recovery factor:" + str(rec_rate) + "--" + str(y[k]) + "\r")
            else:
                py2 = 0.0
        else:
            py2 = 0.0
            
        yr[k] = py2  # - gesund     
        if (y[k] <= 0): py2 = 0.0
       
#        print ("Recovery factor:" + str(f) + "\r")
        k= k+1    
    return

def ta_active_Infection(r,x,y):
# VUONG SIMULATOR 
# ---- VUONG-Aligorithm: Calculation of active cases 
#      from Estim. Infection & Gesund function
#  Author: Dr. The Anh Vuong
# (c) 2020 by Dr.-The Anh Vuong
# Licence: MIT , Patent right is reserved
#--------------------------------------------------
# r = rest Infection
# x = infection cases
# y = recovered cases
    k = 0
    for i in x:
        r [k] = x[k] - y[k]
#        print (str(k) + ":"+ str(r[k])) 
        k= k+1   
    return

def ta_recovery_copy(r,x):
# r = rest Infection
# x = infection cases
# y = recovered cases
    k = 0
    for i in x:
        r [k] = x[k]        
#   print (str(k) + ":"+ str(r[k])) 
        k= k+1   
    return

def ta_para_read(text_req, read_in, default):
    
#    text_req1 = 'VMODEL >' 
    text_req1 = text_req
    para_read = ''

    if (read_in == ''):
        read_in = input (text_req1)
        if (read_in != '') :
            return read_in
        else:
            return default
    return read_in

def ta_norm (y):
# VUONG SIMULATOR 
# ---- VUONG-Aligorithm: unified calculation 
#  Author: Dr. The Anh Vuong
# (c) 2020 by Dr.-The Anh Vuong
# Licence: MIT , Patent right is reserved
#--------------------------------------------------
# y: input
# y3 = ta_norm : calculead output

# y3 generated
    y3 = [] 
    k = 0
    for k in y:
        y3.append(0.0)    

#------ y3 = Acummulated y []---    
    k = 0
    summe = 0         
    y3np = np.matrix(y) 
    y3max = y3np.max() 
    print('max=', y3max)
    for i in y:
        y3[k] = 100*y[k]/y3max
        k = k+1
    return y3
     
def ta_vuong_norm_s (y):
# Covid19 _VuongSimulator 
# ---- VUONG-Aligorithm: Normalyse Summe function 
#  Author: Dr. The Anh Vuong
# (c) 2020 by Dr.-The Anh Vuong
# Licence: MIT , Patent right is reserved
#--------------------------------------------------
# y: input
# y3 = ta_norm : calculead output

# y3 generated
    y3 = [] 
    k = 0
    for k in y:
        y3.append(0.0)    

#------ y3 = Acummulated y []---    
    k = 0
    summe = 0         
    for i in y:
        summe = y[k] + summe
        y3[k] = summe
        k = k+1
#------- Maximal search --------
    y3np = np.matrix(y3) 
    y3max = y3np.max() 
    summe = y3max

    k = 0
    ywert = 0.0
    for i in y:
        ywert = y [k]      
        y3[k] = 100.0*ywert/summe

        k = k+1    
    return y3 