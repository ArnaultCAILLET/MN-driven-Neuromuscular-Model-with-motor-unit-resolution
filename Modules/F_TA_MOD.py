""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Computes, from a recorded force (Transd_Force) and the co-contractile activity of agonist and antagonist muscles (deltaT(x)), an estimation of the generated TA force (in N) during contraction 


"""


import numpy as np

def F_TA_func(Transd_Force, MVC, fs, range_start, range_stop, plateau_time1, plateau_time2):

    # 1. Remove offset 
    offset_Force_AU = Transd_Force[range_start:range_stop]-min(Transd_Force[0:6000])
    # 2. Normalize to the mean of the plateau (in arbitrary units)
    mean_Force_AU_plateau = np.mean(offset_Force_AU[plateau_time1*fs:plateau_time2*fs])
    norm_Force_AU = offset_Force_AU/mean_Force_AU_plateau #Normalized recorded Torque
    # 3. Scale the recorded Force to Nm (see manuscript, load cell documentation, and dynamometer geometry for the procedure)
    Force_Perc_MVC = norm_Force_AU*MVC # Recorded force in %MVC
    Torque_Nm = Force_Perc_MVC/100 * 0.23*0.10*981 # Recorded Force converted in torques in Nm
    # 4. Remove to the total torque the torque taken by co-contracting agonist and antagonist muscles 
    def deltaT(x): # Obtained from 2nd recorded session
        return -0.1202*np.exp(0.3453*x)
    Torque_Nm_TA_only = Torque_Nm - deltaT(Torque_Nm)
    # 5. Convert into TA force with TA moment arm
    Subj_Spec_TA_moment_arm = 0.0255
    F_TA = Torque_Nm_TA_only/Subj_Spec_TA_moment_arm 
    F_TA = F_TA- min(F_TA[0:6000])
    # 6. And finally normalize to validate neural drive
    F_TA_norm = F_TA / np.mean(F_TA[plateau_time1*fs:plateau_time2*fs]) #F_TA normalized

    return F_TA, F_TA_norm