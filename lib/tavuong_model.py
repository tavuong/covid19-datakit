# tavuong_model.py
# Model Bibliotkek für Data processing
# Author : Dr.-Ing. The Anh Vuong
# Basis Structur
# cal_myfunction(yc,y, faktor, Tau)
# yc[] = cal_myfunction(y[],factor,Tau, gesund)
# factor = Productionsfaktor
# Tau = Delay time/ Incubation
# gesund = gesundfactor

import math
import numpy as np
def cal_y(yc,y, faktor, Tau) :
#  model0 :fix faktor (t > Tau)
    k = 0
    T = Tau
    f = faktor
    py2= 0
    for i in  y:
        if k >T: 
            py2 = y[k-T]*f
        else:
            py2 = y [k]
        
        yc[k] = py2       
#       print (y[k] , py2, yc [k])
        k= k+1    
    return{}

def cal_yr(ys,y, faktor, Tau, gesund) :
# model: variabel faktor (t>Tau) + gesund faktor

    k = 0
    T = Tau
    f = faktor
    py2 = 0.0
#    gesund = 0
# linear Model                
    
    for i in  y:       
        if k >T: 
            if (y[k-T] != 0):
                f = y[k-1] / y[k-T]
            else:
                f = 0

        else:
            f =0
        
        if (k!=0): 
            ys[k] = y[k -1]*(f-gesund)
        else: 
            ys [k] = 0
#        print (f, y[k] , py2, ys [k])
        k= k+1    
    return{}

def cal_yf(ys,y, faktor, Tau, gesund) :
# model: fix faktor (t>Tau) + gesund faktor

    k = 0
    T = Tau     # Dummy
#    f = faktor  # Fix faktor
    py2 = 0
    for i in  y:       
        if k >T: 
            f = faktor
#           print (f, y[k] , py2)
        else:
            f = 0  
        
        if (k!=0): 
            ys[k] = y[k -1]*(f-gesund)
        else: 
            ys [k] = 0
#        print (f, y[k] , py2, ys [k])
        k= k+1    
    return{}

def cal_yg(yg,y, faktor, Tau, gesund) :
# model: gesund / immun curve calculate

    k = 0
    T = Tau     # Dummy
#    f = faktor  # Fix faktor
    py2 = 0
    g = gesund
    for i in  y:       
        if (k ==0): 
            yg [0]=0
        else:
            if k >T: 
                yg[k] = y[k -T]*gesund
#           print (f, y[k] , py2)
            else:
                yg[k] = 0  
        
#        print (f, y[k] , py2, ys [k])
        k= k+1    
    return{}
def cal_sig(ys,y, faktor, Tau, gesund) :
# model: Infection - gesund sume curve calculate
    py2 = 0 #Infaktion part
    py3 = 0 #Gesund part
    k = 0
    T = Tau
    for i in  y:
        py2 = y[k] + py2
        if (y[k] > 0):
            if (k>T):
                py3 = y[k -T]*gesund + py3
        ys[k] = py2 -py3
 #       print (y[k] , py2, ys [k])
        k= k+1    
    return{}

def cal_s(ys,y, faktor, Tau, gesund) :
# model: summe y(k) ,  time delay and fix faktor
#   Dummy for smae Structture:
#   Tau delay
#   faktor multicator
#   gesund reduction factor
#    ys[0] = 0
    py2 = 0
    k = 0

    for i in  y:
        py2 = y[k] + py2
        ys[k] = py2       
 #       print (y[k] , py2, ys [k])
        k= k+1    
    return{}

def cal_rf0(ys,y, faktor, Tau, gesund) :
# model: variabel faktor (t>Tau) + gesund faktor

    k = 0
    T = Tau
    f = faktor
    py2 = 0.0
    gesund = 0
# linear Model                
    
    for i in  y:       
        if k >T: 
            if (y[k-T-1] != 0):
                f = y[k-1] / y[k-T-1]
            else:
                f = 1 

        else:
            f =0
        
        ys[k] = f - gesund
#        print (f, y[k] , py2, ys [k])
        k= k+1    
    return{}

def cal_rf1(yr,y, faktor, Tau, gesund) :
# model: time delay and relative faktor
# exponential model
# in developping
    k = 0
    T = Tau
    f = faktor # f is generated, f=1 by Tau =0 
    yr[0] = 0
    py2 = 0.0
#   gesund is faktor 
    for i in  y:       
        if k >T: 
            if (y[k-T] != 0):
# linear model
#                f = y[k-1] / y[k-T-1]
# exponent model
                if (y[k] == 0):
                    f=0
                else:
                    py2 = np.log10(y[k]) - np.log10(y[k-T])
                    py2 = 10**py2
                    f = py2
#                print ("R-Factor:" + str(f) + "--" + str(y[k]) + "\r")
            else:
                f = 0
        else:
            f = 0
            
        yr[k] = f # - gesund     
        
       
#        print ("R-Factor:" + str(f) + "\r")
        k= k+1    
    return{}
