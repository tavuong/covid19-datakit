# user_visual.py
# Bibliotkek für Data Visualizing
# Author : Dr.-Ing. The Anh Vuong
#          + your Name
# Basis Structur
# my_collection_x(x,y,y1,y2,namecountry)
#   x [] datum
#   y [] case Data 
#   y1[] buffer/ Reserved
#   y2[] buffer/ Reserved
#   Name of Choice Colume 

import matplotlib.pyplot as plt

from lib.tavuong_model import *
from lib.user_model import *

def my_collection_1(x,y,y1,y2,namecountry):
# --My Block_case Visual ---------------------------------------   
#   Model : my_model_1(y2,y,1,0) : accumulate of cases 
#   faktor = R -Faktor Fix or realtiv
#   Tau = delay time
#   gesund = recovery faktor

    r=0 # dummy

#  using tavuong_model y1(y(x))
    r=0 # dummy
    cal_y(y1,y,1,0)    
    plt.bar(x,y1, label='tavuong_model:infection (t)')

#  using user_model y1(y(x))
    factor = 0.1
    Tau = 0
    my_model_1(y2,y,factor,Tau)
    plt.plot(x,y2, label='user_model: accumulated /10')

    return{}



