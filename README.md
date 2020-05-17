# covid-data-kit
[![N|](https://vuongblog.files.wordpress.com/2020/05/git_power1_vuong-1.png)](https://vuongblog.wordpress.com)
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

- copy csv.file in ./data 
- You could find [here [Data Sources](https://ourworldindata.org/coronavirus-source-data)] or from other public source 

## program covid_kid_App1.py & dialog
$ python covid_kid_1.py

- Case data file: ./data/new_cases.csv or ("return" for using default data for testing) 
- Country: Name_of Country in list
- What is your calculate-model? me (my model / tavuong_model,py: ac,sr,t2)

Curve will be shown!

## program covid_kid_Ap2.py & dialog
In development

Project : Covid-data-kit
----
Author: Dr.-Ing. The Anh Vuong 

Copyright (c) 2020 Dr.-Ing. The Anh Vuong , Germany

License: MIT
