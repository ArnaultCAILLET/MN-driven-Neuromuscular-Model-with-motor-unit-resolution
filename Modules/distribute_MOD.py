""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Computes the distribution across the investigated MU sample of the mean of the MU-specific quantity (Data) across the plateau of recorded force. 
"""

import numpy as np

def distribute_func(i, k, path, data_npy_files_list, plateau_time1, plateau_time2, Trial): 
    Data = np.load(path[i] / data_npy_files_list[k], allow_pickle=True) #EXP FORCE
    Data = np.reshape(Data, (len(Data),1))
    Data_max=np.zeros((len(Data)))
    Data_max_mean=np.zeros((len(Data)))    

    for j in range(len(Data)):
        Data_max[j] = np.max(Data[j][0]) 
        Data_max_mean[j] = np.mean(Data[j][0][plateau_time1*10000:plateau_time2*10000]) 
    return Data_max_mean