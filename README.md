# covid19-datakit
[![N|](https://vuongblog.files.wordpress.com/2020/05/git_pt_vuong60.png)](https://vuongblog.wordpress.com)

## Description:
- Development kit for Covid-Data Analysis and Visualization.
- User could develop his owner model in user_model.py
- User could develop his owner presentation in user_visual.py 
- All analysis methods in tavuong_model.py are models for reasearch, could giving non-real statements.

## Features:
- Program: covid19-datakit-app1.py,covid19-datakit-app2.py
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

## covid19-datakit-app1.py start & dialog
### Direct to dialog
```sh
$ cd ~/covid19-datakit
$ python covid19-datakit-app1.py
```
- Case data file: ./data/new_cases.csv or ("return" for using default data for testing) 
- Country: Name_of Country in list
- What is your calculate-model? me (or: ac, sr, t2 from tavuong_visual.py)

Curve will be shown!

### command line
```sh
usage: covid19-datakit-app1.py -i <inputfile> -o <outputfile>
```
- inputfile :  Data-csv-file
- outputfile : png-file of plot  
  
## covid19-datakit-app2.py start & dialog
In development

Project : covid19-datakit
----
Author: Dr.-Ing. The Anh Vuong 

Copyright (c) 2020 Dr.-Ing. The Anh Vuong , Germany

License: MIT
