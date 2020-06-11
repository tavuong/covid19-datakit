# tavuong_visual.py
# Bibliotkek für Data Visualizing
# Author : Dr.-Ing. The Anh Vuong
# Basis Structur
# tavuong_collection(x,y,y1,y2,namecountry)
#   x [] datum
#   y [] case Data 
#   y1[] buffer/ Reserved
#   y2[] buffer/ Reserved
#   Name of Choice Colume 
import sys, getopt
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
from datetime import date
from lib.tavuong_model import *

# ------------------------------------------   
# PLOT Models 
def tavuong_collection_gc(x,y,y1,y2,gesund):
# ----Actualcase ----------------------------------
#   x [] datum
#   y [] case Data 
#   y1[] buffer/ Reserved
#   y2[] buffer/ Reserved
#   namecontry = Choice Colume 

#  direct plot Y(x)
#  plt.bar(x,y, color ="green", label='infection (t)')
#  using tavuong_model y1(y(x))
    cal_y(y1,y,1,0)    
    plt.plot(x,y1, color="blue", label='actual cases')

    rprod= 2.5
    cal_yf(y1,y,rprod,7,gesund)    
    plt.plot(x,y1, color="red", label='fix Reprod + Recov. (estim.)' )

    cal_yg(y1,y,0,14,gesund)    
    plt.plot(x,y1, color="green", label='Recov. (estim.)')

    return{}
def tavuong_collection_gs(x,y,y1,y2,gesund):
# ----Actualcase ----------------------------------
#   x [] datum
#   y [] case Data 
#   y1[] buffer/ Reserved
#   y2[] buffer/ Reserved
#   namecontry = Choice Colume 

#  direct plot Y(x)
#    plt.bar(x,y, color ="green", label='infection (t)')
#  using tavuong_model y1(y(x))
    r=0 # dummy
    cal_s(y1,y,1,0,0)    
    plt.plot(x,y1, label='Infection')
# gesund = 0    
#    cal_yf(y1,y,2,7,0)
#    cal_s(y2,y1,1,0,0)    
#    plt.plot(x,y2, label='estimated (2f,7,0)' )

    cal_sig(y1,y,0,14,gesund)    
    plt.plot(x,y1, label='Inf. + Recov. (estim.)' )

    cal_yg(y1,y,0,14,gesund)
    cal_s(y2,y1,1,0,0)    
    plt.plot(x,y2, label='Recov. (estim.)')

    return{}

def tavuong_collection_ac(x,y,y1,y2):
# ----Actualcase ----------------------------------
#   x [] datum
#   y [] case Data 
#   y1[] buffer/ Reserved
#   y2[] buffer/ Reserved
#   namecontry = Choice Colume 

#  direct plot Y(x)
#    plt.bar(x,y, color ="green", label='infection (t)')
#  using tavuong_model y1(y(x))
    r=0 # dummy
    cal_y(y1,y,1,0)    
    plt.bar(x,y1, label='infection (t)')
    
#    cal_yf(y1,y,2,7,0)    
#    plt.plot(x,y1, label='estimated (2f,7)' )
#
#    cal_yr(y1,y,r,7,0)    
#    plt.plot(x,y1, label=' estimate (r,7)')

    return{}


def tavuong_collection_sr(x,y,y1,y2):
# ------------------------------------------   
#   gesund = recovery faktor
#   summing data

    r=0 # dummy

    cal_s(y2,y,1,0,0)
#    plt.plot(x,y2, label='Sum(0)')
    plt.bar(x,y2, label='Sum infected')
    
#    cal_yr(y1,y,r,7,0)    
#    cal_s(y2,y1,1,0,0)
#    plt.plot(x,y2, label='Sum estimate (r,7)')
    
#    cal_yf(y1,y,2,7,0)    
#    cal_s(y2,y1,1,0,0)
#    plt.plot(x,y2, label='Sum estimated (2f,7)' )
    
    
    return{}

def tavuong_collection_rf1(x,y,y1,y2,gesund):
# ------------------------------------------   
#   IN DEVEKOPPING 
#   faktor = R -Factor Fix or realtiv
#   Tau = Incubation period
#   gesund = recovery rate
#  
#   normal Cases
#    cal_y(y1,y,1,0)    
#    plt.plot(x,y1, label='infection (t)')

#   recovered factor gesund is fix
#   reproduction rprod is fix    
    rprod = 2
    cal_rf0(y2,y,rprod,7,gesund)    
    plt.plot(x,y2,label='Recovered-Linear Model')

#   recovered factor is  modeled

    cal_rf1(y2,y,rprod,7,gesund)    
    plt.plot(x,y2,label='Recovered-Exponet Model')
    
    
    return{}
# -----------------------------------------
# Summing and plot up Verison 1.8  Simulator
# summ_color '#eeefff' HEX String
# 'b'  blue
# 'g'  green
# 'r'  red
# 'c'  cyan
#'m'   magenta
#'y'   yellow
#'k'   black
#'w'    white
# by "" Automatic

def tavuong_plot_summe(x,ys,y, summe_text,summe_color):

#   (x,y) --> (x, ys= summe (y))
    summe_t = 0    
    summe_t = cal_s(ys,y,1,0,0)
    summe_text = summe_text + str(int(summe_t))  
    print ('Vuong_Simulator >' + summe_text)
    if (summe_color ==""):
        plt.plot(x,ys, label=summe_text)
    else:
        plt.plot(x,ys, label=summe_text, color=summe_color)
    return summe_t

def kit_plot_test2(t,x):
    
    plt.plot(t,x, color ="green", label="test")
    plt.bar(t,x, color ="blue", label="test")
    plt.scatter(t,x, color ="red", label="test")
    return{}

# ------------------------------------------   
# PLOT Multi Country 
def tavuong_multi_ac(t,x,color_text, label_text):
# Multicall    
    plt.plot(t,x, color =color_text, label=label_text)
#    plt.bar(t,x, color ="blue", label="test")
#    plt.scatter(t,x, color ="red", label="test")
    return{}

def tavuong_multi_s(x,y,y1,y2,color_text, label_text):
#   faktor = R -Factor Fix or realtiv
#   Tau = Incubation period
#   gesund = recovery rate
#   summing data

    cal_s(y2,y,1,0,0)
    plt.plot(x,y2,color =color_text, label=label_text)
#    plt.bar(x,y2, label='Sum infected')    
    return{}

# ------------------------------------------   
# PLOT Template 
def show_curve(ax,sname,namecountry,outputfile):
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
#    plt.xlabel('date')
    plt.ylabel('values')
    plt.title('KIT: '+ sname +' ['+ namecountry + ']')

#   Credit for corona19-data-kit.  
    ax.text(1.0, -0.1, 'powered by Dr.-Ing. The Anh Vuong',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='blue', fontsize=10)

#   JPEG-file output or for  TERMUX
#    out_png = outputfile
    out_png = ''
    out_png = outputfile
    if (out_png != ''):
        plt.savefig(out_png, dpi=150)
        print ('plot: ',out_png)

    plt.show()


# ------------------------------------------   
# backup for plot development
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
#    output for TEXMUX
#    out_png = 'covid19_kit_output.png'
#    plt.savefig(out_png, dpi=150)

    return{}


