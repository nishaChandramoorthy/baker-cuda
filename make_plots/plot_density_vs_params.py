import os
import sys

from pylab import *
from numpy import *
from mpl_toolkits.axes_grid1 import make_axes_locatable

filenames = open('../data/density/filenames')
files = filenames.read().split('\n')[:-1]
for i in range(len(files)):
    d = load('../data/density/' + files[i])
    s = files[i].split('_')[2:6]
    d *= d.size / d.sum() / (2*pi)**2
    d = flipud(d)
    n = d.shape[0]
    dx = 2*pi/n
    print(max(amax(d,axis=1)))
    print(s)
    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    im = ax.imshow(d, interpolation='none', extent=[0, 2*pi, 0, 2*pi])

    ax.set_xlabel("$x_2$", fontsize=40)
    ax.set_ylabel("$x_1$", fontsize=40)
    ax.set_title('s = ' + s[0] + ', ' + s[1] + ', ' + s[2] + \
            ', ' + s[3], fontsize=40)

    ax.xaxis.set_tick_params(labelsize=40)
    ax.yaxis.set_tick_params(labelsize=40)
    
    plt.tight_layout()

    divider = make_axes_locatable(gca())
    cax = divider.append_axes("right", size="5%", pad=0.5)
    cbar = colorbar(im, cax=cax)
    cbar.ax.tick_params(labelsize=40)
