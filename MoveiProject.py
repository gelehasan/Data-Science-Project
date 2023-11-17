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

#converted the columns with float to int type
df['budget'] = df['budget'].fillna(0).astype('int64')
df['gross'] = df['gross'].fillna(0).astype('int64')

#Extracting year from the column
df['year'] = df['released'].str.extract(r'(\d{4})')


# Sorting values by gross
df.sort_values(by="gross", inplace=True, ascending=False)

# displaying all the raws and columns
pd.set_option('display.max_rows', None)


#df["company"].drop_duplicates().sort_values(ascending=False)
df["company"].drop_duplicates()


#High corelation
# the more budget they spend the more they make
# Company will have a high corelation

# plotting the budget vs gross
plt.scatter(x=df["budget"], y=df["gross"])
plt.title("Budget vs Gross")

plt.xlabel("Gross Earning")

plt.ylabel("Budget Earning")

plt.show()



#budget vs gross using seaborn

sns.regplot( x="budget", y="gross", data=df, scatter_kws={"color":"red"}, line_kws={"color":"blue"})


#high correlation between budget and gross, i was write
df.corr()
#pearson, kandal, spearman
df.corr(method="pearson")


correlation_matrix= df.corr(method="pearson")

sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlation Matric for numeric features")

plt.xlabel("Movie Features")

plt.ylabel("Movie Features")


plt.show()
