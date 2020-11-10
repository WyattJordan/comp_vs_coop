# Roadmap:

# calc.py
#      given list of team sizes calculate total coop and comp, (assumes relationship is all -1)
#      give list of team sizes and relationship scores give total coop and comp
#

# data.py
#      load and process democracy and population data

# viz.py
#      basic 2D plotting
#      3D plotting with marker color indicating score (red = comp, green = coop)

# main.py
#      sections for doing different pieces of the work
#      1 - score for equal team sizes
#      2 - score for unequal team sizes (3D plot, height is score value)
#      3 - score for 3 teams (3D plot, heatmap is score values)
#              add relationships? two teams in competition but both in more competition w/ the 3rd...
#      4 - real-world data (sports teams)
#      5 - real-world data w/ relationship factors (friends of democracy? find another dataset?)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

from calc import coop_vs_comp
from equal import equal_teams
from two_teams import variable_sizes
from three_teams import heatmap
from sports import sports_leagues
def main():

    # Equal team sizes
    # equal_teams()

    # Unequal various sizes
    # variable_sizes(animate="uncoooperative_teams", plot_low_scorers=False)
    # variable_sizes(plot_low_scorers=False)    

    # Three variable teams
    # heatmap(gif=True, text=False)
    # heatmap(plot=False, min_s=10, max_s=50)
    # heatmap(plot=False, min_s=10, max_s=100)
    # heatmap(plot=False, min_s=10, max_s=250)

    # Sports data
    sports_leagues()
    
if __name__ == "__main__":
    main()

