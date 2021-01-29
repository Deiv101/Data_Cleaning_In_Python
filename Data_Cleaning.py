### Project Goal
# > The goal of this project is to **Clean the dataset** to predict housing price fluctuations in New York City.
# - **First, let's import relevant libraries.**

# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

# - **Read the Data**

# Read the dataset
df = pd.read_csv('housing.csv')

# Check the first 5 entries
df.head()

# - **How many Rows and Columns?**

# Shape
print("There are \n", df.shape[0], "\nentries/rows and\n", 
      df.shape[1], "\nfeatures/columns in this daataset.")

# - **What are the datatypes pf each feature in this dataset?**

# Data Types
df.dtypes

# - **Which features/columns are numerical?**

# Numerical Columns
df_numeric = df.select_dtypes(include=[np.number])
df_numeric.columns.values
num_cols


# ### Data Cleaning
# #### Missing Data
# > **Technique #1**: **Missing Data Heatmap** 
# - Works best when there are fewer features

cols = df.columns[:] # All Columns
colors = ['#000099', '#ffff00'] # yellow indicates missing; blue indicates not missing
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colors))


# - - Yellow indicates Missing; Blue indicates not missing

# > **Technique #2**: **Missing Data Percentage List** 
# - Works best when there are many features in the dataset.


for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# > **Technique #3**: **Missing Data Histogram** 
# - Also works best when there are many features in the dataset.


for col in df.columns:
    missing = df[col].isnull()
    num_missing = np.sum(missing)
    
    if num_missing > 0:
        print('created missing indicator for: {}'.format(col))
        df['{}_ismissing'.format(col)] = missing
# based on the indicator,plot the histogra, of missing values
ismissing_cols = [col for col in df.columns if 'ismissing' in col]
df['num_missing'] = df[ismissing_cols].sum(axis=1)
df['num_missing'].value_counts().reset_index().sort_values(by='index').plot.bar(x='index', y='num_missing')



