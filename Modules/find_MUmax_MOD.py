""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

In the case of a reconstructed MU population, identifies the MUs that display an average discharge frequency < 7Hz across the plateau of recorded torque
"""

import numpy as np

def find_MUmax_func(Firing_times_sim):
    for i in range(len(Firing_times_sim)):
        A = Firing_times_sim[i].size
        if A>0:
            k=i
    firing_frequencies = np.empty((k,), dtype=object)
    mean_firing_frequencies = np.zeros((k))
    
    for j in range (k):
        firing_frequencies[j] = 1/np.diff(Firing_times_sim[j])
        mean_firing_frequencies[j] = np.mean(firing_frequencies[j])
    MUs_below_7Hz = np.argwhere(mean_firing_frequencies<7)[0][0] #first idx of the MUs firing at less than 5 Hz  

 
    return MUs_below_7Hz