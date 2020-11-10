import pandas as pd
import numpy as np
from calc import coop_vs_comp

def sports_leagues():
    df = pd.read_csv(r'../data/sports.csv')
    leagues = []
    names = []
    results = []
    
    for i, name in enumerate(df.columns):
        ser = df[name][1:]
        a = ser.to_numpy(dtype=np.float32)
        a = a[~np.isnan(a)].reshape(1,-1)
        res = coop_vs_comp(a)
        names.append(name)
        leagues.append(a)        
        results.append(res)

    for n,l,r in zip(names, leagues, results):
        print("|{}        | {:.4f}        | {}      |".format(n, r[0][2], len(l[0])))
