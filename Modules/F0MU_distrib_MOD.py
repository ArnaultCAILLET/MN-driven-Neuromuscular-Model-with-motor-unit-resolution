""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Computes, using results from the literature, a distribution of MU max iso forces F0MU(j) for the simulated population of N or Nr MUs.
If only the experimental population of Nr MUs identified from HDEMG is considered, two approches are considered to deirved the F0MU distribution across that experimental sample
evenly: the Nr MUs are supposed to be homogeneously spread across the MU pool
identified: the Nr Mus are identified into the MU according to their torque recruitment thresholds and their representative F0MU values are adapted accordingly

"""
import numpy as np
from MN_properties_relationships_MOD import F0MU_norm_distrib_func, Fth_distrib_func

def F0MU_distrib_func(MVC, Nr, MN_pop, F0M, Input, Real_MN_pop,  spread='evenly'):
    MU_list_identified=np.arange(1, Nr+1, 1) #list of identified MUs (index)
    MU_pool_list = np.arange(1, MN_pop+1, 1) # Total MU pop in the TA = 400
    
    #### Let's scale the normalized distribution of MU F0MU (from literature) to Newtons
    # Let's compute the sum of the normalized F0MU(i)
    cumulative_all_MUs=sum(F0MU_norm_distrib_func(MU_pool_list,  MN_pop))
    #Obtaining, using the subject-specific F0M, the N-% relationship
    scale_factor = F0M/cumulative_all_MUs
    # and scaling the normalized distribution of F0MU 
    F0MU_distribution_complete_MU_pool = F0MU_norm_distrib_func(MU_pool_list,  MN_pop) * scale_factor
    
    if Input == '400': # if the completely reconstructed MU pool is considered, the F0MU_distribution_complete_MU_pool distirbution is directly applied to the discharging MU pop
        F0MU_distribution = F0MU_distribution_complete_MU_pool[0:Nr]
        
    elif Input=='Nr': # If only the Nr experimental MUs are considered, representative F0MU values must be derived, from F0MU_distribution_complete_MU_pool
        F0MU_distribution = np.empty(Nr)
        last_recruited_MU = np.argwhere(Fth_distrib_func(MU_pool_list,  MN_pop)<MVC)[-1][0]+1 #finding it with MVC value only. 'Blind' approach
        
        if spread == 'evenly': #easy approach: assuming the Nr identified MUs are evenly spread across the MU pool
            MU_list_identified = MU_list_identified * last_recruited_MU//Nr #Evenly spreading the Nr MUs across the MU pool
        elif spread == 'identified': #the identified MUs are here located into the MU pool according to their experimental Fth
            MU_list_identified = Real_MN_pop            

        # Here, each of the Nr identified MUs is conisdered to be representative of a fraction of the MUs of the MU pool, and of their summed F0Mu
        for i in range(0, len(MU_list_identified)):
            if i == 0 : 
                index_min = 0
            else: 
                index_min = int(MU_list_identified[i-1] + abs(MU_list_identified[i]-MU_list_identified[i-1])/2) +1
            if i == len(MU_list_identified)-1 : 
                index_max = last_recruited_MU +1
            else: 
                index_max = int(MU_list_identified[i] + abs(MU_list_identified[i+1]-MU_list_identified[i])/2)
            if index_max<index_min: index_max = index_min #because of this, some MUs may be counted two times. In such case, the sum of F0Ms must be scaled back to true value (see below)
            F0MU_distribution[i] = sum(F0MU_distribution_complete_MU_pool[index_min : index_max+1])
        
        F0MU_distribution = F0MU_distribution / sum(F0MU_distribution) * sum(F0MU_distribution_complete_MU_pool[0:last_recruited_MU]) #in case some MUs must have been counted twice

    F0MU_distribution = np.reshape(F0MU_distribution, (Nr,1))

    return F0MU_distribution


# plt.scatter(MU_list_identified, F0MU_distrib_func(MVC, Nr, MN_pop, F0M, Input, Real_MN_pop, spread='evenly'), s=1)
