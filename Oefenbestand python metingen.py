# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 13:40:30 2025

@author: NatMe
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.integrate import cumtrapz
import numpy as np


# Set working directory to script's folder
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Get and print the current working directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

#inlezen van het csv bestand
df = pd.read_csv('Project oefenbestand 1.csv')

t = df["Data Set 1:Time(s)"]
a_meet = df["Data Set 1:Acceleration(m/s²)"]
v_meet = df["Data Set 1:Velocity(m/s)"]
d_meet = df["Data Set 1:Position(m)"]

#bepaling van startwaarden 
m = 5e-2
k = 2
b = 2*np.sqrt(m*k)
x0 = 5e-2

#afstandsfunctie
def x_massa(m, k, b, x0, x, v,):
    x_m = 
    return x_m

#plotten van de afstand werkelijk
plt.plot(t, d_meet, label="afstand gemeten (m)")
plt.ylabel("afstand gemeten (m)")
plt.xlabel("tijd (s)")
plt.grid()
plt.show()

plt.plot(t, a_meet, label="versnelling gemeten (m/s^2)")
plt.ylabel("versnelling (m/s)²")
plt.xlabel("tijd (s)")
plt.grid()
plt.show()

