""" 
Author: Arnault CAILLET
arnault.caillet17@imperial.ac.uk
July 2023
Imperial College London
Department of Civil Engineering
Function necessary to compute the results presented in the manuscript Caillet et al. 'Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy' (2023)
---------

Activation-dependent FL relaitonship, fitted on human sarcomere data (Gollapudi et al, 2009)

"""

import numpy as np
def Force_Length_func(X, active_state=1.0, a=0.45) :
    b = 1.0*(0.15*(1-active_state)+1) 
    return np.exp(-((X-b)/a)**2)