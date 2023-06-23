""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Computes the path to fecth the files storing the results of the simulation
"""

import numpy as np

def dataname_func(N_Nr_Input, Trial, distrib_approach, Data, i):
    k = N_Nr_Input[i]
    prefix = k+Trial
    prefix = prefix + distrib_approach[i]
    data = np.core.defchararray.add(prefix, Data)
    data = np.core.defchararray.add(data, '.npy') 
    return data    