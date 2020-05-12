# tavuong_visual.py
# Bibliotkek für Data Visualizing
# Author : Dr.-Ing. The Anh Vuong
# Basis Structur
# myBlock_case(x,y,y1,y2,namecountry)
#   x [] datum
#   y [] case Data 
#   y1[] buffer/ Reserved
#   y2[] buffer/ Reserved
#   Name of Choice Colume 

import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
from datetime import date
from lib.tavuong_model import *

def block_case_ac(x,y,y1,y2,namecountry):
# ----Actualcase ----------------------------------
#   x [] datum
#   y [] case Data 
#   y1[] buffer/ Reserved
#   y2[] buffer/ Reserved
#   namecontry = Choice Colume 
    r=0 # dummy
    fig, ax = plt.subplots()

    plt.bar(x,y, color ="green", label='infection (t)')
#   ax.plot(x,y)           

    show_curve(ax,namecountry)
    return{}


def block_case_ca(x,y,y1,y2,namecountry):
# ----Number of Case ----------------------------------
#   faktor = R -Faktor Fix or realtiv
#   Tau = delay time
#   gesund = recovery faktor
#   actuell data
#   cal_y(y1,y,faktor,Tau)
#   cal_yr(y1,y,faktor,Tau,gesund)
    r=0 # dummy
    fig, ax = plt.subplots()

    plt.plot(x,y, color ="green", label='infection (t)')
#   ax.plot(x,y)           

    cal_yr(y2,y,r,7,0)
    plt.plot(x,y2, color ="red", label='Estimate (7)')

    cal_yf(y2,y,2,7,0)    
    plt.plot(x,y2, label='Sum estimated (2f,7)' )

#   ax.plot(x,y2)

    show_curve(ax,namecountry)
    return{}

def block_case_sr(x,y,y1,y2,namecountry):
# ------------------------------------------   
#   faktor = R -Faktor Fix or realtiv
#   Tau = delay time
#   gesund = recovery faktor
#   summing data
#   cal_s(y1,y,faktor,Tau)
#   cal_sr(y1,y,faktor,Tau,gesund)

    r=0 # dummy
    fig, ax = plt.subplots()

    cal_s(y2,y,1,0)
#    plt.plot(x,y2, label='Sum(0)')
    plt.bar(x,y2, label='Sum infected')
    
    cal_yr(y1,y,r,7,0)    
    cal_s(y2,y1,1,0)
    plt.plot(x,y2, label='Sum estimate (r,7)')
    
    cal_yf(y1,y,2,7,0)    
    cal_s(y2,y1,1,0)
    plt.plot(x,y2, label='Sum estimated (2f,7)' )
    
    
    show_curve(ax,namecountry)
    return{}


# PLOT TEST
def corona_plot_test(t,x):
    
    fig, ax = plt.subplots()
    plt.plot(t,x, color ="green", label="test")
    plt.bar(t,x, color ="blue", label="test")
    plt.scatter(t,x, color ="red", label="test")
#   ax.plot(t,x, color="green")
    ax.set_ylabel(r"Covid19-data-kit", color='green', rotation='horizontal')
    ax.yaxis.set_label_position('right')

    ax.legend()
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    ax.xaxis.set_minor_locator(matplotlib.dates.MonthLocator((1,2,3,4,5,6,7,8,9,10,11,12)))

    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("\n%Y"))
    ax.xaxis.set_minor_formatter(matplotlib.dates.DateFormatter("%d-%b"))
    plt.setp(ax.get_xticklabels(), rotation=0, ha="center")

    plt.show()
    return{}

def show_curve(ax,namecountry):
#    t = [date.fromisoformat('2016-01-01'), date.fromisoformat('2017-12-31')]
#    x = [0,1]
#    print (t)
#    ax.plot(t,x)
#    fig, ax = plt.subplots()
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    ax.xaxis.set_minor_locator(matplotlib.dates.MonthLocator((1,2,3,4,5,6,7,8,9,10,11,12)))
    
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("\n%Y"))
    ax.xaxis.set_minor_formatter(matplotlib.dates.DateFormatter("%d-%b"))
    
    plt.setp(ax.get_xticklabels(), rotation=0, ha="center")
    ax.legend()    
    plt.xlabel('date')
    plt.ylabel('cases / factor')
    plt.title('Corona Calculator ' + namecountry)
    plt.show()



