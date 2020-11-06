import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from calc import coop_vs_comp

def equal_teams():
    mpl.style.use('dark_background')
    
    scenarios = np.repeat(np.arange(1,20).reshape(19,1), 2, axis=1)
    results = coop_vs_comp(scenarios)

    fig, ax1 = plt.subplots()
    # ax1.set_xbound(0, 25)
    ax1.set_ybound(0, 1.1)
    plt.title("Friendly Score Between Two Teams of Equal Size")

    friend = ax1.plot(results[:,2], 'go', label='Friendly Score')
    ax1.tick_params(axis='y',color='tab:green', width=5, length=7)
    ax1.set_ylabel("Cooperation / Competition Score")
    ax1.set_xlabel("Members per Team")
    ax1.set_xticks(np.linspace(0,20,11))

    ax2 = ax1.twinx()
    #ax2.set_yscale("log")
    ax2.set_ybound(0, 550)
    ax2.tick_params(axis='y',color='tab:red', width=5, length=7)    
    coop = ax2.plot(results[:,0], '*', color='xkcd:bluish', label='Cooperative Connections')
    comp = ax2.plot(results[:,1], '*', color='xkcd:deep red', label='Competitive Connections')
    # diff = ax2.plot(results[:,1] - results[:,0], '*', color='xkcd:barney purple', label='Difference')    

    lns = friend + coop + comp #+ diff
    labs = [l.get_label() for l in lns]
    ax1.legend(lns,labs)
    fig.set_size_inches(8,5)
    img = os.path.join(os.path.dirname(__file__),'../img/two_teams.png')
    plt.savefig(img)
    plt.show()
