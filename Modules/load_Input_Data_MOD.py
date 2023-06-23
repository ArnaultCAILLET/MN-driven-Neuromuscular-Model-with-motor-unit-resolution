""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

The experimental data of MN spike trains (obtained from decomposed HDEMGs) and recorded force were pre-processed to enable the complete reconstruction of the
discharge activity of the complete MU pool, using another of our computational methods available at https://doi.org/10.1371/journal.pcbi.1010556

This function loads the experimental results, as well as the results obtained with that method.

Output data: 
 
%%% EXPERIMENTAL DATA %%%    
$ time: array of experimental time instants (fs = 2048Hz) 
$ MVC: maximum force developed during the contraction (30 or 50%) 
$ Force: Ankle force (in V) recorded with a force transducer
$ Nb_MN: number of MUs identified from HDEMGs
$ exp_disch_times: experimental discharge times for the Nb_MN (Nr) identified MNs (in samples) 

%%% DERIVED FROM EXPERIMENTAL DATA %%%
$ muscle_F0M: subject-specific max iso force of the TA muscle - DERIVED FROM SEGMENTED MRIs AND SUBJECT-SPECIFIC MSK MODEL
$ Real_MN_pop: location (index) of the Nb_MN identified MNs into the real pool of 400 MNs, identified according to their Torque recruitment thresholds - DERIVED WITH MN_distribution_MOD.py

%%% DERIVED USING THE COMPUTATIONAL TOOL at https://doi.org/10.1371/journal.pcbi.1010556 %%%
$ Firing_times_sim: reconstructed simulated discharge times (in seconds) for the complete MN pool of N MNs - DERIVED FROM COMPUTATIONAL TOOL at https://doi.org/10.1371/journal.pcbi.1010556

%%% DEFAULT PARAMETERS %%%
$ time_MU: array of simulation time instants (fs = 10,000Hz) - BY DEFAULT
$ MN_pop: total MN/MU population in the TA (400 MNs) - FROM LITERATURE (see manuscript)
$ range_start,range_stop, t_start, plateau_time1, plateau_time2, end_force, d: values identifying the times at which the contraction and its plateau start and stop
$ dt: simultation time step

"""

def load_Input_Data_func(test, path_to_data):
    import numpy as np 
    test_cases= np.array([                       
                            ['S1_30_256','TA', 10,  30, 38, 0.3,  400, 2048],
                            ['S1_50_256','TA', 14,  29, 40, 0.5,  400, 2048],
                            ['S1_30_64L','TA', 10,  30, 38, 0.3,  400, 2048],
                            ['S1_30_36L','TA', 10,  30, 38, 0.3,  400, 2048],
                            ['S1_50_64L','TA', 14,  29, 40, 0.5,  400, 2048],      
                          ], dtype=object)
    
    [test, muscle, plateau_time1, plateau_time2, end_force, MVC, MN_pop, fs]= test_cases[np.argwhere(test_cases==test)[0][0]]
    
    #Loading the results obtained from the 1_MAIN_MN_model code
    prefix = test+'_'
    Data = np.array(['time_array', 'exp_force', 'exp_discharge_times', 'PRED_discharge_times', 'parameters', 'MAIN_results' ])
    Data = np.core.defchararray.add(prefix, Data)
    Data = np.core.defchararray.add(Data, '.npy')
    
    time=np.load( path_to_data / test / Data[0], allow_pickle=True) # TIME ARRAY
    Force=np.load(path_to_data / test / Data[1], allow_pickle=True) #EXP FORCE
    exp_disch_times=np.load(path_to_data / test / Data[2], allow_pickle=True) #EXP SPIKE TRAINS
    Firing_times_sim=np.load(path_to_data / test / Data[3], allow_pickle=True) #PREDICTED SPIKE TRAINS
    [range_start,range_stop, t_start, end_force, Nb_MN] = np.load(path_to_data / test / Data[4], allow_pickle=True)[0:5] # time boundaries, conditions of simulation
    range_start,range_stop, t_start, end_force, Nb_MN = int(range_start),int(range_stop), int(t_start), int(float(end_force)), int(Nb_MN)
    Real_MN_pop = np.load(path_to_data / test / Data[5], allow_pickle=True)[0]
    # Additional parameter
    muscle_F0M=1046 #N
    d = end_force-t_start # duration of the simulation
    dt=1*10**-4 #time step for precision and calculation, 1E-4 at least, as the AP sinuses are of 7E-4 duration
    time_MU = np.arange(0, d, dt)
  
        
    return time,time_MU, muscle, MVC*100, Force, muscle_F0M, Nb_MN, MN_pop, Real_MN_pop, exp_disch_times, Firing_times_sim, range_start,range_stop, t_start, plateau_time1, plateau_time2, end_force, d, dt, fs