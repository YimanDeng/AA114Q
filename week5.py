# -*- coding: utf-8 -*-
"""
Created on Thu May  5 00:34:09 2022

@author: Yiman
"""

import matplotlib.pyplot as plt
import math
import numpy as np


# plot R as a function of hub length
def plotR():
    hub_lengths = np.linspace(0, 0.1, 100)
    R_vals = []
    for hub_length in hub_lengths:
        R = math.sqrt((0.1834 + hub_length ** 2) / math.pi)
        R_vals.append(R)
    plt.xlabel('Hub Length (m)')
    plt.ylabel('Deployed Radius (m)')
    plt.plot(hub_lengths, R_vals)

if __name__ == '__main__':
    plotR()