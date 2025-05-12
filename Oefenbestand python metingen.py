# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 13:40:30 2025

@author: NatMe
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Set working directory to script's folder
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

#inlezen van het csv bestand
df = pd.read_csv('versnellingsprofiel_scherp.csv')

t = df["# tijd (s)"]
a = df[" versnelling (m/s^2)"]

#bepaling van constantes
m = 5e-2
k = 2
b = 2*((m*k)**.5)
x0 = 0.2
v0 = 0
dt = t[1]-t[0]

#positie en eerste stap
x = np.zeros_like(t)
x[0] = x0
x[1] = x0 + dt*v0

#snelheid en eerste stap
v = np.zeros_like(t)
v[0] = v0
v[1] = v0 + a[0]*dt

#for loop voor het berekenen van de positie van de massa TOV de sensor over de tijd
for i in range(1, len(t)-1):
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = (m*(a[i+1])-(b*v[i+1]))/k + x0
    

#plotten van de afstand werkelijk
plt.plot(t, x, label="afstand massa (m)")
plt.ylabel("afstand massa (m)")
plt.xlabel("tijd (s)")
plt.grid()
plt.show()

plt.plot(t, a, label="versnelling gemeten (m/s^2)")
plt.ylabel("versnelling (m/s)²")
plt.xlabel("tijd (s)")
plt.grid()
plt.show()

