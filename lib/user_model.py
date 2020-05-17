# user_model.py
# Bibliotkek für Data Visualizing
# Author : Dr.-Ing. The Anh Vuong
#        + your Name 
# Basis Structur

import math
import numpy as np

# my_model_1(ys,y,faktor, Tau)
#   y [] input data /e.g. Case nummer
#   ys [] out put data / e.g. of accoumulate cases  
#   Faktor: ys [k] = summe Faktor * y[k]
#   Tau : Delaytime / Incubazion time 

def my_model_1(ys,y, faktor, Tau) :
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



