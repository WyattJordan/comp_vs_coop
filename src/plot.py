from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

def hide_axes(ax):
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_zlabel('')
    
    ax.set_zticklabels([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.w_xaxis.set_pane_color((1., 1., 1., 0.))
    ax.w_yaxis.set_pane_color((1., 1., 1., 0.))
    ax.w_zaxis.set_pane_color((1., 1., 1., 0.))    
    
    ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))    

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

def generate_imgs(ax, angles, elevation=None, width=4, height=3,prefix='tmprot_', **kwargs):
    files = []
    ax.figure.set_size_inches(width,height)
     
    for i,angle in enumerate(angles):
     
        ax.view_init(elev = elevation, azim=angle)
        fname = '%s%03d.jpeg'%(prefix,i)
        ax.figure.savefig(fname, dpi=200)
        files.append(fname)
        if i%10 == 0:
            print('Generated %d out of %d frames' %(i, len(angles)))
    return files

def make_gif(files, output, delay=100, repeat=True, **kwargs):
    loop = -1 if repeat else 0
    print("Making gif of files...")
    # print('echo "-delay %d -loop %d %s %s"'                  
    os.system('convert -delay %d -loop %d %s %s'
              %(delay,loop," ".join(files),output))
    # for f in files:
    #     os.remove(f)


