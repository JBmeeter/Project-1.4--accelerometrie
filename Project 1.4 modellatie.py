# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 20:13:08 2025

@author: NatMe
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#bepaling van constantes
massa = 10
Cveer = 2
Cdemp = 2*np.sqrt(massa*Cveer)
x = 5
v = 2
a0 = 0

#tijd array creëren
teind = 100
Nstap = 1000+1
tijd = np.linspace(0, teind, Nstap)
dt = teind/(Nstap-1)

#bepalen van startwaarden
i = 1
N_meting = len(t)
dt = 

#numerieke functie voor de afstand berekenen 
while i < len(t):
    a_num = (d[i+1]-2*d[i]+d[i-1])/(dt**2)

#versnelling functie
def versnelling(Cdemp, Cveer, massa, x, dx):
    a = (Cdemp/massa)*x + (Cveer/massa)*v + a0
    return a
    

print(versnelling(Cdemp, Cveer, massa, x, dx))

