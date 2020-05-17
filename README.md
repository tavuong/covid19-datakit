# covid-data-kit
[![N|](https://vuongblog.files.wordpress.com/2020/05/git_pt_vuong60.png)](https://vuongblog.wordpress.com)
## Description:
A development kit for Covid-Data Analysis and Visualization
## Features:
- Program: covid_kit_1.py
- Input: data source and Parameter
- Modeling:     ./lib/user_model.py ./lib/tavuong_model.py (default)
- Visualizing : .lib/user_visual.py ./lib/tavuong_model.py (default)

## Status
- all methods in tavuong_lib.py, user_lib.py  are  models could giving non-real statements.
- This Project is in development

# Install
## download
$ git clone https://github.com/tavuong/covid19-data-kit.git

## lib install (for first time)
$ cd ~/covid-data-kit
$ pip install matplotlib
$ pip install mumpy

## data prepare: 
$ cd ~/covid-data-kit/

- copy csv-file to ./data (e.g. new_cases.csv) 
- You could find [here Data Sources](https://ourworldindata.org/coronavirus-source-data) or from other public source 

## covid_kit_App1.py start & dialog
covid_app1.py : app for visualizing of data cases (csv-files in ./data). It could be using also to develop your own presentation.  

$ cd ~/covid-data-kit

$ python covid_kit_1.py

- Case data file: ./data/new_cases.csv or ("return" for using default data for testing) 
- Country: Name_of Country in list
- What is your calculate-model? me (my model / tavuong_model,py: ac,sr,t2)

Curve will be shown!

## covid_kit_Ap2.py start & dialog
In development

Project : Covid-data-kit
----
Author: Dr.-Ing. The Anh Vuong 

Copyright (c) 2020 Dr.-Ing. The Anh Vuong , Germany

License: MIT
