# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:48:49 2023

@author: akhil
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_excel("a.xlsx")
print(data1)

plt.figure()

plt.plot(data1["year"], data1["Australia"], label="Australia")
plt.plot(data1["year"], data1["Bhutan"], label="Bhutan")
plt.plot(data1["year"], data1["Bulgaria"], label="Bulgaria")
plt.plot(data1["year"], data1["China"], label="China")

plt.xlabel("year")
plt.ylabel("country")
plt.legend()
plt.xticks(rotation = 90)
plt.show()