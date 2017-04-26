import numpy as np
import matplotlib.pyplot as plt

def read_fisher(prefix) :
    data=np.load(prefix+"/fisher_raw.npz")
    
    fish_package={'names' :data['names'],
                  'values':data['values'],
                  'labels':data['labels'],
                  'fisher':data['fisher_tot'],
                  'bias'  :data['fisher_bias']}
    return fish_package

def print_sigmas(prefix) :
    pkg=read_fisher(prefix)
    cov=np.linalg.inv(pkg['fisher'])
    bias_vec=pkg['bias']
    for i,nm in enumerate(pkg['names']) :
        print nm+" = %lE"%(pkg['values'][i])+" +- %lE"%(np.sqrt(cov[i,i]))+" + %lE"%bias_vec[i]+"(bias)"

print_sigmas("outputs_nolens_bias/Fisher_all_nolens_bias")

