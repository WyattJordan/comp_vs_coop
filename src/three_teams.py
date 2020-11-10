from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from animate import rotanimate
from calc import coop_vs_comp
from plot import hide_axes, generate_imgs, make_gif

def heatmap(plot=True, text=False, gif=False, min_s=10, max_s=50):
    mpl.style.use('dark_background')
    sizesx = np.array(range(min_s,max_s))
    sizesy = sizesx
    sizesz = sizesx
    scenarios = np.stack(np.meshgrid(sizesx,sizesy,sizesz),axis=3).reshape(-1,3)
    
    results = coop_vs_comp(scenarios)

    over = float(len(results[results[:,2]>1.0,2]))
    total= float(len(results[:,2]))
    print("over is {} out of {}".format(over,total))
    prob = over/total
    print("Probability s_f > 1.0 for min {} and max {} is {}".format(min_s,max_s,prob))

    if plot:
        fig = plt.figure() #figsize=(7,5))
        ax = fig.add_subplot(111, projection='3d')
        print("scenarios shape "+str(scenarios.shape)+" results shape "+str(results.shape))
        step=1
        # scenarios = scenarios[results[:,2]>=1.0, :]
        ax.scatter(scenarios[:,0][::step], scenarios[:,1][::step],
                   scenarios[:,2][::step], c=results[:, 2][::step])
        # scenarios[:,2][::step], c=results[results[:,2]>1.0, 2][::step])    
        ax.view_init(azim=225)

    if text:
        # Axes settings for still photo
        ax.set_xlabel('Team 1 size')
        ax.set_ylabel('Team 2 size')
        ax.set_zlabel('Team 3 size')
        plt.title('Friendly Score >1.0 for Three Teams of Variable Sizes')
        ax.figure.set_size_inches(7,5)    

        ax.set_xticks(np.linspace(10,50,5))
        ax.set_yticks(np.linspace(10,50,5))
        ax.set_zticks(np.linspace(10,50,5))
        ax.figure.savefig('three_teams.jpeg', dpi=200)

    if gif:
        # Settings for making Gif
        hide_axes(ax)
        angles = np.linspace(0,360,101)[:-1]
        files = generate_imgs(ax, angles, width=7, height=5)
        make_gif(files,'three_teams_comp.gif', delay=5, repeat=True)

    if plot:
        plt.show()
        
        
