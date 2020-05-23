# user_visual.py
# Bibliotkek für Data Visualizing
# Author : Dr.-Ing. The Anh Vuong
#          + your Name
# Basis Structur
# my_collection_x(x,y,y1,y2,namecountry)
#   x [] datum
#   y [] case Data 
#   y1[] buffer/ Reserved for model calculation
#   y2[] buffer/ Reserved for visual calculation
#   Name of Choice Colume 

import matplotlib.pyplot as plt

from lib.tavuong_model import *
from lib.user_model import *

def my_collection_1(x,y,y1,y2,namecountry,gesund):
# --My Block_case Visual ---------------------------------------   
#   Model : my_model_1(y2,y,1,0) : accumulate of cases 
#   faktor = R -Factor Fix or realtiv
#   Tau = Incubation period
#   gesund = recovery rate

    r=0 # dummy

#  using tavuong_model y1(y(x))
    r=0 # dummy
    cal_y(y1,y,1,0)    
    plt.bar(x,y1, label='tavuong_model:infection (t)')

#  using user_model y1(y(x))
    factor = 0.1
    Tau = 0
    my_model_1(y2,y,factor,Tau,gesund)
    plt.plot(x,y2, label='user_model: accumulated /10')

    return{}



