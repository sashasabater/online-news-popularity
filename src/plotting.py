import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 





def plot_cols(df,num, target):
    for col in df.columns[:num]:
        fig, ax = plt.subplots()
        ax.scatter(df[col], df[target])
        ax.set_title(f'{col}')
        ax.set_ylabel(f'{target}')
        
    
    