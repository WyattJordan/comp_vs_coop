import pandas as pd
import numpy as np
from calc import coop_vs_comp

def democracy():
    demo = pd.read_csv(r'../data/nations.csv')
    pop  = pd.read_csv(r'../data/nations_populations.csv')
    df = demo.merge(pop, how='inner', left_on='Country', right_on='Country')

    pops = df['Population'].to_numpy(dtype=np.float64).reshape(1,-1)
    dem_score = df['Score'].to_numpy(dtype=np.float64).reshape(1,-1)

    dem_score = (dem_score - np.mean(dem_score)) / np.std(dem_score) # normalize between -1, and 1
    rel = np.matmul(dem_score.T, dem_score) # square, larger values are more coop
    rel = rel - np.amin(rel)   # min at 0.0
    rel = rel/np.amax(rel)     # max at 1.0
    rel = (1-rel) * 0.5        # invert (expects high score for comp) and scale

    results = coop_vs_comp(pops, rel)
    print("World friendliness score = {}".format(results[0][2]))
    
    

    
