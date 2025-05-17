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
m = 5e-2
M = .5
k = 2
b = 2*((m*k)**.5)
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
    dvdt = (M * a_interp(t) - b * v - k * x) / m
    return [dxdt, dvdt]

# startwaarden invoeren voor het systeem
y0 = [x0, v0]  

# tijd-array instellen voor het berekenen
t_span = (t.iloc[0], t.iloc[-1])
t_eval = t 

# oplossen differentiaalvergelijking met scipy
sol_x = solve_ivp(system, t_span, y0, t_eval=t_eval, method='RK45')

# output DV definieren voor berekening
x = sol_x.y[0]
v_m = sol_x.y[1]

# versnellingsarrays aanmaken voor for-loop
a_m = np.zeros_like(t)
a_m[0] = a0
a_a = np.zeros_like(t)
a_a[0] = a0

# for-loop voor berekenen versnelling 
for i in range(1, len(t)-2):
    #v_m[i] = (x[i+1]-x[i-1])/(dt*2)
    a_m[i] = (v_m[i+1]-v_m[i-1])/(2*dt)
    a_a[i] = (m*a_m[i]+b*v_m[i]+k*x[i])/M

#(x[i+1]-2*x[i]+x[i-1])/dt2 (overige opties om a_m te bereken)
#(v_m[i]-v_m[i-1])/dt

# creeren daraframe om op te slaan als csv
DF = pd.DataFrame({
    "tijd (s)": t,
    "versnelling (m/s^2)": a_a  
})

DF.to_csv('output numerieke accelerometer', sep=',')

# plotten 
plt.plot(sol_x.t, sol_x.y[0], label='x(t) - Position')
plt.plot(sol_x.t, sol_x.y[1], label='v(t) - Velocity')
plt.ylabel("afstand massa (m)")
plt.xlabel("tijd (s)")
plt.title('afstand massa')
plt.legend()
plt.grid()
plt.show()

plt.plot(t, a, label='inputwaarden versnelling')
plt.plot(t, a_a, label="versnelling berekent (m/s^2)")
plt.ylabel('input versnelling (m/s^2')
plt.xlabel('tijd (s)')
plt.title('inputversnelling')
plt.legend()
plt.grid()
plt.show()

plt.plot(t, a, label='inputwaarden versnelling')
plt.ylabel('input versnelling (m/s^2')
plt.xlabel('tijd (s)')
plt.title('inputversnelling')
plt.legend()
plt.grid()
plt.show()
