#Importing 
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

%matplotlib inline

matplotlib.rcParams['figure.figsize']=(12,8)# it will adjust the configuration of the plots that will be created

# Read in data
df = pd.read_csv("movies.csv")

# Displaying the data
df.head()

#Checking if there is any invalid or null data
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))
