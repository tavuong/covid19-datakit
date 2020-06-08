# covid19-VuongSimulator
[![N|](https://vuongblog.files.wordpress.com/2020/05/git_pt_vuong60.png)](https://vuongblog.wordpress.com)

## Publication
[towards datas cience](https://towardsdatascience.com/prediction-and-analysis-of-covid-19-data-model-proposal-algorithm-vuong-simulator-2b05d1bded7e)  Prediction and Analysis of COVID-19 Data: Model — Proposal Algorithm- Vuong Simulator, 07.06.2020

[Codvid19- Datakit WIKI](https://github.com/tavuong/covid19-datakit/wiki) Info for using
## Description:
- Vuong-Algorith for prediction of unrecovered Infection cases.
- Analyze the corfimed  and Deaths
- Prediction of Infections case 
- All analysis methods in tavuong_model.py are models for reasearch, could giving non-real statements.

## Features:
- Program: covid19-VuongSimulator.py: dashboard / Command-line
- Input: data source and Parameter
- Modeling:     ./lib/tavuong_simulator.py,  ./lib/tavuong_model.py (default)
- Visualizing : ./lib/tavuong_model.py (default)

# Install - Data prepare - Start 
## Install Covid19-datkit
```sh
$ git clone https://github.com/tavuong/covid19-datakit.git
$ cd ~/covid19-datakit
$ pip install matplotlib
$ pip install mumpy
```
# data prepare: 
```sh
$ cd ~/covid19-datakit/
```
- copy csv-file to ./data (e.g. new_cases.csv) 
- You could find [here Data Sources](https://ourworldindata.org/coronavirus-source-data) or from other public source 

## covid19-datakit.py start & dialog
### input format:
```sh
By direct input : 
Name could have sape and dont put in '', eg. United States, United Kingdom
Nummer  musst be  in '', e,g, '0,78'

By command line
Parmeters (Name, number)  must be in ''
```

### Direct start with dialog
```sh
$ cd ~/covid19-datakit
$ python covid19-VuongSimulator.py
```
$ cd ~\covid19-data-kit\
$ python .\covid19-VuongSimulator.py [by PC]
VMODEL > country? World
VMODEL > new_case-file ? ./data/new_cases.csv
VMODEL > deaths-file ? ./data/new_deaths.csv
VMODEL > VuongSimualtion mode ? 6
VMODEL > Incubation Period? 7
VMODEL > Recovery Period ?14
Curve will be shown!

### command line
```sh
usage: covid19-VuongSimulator.py -n <new_case-file> -d <deaths-file> -o <outputfile> -[c/t/g/s} 

$ python .\covid19-VuongSimulator.py -h
-n <new_Cases_file> -d <new_Deaths_file> -o outputfile
-c country
-t Incubation Period Tau
-r Recovery Period
-s simulation mode
The Programm calculates and plots according to simulation-mode. Only in mode 1 is time function, in other modes, accumulate of time functions are shown
1 : R-factor after Vuong Modell (in development)
2: confirmed Infection nc[x] — Deaths nd [x]
3: confirmed Infection nc[x] / recovery Function G[x]
/ final estimated Infection I[x] /Deaths nd [x]
4 : confirmed Infection nc[x] — Recovery Function G[x]
Deaths nd [x]
5: confirmed Infection nc[x] / estimated Infection Ip[x]
/ final estimated Infection I[x] /Deaths nd [x]
6: confirmed Infection nc[x] / estimated Infection Ip[x]
/ Recovery Function G[x]
/ final estimated Infection I[x] /Deaths nd [x]
```

Project : covid19-datakit
----
Author: Dr.-Ing. The Anh Vuong 

Copyright (c) 2020 Dr.-Ing. The Anh Vuong , Germany

License: MIT
