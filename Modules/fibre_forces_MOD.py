""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

At this stage, the time-histories of the MU forces (normalized_MU_Force_list) are computed. This function accounts for the asynchronous activity of the fibres constituting each MU, and acts as a low-pass filter
"""

import numpy as np

def fibre_forces_func(Nr, muscle_F0M, F0MU_distribution, normalized_MU_Force_list):
    Ta_fibres_number = 200000 # ~200,000 fibres in TA muscle (see manuscript)
    Unitary_fibre_force = muscle_F0M/Ta_fibres_number #assuming all fibre have similar maximum force-generating capacities
    nb_fibres_per_MU = (F0MU_distribution/Unitary_fibre_force).astype(int)
    
    
    Normalized_force_list_FIBRES = np.empty((Nr,len(normalized_MU_Force_list[0]))) 
    
    for i in range (Nr):
        if i%10==0: print(i, 'th MU fibres processed')
        for j in range (nb_fibres_per_MU[i][0]):
            decalage =  np.random.randint(0, 500) #any random delay between 0 and 10 ms
            decalage_array = np.zeros(decalage)
            transposed_act = np.transpose(normalized_MU_Force_list[i])[0]
            length = len(transposed_act)
            shrunk_act_array = transposed_act [0:length-decalage]
            Normalized_force_list_decal = np.concatenate((decalage_array,shrunk_act_array ))
            Normalized_force_list_FIBRES[i]=Normalized_force_list_FIBRES[i] + Normalized_force_list_decal 
        Normalized_force_list_FIBRES[i] = Normalized_force_list_FIBRES[i]/nb_fibres_per_MU[i]    
    
    return Normalized_force_list_FIBRES