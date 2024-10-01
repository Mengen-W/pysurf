#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:06:55 2024

@author: Kejia Li

This code reads surface energies from  surface_energy.csv, 
determine the most stable surface at a given Pb and I chemical potential,
and plots a color contour phase diagram.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


df = pd.read_csv('./data/surface_energy.csv')
"""
The .csv file should contain n_Cs, n_Pb, n_i, n_CsPbI3, E_formation, and	A
"""

#Define the formation enthalpy of CsPbI3
delta_H_CsPbI3=-5.774

def energy_form(row, delta_mu_pb, delta_mu_i):
    
    #Read data from df and calculate the surface energy 
    
    E_formation = row['E_formation']
    E_cs = row['n_Cs'] * (delta_H_CsPbI3 - delta_mu_pb - 3 * delta_mu_i)
    E_pb = row['n_Pb'] * delta_mu_pb
    E_i = row['n_i'] * delta_mu_i
    surface_area = row['A']
    return (E_formation - E_cs - E_pb - E_i)/2/surface_area


"""
Determine the most stable surface at the user-defined region of Pb and I chemical potentials.
"""
delta_mu_pb_lim=-2
delta_mu_i_lim=-1.5

most_stable = set()

for x in np.linspace(delta_mu_pb_lim, 0, num=50):
    for y in np.linspace(delta_mu_i_lim, 0, num=50):
        cal = float('inf')
        for index, row in df.iterrows():
            E_f = energy_form(row, x, y)
            if E_f < cal:
                cal = E_f
                most_stable_surface = [index]
            elif E_f == cal:
                most_stable_surface.append(index)
        most_stable.update(most_stable_surface)


print('Listing the surfaces that are stable in the phase diagram:')
stable_surfaces = df.iloc[list(most_stable)]
stable_surfaces.reset_index(drop=True, inplace=True)
print(stable_surfaces)
#print(stable_surfaces.iloc[:, 0])



print('Plotting the color contour phase diagram...')

x = np.linspace(0, -2, 600)
y = np.linspace(0, -1.5, 450)
z = np.empty((len(y), len(x)))

for ix, i in enumerate(x):
    for ij, j in enumerate(y):
        energy_list = []
        for index, row in stable_surfaces.iterrows():
            e = energy_form(row, i, j)
            energy_list.append(e)
        z[ij, ix] = energy_list.index(min(energy_list))



tick = np.arange(stable_surfaces.index.min()-0.5,
                 stable_surfaces.index.max()+1.5, 1)
labels = stable_surfaces.iloc[:, 0].tolist()
level = np.arange(stable_surfaces.index.min()-1,
                  stable_surfaces.index.max()+1, 1)
labels.append('surf')

fig = plt.figure()
fig.set_size_inches(9, fig.get_figheight())
fig.set_size_inches(16, fig.get_figwidth())
ax = fig.add_subplot(1, 1, 1)

CM = ax.contourf(x, y, z, levels=level, cmap=cm.Pastel1)

cbar = plt.colorbar(CM, ticks=tick, location='left')
cbar.ax.set_yticklabels(labels, fontsize=20)

"""
Plot the shaded area for thermodynamic stable region of bulk CsPbI3  
"""
x = np.arange(-1.852, 0.1, 0.01)
y_bottom = (-2.469-x)/2
y_top = (-2.414-x)/2
plt.fill_between(x, y_bottom, y_top, color='grey')



ax.xaxis.tick_top()
ax.yaxis.tick_right()
ax.xaxis.set_label_position('top')
ax.yaxis.set_label_position('right')
plt.xlabel(r'$\Delta\mu_{\mathrm{Pb}}$ (eV)', fontsize=30, labelpad=30)
plt.ylabel(r'$\Delta\mu_{\mathrm{I}}$ (eV)', fontsize=30, labelpad=30)
ax.set_xlim([-2, 0])
ax.set_ylim([-1.5, 0])
plt.tick_params(axis='x', width=3, length=7, labelsize=30)
plt.tick_params(axis='y', width=3, length=7, labelsize=30)

plt.xticks(np.arange(-2.0, 0, 0.4))
plt.yticks(np.arange(-1.5, 0, 0.2))

ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
plt.savefig('phase_diagram.jpeg',
            format='jpeg', dpi=300, bbox_inches='tight')

plt.tight_layout()

plt.show()
