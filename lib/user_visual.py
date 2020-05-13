# user_visual.py
# Bibliotkek für Data Visualizing
# Author : Dr.-Ing. The Anh Vuong
# Basis Structur
# my_collection_x(x,y,y1,y2,namecountry)
#   x [] datum
#   y [] case Data 
#   y1[] buffer/ Reserved
#   y2[] buffer/ Reserved
#   Name of Choice Colume 

import matplotlib.pyplot as plt
#import matplotlib.dates
#from datetime import datetime
#from datetime import date
from lib.tavuong_model import *

def my_collection_1(x,y,y1,y2,namecountry):
# --My Block_case Visual ---------------------------------------   
#   faktor = R -Faktor Fix or realtiv
#   Tau = delay time
#   gesund = recovery faktor

    r=0 # dummy

#   plot y(x) = x(t)
    plt.bar(x,y, color ="green", label='infection (t)')

    cal_s(y2,y,1,0)
#    plt.plot(x,y2, label='Sum(0)')
    plt.plot(x,y2, label='Sum infected')

    return{}



