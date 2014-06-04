__author__ = "Shih-Ho Cheng" 

import pandas as pd
import numpy as np

def trimmed_significance(X, threshold=2.5, winsize=50):
    """Calculates the trimmed significance, i.e., Z-score "without outliers".
    """
    x = np.array(X)
    t = np.array(X.index)
    stat_arr = x[:winsize]
    sg_arr = np.repeat(float('NaN'), len(x))
    mu_arr = np.repeat(float('NaN'), len(x))
    sd_arr = np.repeat(float('NaN'), len(x))
    
    for i in range(winsize, len(x)):
        mu_arr[i] = np.mean(stat_arr)
        sd_arr[i] = np.std(stat_arr)
        sg_arr[i] = (x[i] - mu_arr[i])/sd_arr[i]
        if sg_arr[i] < threshold:
            stat_arr = np.delete(stat_arr, 0)
            stat_arr = np.append(stat_arr, x[i])
            
    output = pd.DataFrame(mu_arr, index=t, columns=['mu'])
    output['sd'] = pd.Series(sd_arr, index=t)
    output['sg'] = pd.Series(sg_arr, index=t)
    
    return output
