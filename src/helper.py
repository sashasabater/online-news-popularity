import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error as mse 






def plot_cols(df,num, target):
    for col in df.columns[:num]:
        fig, ax = plt.subplots()
        ax.scatter(df[col], df[target])
        ax.set_title(f'{col}')
        ax.set_ylabel(f'{target}')

        
def model_test(model, X_tn, X_tst, y_tn, y_tst):
    model = model.fit(X_tn, y_tn)
    yhat = model.predict(X_tst)
    return mse(y_tst, yhat) ** .5
        
    
    