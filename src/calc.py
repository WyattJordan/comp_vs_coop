import numpy as np
# Scenarios is a 2D numpy array
# Each row contains the team sizes for teams 1 to n
def coop_vs_comp(scenarios, rel_scores=None):
    results = np.zeros([scenarios.shape[0],3])
    examples, n_teams = scenarios.shape

    # Relationships between teams.
    # 1 is perfectly competitive, -1 is perfectly cooperative
    if rel_scores == None:
        rel_scores = np.ones([n_teams,n_teams])
        
    for i in range(examples):
        coop = 0
        comp = 0
        
        for j in range(n_teams):
            curr_team = scenarios[i][j]
            coop += links_in_network(curr_team)
            for k in range(j+1, n_teams):
                comp += curr_team * scenarios[i][k] * rel_scores[j][k]
                
        results[i][0] = coop
        results[i][1] = comp
        results[i][2] = coop/comp        
    return results

def links_in_network(n):
    return n*(n-1)/2
