# covid-data-kit

## Description:
A development kit for Covid-Data Analysis and Visualization
## Features:
- Program: covid_kit_1.py
- Input: data source and Parameter
- Modeling:     ./lib/user_model.py ./lib/tavuong_model.py (default)
- Visualizing : .lib/user_visual.py ./lib/tavuong_model.py (default)

## install
$ git clone https://github.com/tavuong/covid19-data-kit.git
## data prepare: 
$ cd ~/covid-data-kit/
copy csv.file in ./data 
You could find [here [Data Sources](https://ourworldindata.org/coronavirus-source-data)] or from other public source 
## lib install
$ cd ~/covid-data-kit
$ pip install matplotlib
$ pip install mumpy

## program covid_kid_1.py & dialog
$ python covid_kid_1.py

Case data file: ./data/new_cases.csv or blank for default 
| Visualization model                  |
| ac : actual case                     |
| sr : summe of cases                  |
| me : my model                        |
| t2 : test plot                       |
What is your calculate-model? me

# Status
- all methods in tavuong_lib.py, user_lib.py  are  models could giving non-real statements.
- This Project is in development

Project : Covid-data-kit
----
Author: Dr.-Ing. The Anh Vuong [![N|](https://vuongblog.files.wordpress.com/2020/05/vuong_thumb.png)](https://vuongblog.wordpress.com)

Copyright (c) 2020 Dr.-Ing. The Anh Vuong (tavuong)

License: MIT
