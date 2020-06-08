# covid19-datakit
[![N|](https://vuongblog.files.wordpress.com/2020/05/git_pt_vuong60.png)](https://vuongblog.wordpress.com)

## Publication
[towards datas cience](https://towardsdatascience.com/python-development-kit-for-visualizing-and-modelling-of-covid19-data-b33e7a13aace)  Python Development Kit for Visualizing and Modelling covid19-data. Dr. The Anh Vuong, 24.05.2020

[towards datas cience](https://towardsdatascience.com/prediction-and-analysis-of-covid-19-data-model-proposal-algorithm-vuong-simulator-2b05d1bded7e)  Prediction and Analysis of COVID-19 Data: Model — Proposal Algorithm- Vuong Simulator, 07.06.2020

[Codvid19- Datakit WIKI](https://github.com/tavuong/covid19-datakit/wiki) Info for using
## Description:
- Development kit for Covid-Data Analysis and Visualization.
- User could develop his own model in user_model.py
- User could develop his own presentation in user_visual.py 
- All analysis methods in tavuong_model.py are models for reasearch, could giving non-real statements.

## Features:
- Program: covid19-datakit.py : dashboard
- Input: data source and Parameter
- Modeling:     ./lib/user_model.py ./lib/tavuong_model.py (default)
- Visualizing : .lib/user_visual.py ./lib/tavuong_model.py (default)

# Install - Data prepare - Start 
## Install
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
$ python covid19-datakit.py
```
- Case data file: ./data/new_cases.csv or ("return" for using default data for testing) 
- Country: Name_of Country in list
- What is your calculate-model? me (or: ac, sr, t2 from tavuong_visual.py)

Curve will be shown!

### command line
```sh
usage: covid19-datakit.py -i <inputfile> -o <outputfile> -[c/m/g} 

$ python .\covid19-datakit.py -h
covid19-datakit
-i <inputfile> -o <outputfile>
-c country
-m mode
-g recover  
```
## covid19-VuongSimulator.py
[Codvid19-VuongSimulator](https://github.com/tavuong/covid19-datakit/README_VuongSimulator.md) VuongSimulator README

Project : covid19-datakit
----
Author: Dr.-Ing. The Anh Vuong 

Copyright (c) 2020 Dr.-Ing. The Anh Vuong , Germany

License: MIT
