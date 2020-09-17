import os
import sys

from pylab import *
from numpy import *
from mpl_toolkits.axes_grid1 import make_axes_locatable


d = load('density/bakers_density_0.1_0.0_0.1_0.0_endeavour_1024_0.8675180312145866.npy')

d *= d.size / d.sum() / (2*pi)**2
d = flipud(d)
n = d.shape[0]
dx = 2*pi/n
mar_den_y = sum(d, axis=1)
max_inds = argsort(mar_den_y)[-20:]
max_inds = max_inds[[2,-2,-1]]
n_inds = max_inds.size
n_pts = 50
x = dx*max_inds*ones([n_pts,1])
y = max(dx*mar_den_y)*arange(n_pts)*ones([n_inds,1])/n_pts
fig = figure(figsize=(10, 5))
ax = fig.add_subplot(111)
ax.plot(dx*arange(n), mar_den_y*dx, lw=2.5)
ax.plot(x, y.T, "--", lw=2.5)

ax.grid(True)
ax.set_xlabel("$x_2$", fontsize=40)
ax.set_ylabel("$\mu_{x_2}$", fontsize=40)
plt.tight_layout()
#im = imshow(d, origin='lower', interpolation='none', extent=[0,
#2*pi, 0, 2*pi])
for tick in gca().xaxis.get_major_ticks():
    tick.label.set_fontsize(40)
for tick in gca().yaxis.get_major_ticks():
    tick.label.set_fontsize(40)

fig = figure(figsize=(7, 5))
ax = fig.add_subplot(111)
ci = ['orange', 'green', 'red']
for i in range(n_inds):
    ax.plot(dx*arange(n), d[max_inds[i]]/sum(d[max_inds[i]]), \
        color=ci[i],\
        lw=2.5)
ax.grid(True)
ax.set_xlabel("$x_1$", fontsize=40)
ax.set_ylabel("$\mu_{x_1|x_2}$", fontsize=40)
plt.tight_layout()
for tick in gca().xaxis.get_major_ticks():
    tick.label.set_fontsize(40)
for tick in gca().yaxis.get_major_ticks():
    tick.label.set_fontsize(40)


#divider = make_axes_locatable(gca())
#cax = divider.append_axes("right", size="5%", pad=0.5)
#cbar = colorbar(im, cax=cax)
#cbar.ax.tick_params(labelsize=40)

