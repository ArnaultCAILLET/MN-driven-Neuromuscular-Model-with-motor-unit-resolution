""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2021
Imperial College London
Department of Civil Engineering
"""

import numpy as np
import pandas as pd
import scipy.io

def EXP_DATA_PROCESSING_func(author, test, plateau_time2=32*2048):
    '''
This function
    1. loads the .mat file that stores the experimental data (MN discharge times and transducer force time histories)
    obtained from the decomposition of HDEMG signals. 
    2. orders the identified MNs in the order of incresaing force recruitment thresholds

Parameters
----------
author : name of the first author of the paper that provides the experimental data, string
test : name of the set of experimental data under study, string


Returns
-------
Nb_MN : the number of identified MNs in the experimental dataset, integer
Force : the time-history of transducer Force amplitude, array, arbitrary units
disch_times : the lists of the MN discharge times, matrix
    The discharge times are returned in samples (fs=2048 Hz in all datasets). disch_times is not a rectangle matrix.
    '''

# loading data
    path_to_data = '../Arnault_PHD_model/Input_Exp_Data/' 
    mat = scipy.io.loadmat(path_to_data + test+'.mat') 

#Extracting relevant data    
    for key, value in mat.items(): 
        if key=='MUPulses':
            disch_times_raw=np.array((value))[0]
        if key=='ref_signal':
            Force=np.array((value))[0]        
    # print(min(Force))
    Nb_MN=len(disch_times_raw) #Number of recorded MNs

# Ordering the spike trains from earliest to latest first discharge time
    disch_times_disorganised=np.empty((Nb_MN,), dtype=object) 
    first_disch=np.ones(Nb_MN) #storing the first discharge times, helping in raking the data

# first, reshaping the spike train data, and storing the first discharge times of each spike train    
    for i in range (Nb_MN): 
        disch_times_disorganised[i]=disch_times_raw[i][0].astype(object)
        first_disch[i]=disch_times_disorganised[i][0] #adding the recruitment time
    
# then, going through the array of recruitment times, and ranking each index of first_disch to sort the data
    order = first_disch.argsort()
    ranks = order.argsort()        
    disch_times=np.empty((Nb_MN,), dtype=object) 
    
    n=0
    for i in range (Nb_MN): 
        j=np.argwhere(ranks==i)[0][0]
        disch_times[i]=disch_times_disorganised[j]  
        if disch_times[i][0]>plateau_time2: n=n+1
    disch_times = disch_times[0: (len(disch_times)-n)]   
    Nb_MN = Nb_MN -n
    
    if author=='Caillet':        Force=(Force-np.min(Force))

    
    # if test=='GM_10': #This set of experiments has the first 4 MNs that start firing at lest than 1% force, let's remove them
    #     disch_times=disch_times[4:Nb_MN+1]
    #     Nb_MN=Nb_MN-4
                          
    return  Nb_MN, Force, disch_times