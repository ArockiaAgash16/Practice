# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eTdX9wIMwIfp_VcMgJZzKBGq9T6E98Fk
"""

from google.colab import files


uploaded = files.upload()

import pandas as pd


# reading the database
data = pd.read_csv("tips.csv")

# printing the top 10 rows
display(data.head(10))

import pandas as pd
import matplotlib.pyplot as plt


# reading the database
data = pd.read_csv("tips.csv")

# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()