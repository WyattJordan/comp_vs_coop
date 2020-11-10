from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from animate import rotanimate
from calc import coop_vs_comp
from plot import hide_axes

def variable_sizes(animate=None, plot_low_scorers=False):
    mpl.style.use('dark_background')    
    sizes = np.array(range(10,50))
    scenarios = np.dstack(np.meshgrid(sizes,sizes)).reshape(-1,2)
    results = coop_vs_comp(scenarios)

    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(scenarios[:,0], scenarios[:,1], results[:,2])
    data = np.hstack([scenarios, results])

    thresh = 1.0
    above_cond = np.array(data[:,4]>=thresh).astype(bool)
    below_cond = np.array(data[:,4]<thresh).astype(bool)
    split_cond = np.array(data[:,1] > data[:,0]).astype(bool)
    above_upper = data[np.logical_and(above_cond, split_cond),:]
    above_lower = data[np.logical_and(above_cond, np.logical_not(split_cond)),:]
    below_thresh = data[below_cond, :]
    # if not plot_low_scorers:
    #     au = ax.plot_trisurf(above_upper[:,0], above_upper[:,1], above_upper[:,4], cmap=cm.PiYG)
    #     al = ax.plot_trisurf(above_lower[:,0], above_lower[:,1], above_lower[:,4], cmap=cm.PiYG)
    # bt = ax.plot_trisurf(below_thresh[:,0],below_thresh[:,1],below_thresh[:,4], cmap=cm.PRGn_r)

    au = ax.plot_trisurf(data[:,0], data[:,1], data[:,4], cmap=cm.PiYG)
    print("size of overly comp teams is {} and of overly cooperative is {}".format(np.sum(below_cond), np.sum(above_cond)))
    print("teams with 10-50 players chosen at random have {}% chance of being cooperative".format(100.*np.sum(above_cond)/(np.sum(above_cond)+np.sum(below_cond))))

    ax.set_xticks(np.linspace(10,50,5))
    ax.set_yticks(np.linspace(10,50,5))
    plt.title('Friendly Score for Two Teams of Variable Sizes')
    ax.view_init(elev=30., azim=225)    
    plt.show()    
    ax.figure.savefig('2variable_teams.jpeg', dpi=200)    
    # ax.plot_trisurf(scenarios[:,0], scenarios[:,1], np.ones_like(scenarios[:,0]))
    # hide_axes(ax)
    # ax.elev = 30
    # angles = np.linspace(0,360,101)[:-1]
    # if not animate==None:
        # rotanimate(ax, angles, animate+".gif", delay=10, elevation=30)


