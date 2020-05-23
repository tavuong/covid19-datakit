# user_model.py
# Bibliotkek für Data Visualizing
# Author : Dr.-Ing. The Anh Vuong
#        + your Name 
# Model Template
# yc(x)  = function(y(x), reprod, Incubation Period, recovery rate)
#          x = date time
# implement  
# yc[] = my_model_x(y[],faktor,Tau, gesund)
#   faktor = R -Factor Fix or realtiv
#   Tau = Incubation period
#   gesund = recovery rate

import math
import numpy as np

def my_model_1(ys,y, faktor, Tau, gesund) :
# model: summe y(k) ,  time delay and fix faktor

    k = 0
    T = Tau   #  Dummy 
    f = faktor  # Dummy
    ys[0] = 0
    py2 = 0
    for i in  y:
        py2 = y[k]*faktor + py2
        ys[k] = py2       
 #       print (y[k] , py2, ys [k])
        k= k+1    
    return{}



