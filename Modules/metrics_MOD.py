""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Produces the validation metrics in Table 4
"""

import numpy as np
import math
from RMS_func import RMS_func

def metrics_func(exp_data, sim_data, time_exp, time_sim, MVC, plateau_time1, plateau_time2): #Compute the validation metrics
    # First make the experimental and simulated arrays with the same sampling frequency
    if MVC == 30: # slightly reshaping the experimental array (2048 Hz) to have a high enough Gcd value with the simulated array (10000 Hz) for sampling
        B = np.zeros((85))
        A = np.ones((85))*time_exp[-1]
        exp_data = np.concatenate ((exp_data, B))
        time_exp = np.concatenate ((time_exp, A))
        k=100
    else:
        k=30
    Gcd = math.gcd(len(exp_data),len(sim_data))

    exp_jump = int(len(exp_data)/Gcd)
    sim_jump = int(len(sim_data)/Gcd)
    exp_data_reshaped = np.squeeze(exp_data[::exp_jump])
    exp_data_reshaped = exp_data_reshaped - np.min(exp_data_reshaped[0:k])
    sim_data_reshaped = sim_data[::sim_jump]
    time_exp_reshaped = time_exp[::exp_jump]
    time_sim_reshaped = time_sim[::sim_jump]    
    # plt.plot(exp_data_reshaped[0:200])
    # plt.plot(sim_data_reshaped[0:200])

    idx1 = np.argwhere(time_exp_reshaped<plateau_time1)[-1][0]
    idx2 = np.argwhere(time_exp_reshaped>plateau_time2)[0][0]
    avg_max_exp_data = np.mean(exp_data_reshaped[idx1:idx2])
    idx3 = np.argwhere(time_exp_reshaped<plateau_time1-1)[-1][0]
    idx4 = np.argwhere(time_exp_reshaped>plateau_time2+1)[0][0]

    idx5 = np.argwhere(time_exp_reshaped<plateau_time1+1)[-1][0]
    idx6 = np.argwhere(time_exp_reshaped>plateau_time2-1)[0][0]

    
    # Onset of Force error (in s) and experimental force at d1
    d1_exp = np.argwhere(exp_data_reshaped[k:-1]>np.max(exp_data_reshaped)*0.02)[0][0]+k
    d1_sim = np.argwhere(sim_data_reshaped>np.max(exp_data_reshaped)*0.02)[0][0]
    d1 = np.round(-time_exp_reshaped[d1_exp] + time_sim_reshaped[d1_sim],1)
    F_exp_d1 = int(exp_data_reshaped[d1_sim])

    # ME
    ME = np.round(np.max(abs(sim_data_reshaped-exp_data_reshaped)),0)

    # r2
    r2 = np.round(np.corrcoef(exp_data_reshaped, sim_data_reshaped)[0][1]**2 ,2)

    # nRMSE for ramps and plateau
    RMS_total = np.round(RMS_func(exp_data_reshaped, sim_data_reshaped)  / avg_max_exp_data *100,0)
    RMS_ramp1 = np.round(RMS_func(exp_data_reshaped[0:idx3], sim_data_reshaped[0:idx3])  / avg_max_exp_data*100,0)
    RMS_plateau = np.round(RMS_func(exp_data_reshaped[idx5:idx6], sim_data_reshaped[idx5:idx6])  / avg_max_exp_data*100,0)
    RMS_ramp2 = np.round(RMS_func(exp_data_reshaped[idx4:-1], sim_data_reshaped[idx4:-1])  / avg_max_exp_data*100,0)
    
    return d1, F_exp_d1, ME, RMS_total, RMS_ramp1, RMS_plateau, RMS_ramp2, r2