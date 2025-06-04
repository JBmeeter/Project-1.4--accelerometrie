# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 13:40:30 2025

@author: NatMe
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.interpolate import interp1d 
from scipy.integrate import solve_ivp
import numpy as np

#zet de directory voor de bestanden naar dezelfde folder and het bestand
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

#inlezen van het csv bestand
df = pd.read_csv('versnellingsprofiel_glad.csv')
t = df["# tijd (s)"]
a = df[" versnelling (m/s^2)"]

#bepaling van constantes
m = .12
M = .5
k1 = 2.8
b1 = (4*m*k1)**.5
x0 = 0
v0 = 0
a0 = 0
dt = t[1]-t[0]
dt2 = dt**2

# interpoleer de data uit het csv bestand, nodig voor de scipy functie
a_interp = interp1d(t, a, kind='cubic', fill_value="interpolate")

# functie definieeren
def system(t, y):
    x, v = y
    dxdt = v
    dvdt = (M * a_interp(t) - b1 * v - k1 * x) / m
    return [dxdt, dvdt]

# startwaarden invoeren voor het systeem
y0 = [x0, v0]  

# tijd-array instellen voor het berekenen
t_span = (t.iloc[0], t.iloc[-1])

# oplossen differentiaalvergelijking met scipy
sol_x1 = solve_ivp(system, t_span, y0, t_eval=t, method='RK45')

# output DV definieren voor berekening
x = sol_x1.y[0]

# versnellingsarrays aanmaken voor for-loop
a_a = np.zeros_like(t)
a_a[0] = a0

for i in range(0, len(t)):
    a_a[i] = (x[i]*k1)/M
    
# creeren daraframe om op te slaan als csv
DF = pd.DataFrame({
    "tijd (s)": t,
    "versnelling (m/s^2)": a_a
})

DF.to_csv('output numerieke accelerometer', sep=',')

# plotten 
plt.plot(sol_x1.t, sol_x1.y[0], label='x(t) - Position')
plt.plot(sol_x1.t, sol_x1.y[1], label='v(t) - Velocity')
plt.ylabel("afstand massa (m)")
plt.xlabel("tijd (s)")
plt.title('afstand massa k=2')
plt.legend()
plt.grid()
plt.show()

plt.plot(t, a, label='inputwaarden versnelling')
plt.plot(t, a_a, label='output versnelling')
plt.ylabel('versnelling (m/s^2)')
plt.xlabel('tijd (s)')
plt.title('berekende versnellingen')
plt.legend()
plt.grid()
plt.show()
