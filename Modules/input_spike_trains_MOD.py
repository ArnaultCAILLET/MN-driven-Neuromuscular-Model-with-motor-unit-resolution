""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

This function loads the trains of discharge times (in sec) 

"""


def input_spike_trains_func(Input_MU_pop, Nb_MN, Firing_times_sim, exp_disch_times, fs):
    #LOADING SPIKE TRAINS (MN_pop or Nr)
    if Input_MU_pop=='400': 
        sp_matrix = Firing_times_sim
        n=0
        while len(sp_matrix[n])>0:
            n=n+1
        sp_matrix=sp_matrix[0:n] #The predicted spike trains for the entire pool of 400 MNs are used as inputs. However, a number n<MN_pop of MNs are actually recruited and fire. The sp matrices are thus of length n and not MN_pop=400
        Nr=len(sp_matrix) #Number of firing MNs
    
    elif Input_MU_pop=='Nr': 
        sp_matrix = exp_disch_times/fs
        Nr = Nb_MN    
    return Nr, sp_matrix

