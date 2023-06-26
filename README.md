# Overview

The code in this repository implements a MN-driven neuromuscular model with motor unit resolution, coupled with subject-specific musculoskeletal anatomy, and driven by individual MN spike trains infered from decomposed HDEMG signals.
The code is associated with the following publication:

```
@article{caillet2023MN-drivenModelling,
  title={Motoneuron-driven computational muscle modelling with motor unit resolution and subject-specific musculoskeletal anatomy},
  author={Caillet, Arnault and Phillips, Andrew TM and Farina, Dario and Modenese, Luca},
  journal={XXX},
  year={2023}
}
```

# Instructions

1. Set up an environment using the provided 'environment.yml' file. To set up this environment, execute 'conda env create -f environment.yml' in your Anaconda Prompt, or visit the [conda website](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file ) for more detailed information.
2. activate the environment excuting 'conda activate _\<the name you chose for your environment\>_'.
3. To run the MN-driven model, run 'MN-driven_model.py'
4. To plot and display the results obtained with the five experimental datasets, already stored in the Results folder, 
run 'Display_results.py'
