""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

This function checks, with a given time precision (in seconds) whether a MN discharge at time t or not (from Matrix_AP)
"""

def is_t_a_firing_time_func(t_round, Matrix_AP, chosen_precision): 

    t_int=int(t_round/chosen_precision+10**-4) # integer in the scale of the chosen precision
    Matrix_AP_newprecision = (Matrix_AP/chosen_precision).astype(int)  # list of integers in the scale of chosen precision
    if t_int in Matrix_AP_newprecision:
        binary=1
    else:
        binary=0
    return binary