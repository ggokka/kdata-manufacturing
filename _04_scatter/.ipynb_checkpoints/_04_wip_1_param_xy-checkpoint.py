#!/c/Apps/Anaconda3/python
# -*- coding: utf-8 -*-
"""
[Title] Scatter Chart
[Author] Yibeck Lee(yibec.Lee@gmail.com)
[Contents] 
 - Scatter Chart for FDC Parameters 
"""
## %matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

import pandas as pd

# font_path = 'C:/Windows/Fonts/나눔고딕코딩.ttf'
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv("WIP_HISTORY.csv")
print(df.columns)

plt.subplot(1,2,1)
plt.ylabel('Target(목표성능)')
plt.xlabel('Temperature(온도)')
plt.scatter(df['TEMPERATURE'],df['TARGET_VALUE'])
plt.subplot(1,2,2)
plt.ylabel('Target(목표성능)')
plt.xlabel('Thickness(두께)')
plt.scatter(df['THICKNESS'],df['TARGET_VALUE'])
plt.show()